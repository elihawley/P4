import pyhop
import json

def check_enough (state, ID, item, num):
	if getattr(state,item)[ID] >= num: return []
	return False

def produce_enough (state, ID, item, num):
	return [('produce', ID, item), ('have_enough', ID, item, num)]

pyhop.declare_methods ('have_enough', check_enough, produce_enough)

def produce (state, ID, item):
	return [('produce_{}'.format(item), ID)]

pyhop.declare_methods ('produce', produce)

# method names should have `produce_` as a prefix
def make_method (name, rule):
	recipe = list(rule.values())[0]
	def and_method (state, ID):
		op_node = (f'op_{name}', ID)
		reqs = []
		for item_or_tool_name, req_num in {**recipe.get('Requires', {}), **recipe.get('Consumes', {})}.items():
			reqs.append(('have_enough', ID, item_or_tool_name, req_num))
		return [*reqs, op_node]
	and_method.__name__ = name
	return and_method

def declare_methods (data):
	# some recipes are faster than others for the same product even though they might require extra tools
	# sort the recipes so that faster recipes go first

	# your code here
	# hint: call make_method, then declare the method to pyhop using pyhop.declare_methods('foo', m1, m2, ..., mk)
	
	# For every Produce-able item/tool,
	# 1. create an AND method for every operator that directly produces it
	# 2. create AND methods for alternative paths to produce it
	# 3. sort and declare them as children of an OR method (which has the produce_ prefix)
	for item_name in [*data['Items'], *data['Tools']]:
		and_methods_with_costs = []
		recipes_that_directly_produce_item = {recipe_name: recipe for recipe_name, recipe in data['Recipes'].items() if item_name in recipe['Produces']}

		for recipe_name, recipe in recipes_that_directly_produce_item.items():
			# Create an AND method for operators that directly produce the item
			direct_and_method_name = recipe_name.replace(" ", "_")
			rule = {recipe_name: recipe}
			direct_and_method = make_method(direct_and_method_name, rule)
			cost = recipe['Time']
			and_methods_with_costs.append((direct_and_method, cost))

		# Sort AND methods by cost
		and_methods_with_costs.sort(key=lambda and_method_with_costs: and_method_with_costs[1])

		# For a given item, create an OR method with sorted AND methods as children
		pyhop.declare_methods(f'produce_{item_name}', *[and_method_with_cost[0] for and_method_with_cost in and_methods_with_costs])

	return

def make_operator (rule):
	op_name = "op_" + list(rule.keys())[0].replace(" ", "_")
	recipe = list(rule.values())[0]
	def operator (state, ID):
		if state.time[ID] >= recipe['Time'] and all(getattr(state, item_or_tool_name, {ID: 0})[ID] >= req_num for item_or_tool_name, req_num in {**recipe.get('Requires', {}), **recipe.get('Consumes', {})}.items()):
			state.time[ID] -= recipe['Time']
			for item_or_tool_name, num in recipe.get('Produces', {}).items():
				if not getattr(state, item_or_tool_name) or ID not in getattr(state, item_or_tool_name):
					setattr(state, item_or_tool_name, {ID: 0})
				getattr(state, item_or_tool_name)[ID] += num
			for item_or_tool_name, num in recipe.get('Consumes', {}).items():
				if not getattr(state, item_or_tool_name) or ID not in getattr(state, item_or_tool_name):
					raise Exception('Item does not exist for consuming')
				getattr(state, item_or_tool_name)[ID] -= num
			return state
		return False
	operator.__name__ = op_name
	return operator

def declare_operators (data):
	# your code here
	ops = []
	for recipe_name, recipe in data['Recipes'].items():
		rule = {recipe_name: recipe}
		op = make_operator(rule)
		ops.append(op)
	# hint: call make_operator, then declare the operator to pyhop using pyhop.declare_operators(o1, o2, ..., ok)
	pyhop.declare_operators(*ops)
	return

def add_heuristic (data, ID):
	# prune search branch if heuristic() returns True
	# do not change parameters to heuristic(), but can add more heuristic functions with the same parameters: 
	# e.g. def heuristic2(...); pyhop.add_check(heuristic2)
	def heuristic (state, curr_task, tasks, plan, depth, calling_stack):
		# your code here
		hard_item = {'cart', 'coal', 'cobble', 'ingot', 'ore', 'rail', 'furnace'}
		if (all([goal_item in hard_item for goal_item in data['Goal'].keys()])):
			newops = []
			for recipe_name, recipe in data['Recipes'].items():
				if recipe_name not in {'iron_axe for wood', 'stone_axe for wood', 'wooden_axe for wood', 'craft wooden_axe at bench', 'craft stone_axe at bench', 'craft iron_axe at bench'}:
					rule = {recipe_name: recipe}
					newop = make_operator(rule)
					newops.append(newop)
			
			pyhop.declare_operators(*newops)

			wood_punch = []
			recipes_that_directly_produce_item = {recipe_name: recipe for recipe_name, recipe in data['Recipes'].items() if 'wood' in recipe['Produces']}
			for recipe_name, recipe in recipes_that_directly_produce_item.items():
				if recipe_name == 'punch for wood':
					direct_and_method_name = recipe_name.replace(" ", "_")
					rule = {recipe_name: recipe}
					direct_and_method = make_method(direct_and_method_name, rule)
					cost = recipe['Time']
					wood_punch.append((direct_and_method, cost))
			pyhop.declare_methods('produce_wood', *[and_method_with_cost[0] for and_method_with_cost in wood_punch])
		# Already reached goal, so finish.
		if (all([getattr(state, goal_item, {ID: 0})[ID] >= req_num for goal_item, req_num in data['Goal'].items()])):
			if len(tasks) > 1:
				return True
			else:
				# For trivial case: start with goal items
				return False
		# No time left, so finish.
		if (state.time[ID] == 0):
			return True

		# If a tool has already been made, don't make more of it.
		if (curr_task[0] == 'produce' and curr_task[2] in data['Tools'] and getattr(state, curr_task[2], {ID: 0})[ID] >= 1):
			return True
		if (curr_task[0] == 'produce' and curr_task[2] in data['Tools'] and curr_task in calling_stack):
			return True

		# Don't produce more of an item if you already have enough for the current task.
		# Special case: Coal and ore depend on how many ingots we need
		if (curr_task[0] == 'produce' and curr_task[2] in data['Items'] and getattr(state, curr_task[2], {ID:0})[ID] >= sum(method[3] for method in tasks if method[0] == 'have_enough' and method[2] == curr_task[2]) \
			or (curr_task[0] == 'produce' and curr_task[2] in ['coal', 'ore'] and getattr(state, curr_task[2], {ID:0})[ID] >= sum(method[3] for method in tasks if method[0] == 'have_enough' and method[2] == 'ingot'))):
			return True

		# If only wood items/tools are needed, don't bother considering non_wood items/tools.
		wood_only_items = {"bench", "wooden_axe", "wooden_pickaxe", "stick", "wood", "plank"}
		non_wood_only_items = {'cart', 'coal', "cobble", "ingot", "ore", "rail", "furnace", "iron_axe", "iron_pickaxe", "stone_axe", "stone_pickaxe"}
		if (all([goal_item in wood_only_items for goal_item in data['Goal'].keys()])):
			if (curr_task[0] == 'have_enough' and curr_task[2] in non_wood_only_items):
				return True
		
		# Skip making an unneeded axe
		if (getattr(state, 'iron_axe', {ID:0})[ID] >= 1 and (curr_task[0] == 'produce' and curr_task[2] == 'stone_axe') and getattr(state, 'stone_axe', {ID:0})[ID] >= data['Goal'].get('stone_axe', 0)):
			return True
		if (getattr(state, 'iron_axe', {ID:0})[ID] >= 1 and (curr_task[0] == 'produce' and curr_task[2] == 'wooden_axe') and getattr(state, 'wooden_axe', {ID:0})[ID] >= data['Goal'].get('wooden_axe', 0)):
			return True
		if (getattr(state, 'stone_axe', {ID:0})[ID] >= 1 and (curr_task[0] == 'produce' and curr_task[2] == 'iron_axe') and getattr(state, 'iron_axe', {ID:0})[ID] >= data['Goal'].get('iron_axe', 0)):
			return True
		if (getattr(state, 'stone_axe', {ID:0})[ID] >= 1 and (curr_task[0] == 'produce' and curr_task[2] == 'wooden_axe') and getattr(state, 'wooden_axe', {ID:0})[ID] >= data['Goal'].get('wooden_axe', 0)):
			return True

		# Skip making an unneeded pickaxe
		# Don't bother making or using a pickaxe if we have a better one
		if getattr(state, 'iron_pickaxe', {ID:0})[ID] >= 1:
			if (curr_task[0] == 'produce' and curr_task[2] in {'stone_pickaxe', 'wooden_pickaxe'}):
				return True
			if (curr_task[0].startswith('op_stone_pickaxe_for') or curr_task[0].startswith('op_wooden_pickaxe_for')):
				return True
		if getattr(state, 'stone_pickaxe', {ID:0})[ID] >= 1:
			if (curr_task[0] == 'produce' and curr_task[2] in {'wooden_pickaxe'}):
				return True
			if (curr_task[0].startswith('op_wooden_pickaxe_for')):
				return True

		return False # if True, prune this branch

	pyhop.add_check(heuristic)


def set_up_state (data, ID, time=0):
	state = pyhop.State('state')
	state.time = {ID: time}

	for item in data['Items']:
		setattr(state, item, {ID: 0})

	for item in data['Tools']:
		setattr(state, item, {ID: 0})

	for item, num in data['Initial'].items():
		setattr(state, item, {ID: num})

	return state

def set_up_goals (data, ID):
	goals = []
	for item, num in data['Goal'].items():
		goals.append(('have_enough', ID, item, num))

	return goals

if __name__ == '__main__':
	rules_filename = 'crafting.json'

	with open(rules_filename) as f:
		data = json.load(f)

	state = set_up_state(data, 'agent', time=250) # allot time here
	goals = set_up_goals(data, 'agent')

	declare_operators(data)
	declare_methods(data)
	add_heuristic(data, 'agent')

	# pyhop.print_operators()
	pyhop.print_methods()

	# Hint: verbose output can take a long time even if the solution is correct; 
	# try verbose=1 if it is taking too long
	pyhop.pyhop(state, goals, verbose=3)
	# pyhop.pyhop(state, [('have_enough', 'agent', 'cart', 1),('have_enough', 'agent', 'rail', 20)], verbose=3)
    # Given {}, achieve {'plank': 1} [time <= 300]
    # Given {}, achieve {'wooden_pickaxe': 1} [time <=300]
    # Given {}, achieve {'furnace': 1} [time <= 300]
    # Given {}, achieve {'cart': 1} [time <= 300]
    # Given {'plank': 1}, achieve {'plank': 1} [time <= 0]
    # Given {'plank': 3, 'stick': 2}, achieve {'wooden_pickaxe': 1} [time <= 10]
    # Given {}, achieve {'stone_pickaxe': 1} [time <= 40]
    # Given {}, achieve {'iron_pickaxe': 1} [time <= 100]
    # Given {}, achieve {'cart': 1, 'rail': 10} [time <= 175]
    # Given {}, achieve {'cart': 1, 'rail': 20} [time <= 250]