import pyhop

'''begin operators'''

def op_punch_for_wood (state, ID):
	if state.time[ID] >= 4:
		state.wood[ID] += 1
		state.time[ID] -= 4
		return state
	return False

def op_craft_wooden_axe_at_bench (state, ID):
	if state.time[ID] >= 1 and state.bench[ID] >= 1 and state.plank[ID] >= 3 and state.stick[ID] >=2:
		state.wooden_axe[ID] += 1
		state.plank[ID] -= 3
		state.stick[ID] -= 2
		state.time[ID] -= 1
		return state
	return False
# your code here

def op_craft_plank (state, ID):
	if state.time[ID] >= 1 and state.wood[ID] >= 1:
		state.plank[ID] += 4
		state.wood[ID] -= 1
		state.time[ID] -= 1
		return state
	return False

def op_craft_stick (state, ID):
	if state.time[ID] >= 1 and state.plank[ID] >= 2:
		state.stick[ID] += 4
		state.plank[ID] -= 2
		state.time[ID] -= 1
		return state
	return False

def op_craft_bench (state, ID):
	if state.time[ID] >= 1 and state.plank[ID] >= 4:
		state.bench[ID] += 1
		state.plank[ID] -= 4
		state.time[ID] -= 1
		return state
	return False

def op_craft_wooden_pickaxe_at_bench (state, ID):
	if state.time[ID] >= 1 and state.bench[ID] >= 1 and state.plank[ID] >= 3 and state.stick[ID] >=2:
		state.wooden_pickaxe[ID] += 1
		state.plank[ID] -= 3
		state.stick[ID] -= 2
		state.time[ID] -= 1
		return state
	return False

def op_mine_with_wood_for_cobble (state, ID):
	if state.time[ID] >= 4 and state.wooden_pickaxe[ID] >= 1:
		state.cobble[ID] += 1
		state.time[ID] -= 4
		return state
	return False

def op_mine_with_wood_for_coal (state, ID):
	if state.time[ID] >= 4 and state.wooden_pickaxe[ID] >= 1:
		state.coal[ID] += 1
		state.time[ID] -= 4
		return state
	return False

def op_mine_with_wood_for_wood (state, ID):
	if state.time[ID] >= 2 and state.wooden_axe[ID] >= 1:
		state.wood[ID] += 1
		state.time[ID] -= 2
		return state
	return False

def op_craft_furnace_at_bench (state, ID):
	if state.time[ID] >= 1 and state.bench[ID] >= 1 and state.cobble[ID] >= 8:
		state.furnace[ID] += 1
		state.cobble[ID] -= 8
		state.time[ID] -= 1
		return state
	return False

def op_craft_stone_pickaxe_at_bench (state, ID):
	if state.time[ID] >= 1 and state.bench[ID] >= 1 and state.cobble[ID] >= 3 and state.stick[ID] >=2:
		state.stone_pickaxe[ID] += 1
		state.cobble[ID] -= 3
		state.stick[ID] -= 2
		state.time[ID] -= 1
		return state
	return False

def op_craft_stone_axe_at_bench (state, ID):
	if state.time[ID] >= 1 and state.bench[ID] >= 1 and state.cobble[ID] >= 3 and state.stick[ID] >=2:
		state.stone_axe[ID] += 1
		state.cobble[ID] -= 3
		state.stick[ID] -= 2
		state.time[ID] -= 1
		return state
	return False

def op_mine_with_stone_for_cobble (state, ID):
	if state.time[ID] >= 2 and state.stone_pickaxe[ID] >= 1:
		state.cobble[ID] += 1
		state.time[ID] -= 2
		return state
	return False

def op_mine_with_stone_for_coal (state, ID):
	if state.time[ID] >= 2 and state.stone_pickaxe[ID] >= 1:
		state.coal[ID] += 1
		state.time[ID] -= 2
		return state
	return False

def op_mine_with_stone_for_ore (state, ID):
	if state.time[ID] >= 4 and state.stone_pickaxe[ID] >= 1:
		state.ore[ID] += 1
		state.time[ID] -= 4
		return state
	return False

def op_mine_with_stone_for_wood (state, ID):
	if state.time[ID] >= 1 and state.stone_axe[ID] >= 1:
		state.wood[ID] += 1
		state.time[ID] -= 1
		return state
	return False

def op_smelt_ore_at_furnace (state, ID):
	if state.time[ID] >= 5 and state.furnace[ID] >= 1 and state.coal[ID] >= 1 and state.ore[ID] >= 1:
		state.ingot[ID] += 1
		state.coal[ID] -= 1
		state.ore[ID] -= 1
		state.time[ID] -= 5
		return state
	return False

def op_craft_iron_axe_at_bench (state, ID):
	if state.time[ID] >= 1 and state.bench[ID] >= 1 and state.ingot[ID] >= 3 and state.stick[ID] >=2:
		state.iron_axe[ID] += 1
		state.ingot[ID] -= 3
		state.stick[ID] -= 2
		state.time[ID] -= 1
		return state
	return False

def op_craft_iron_pickaxe_at_bench (state, ID):
	if state.time[ID] >= 1 and state.bench[ID] >= 1 and state.ingot[ID] >= 3 and state.stick[ID] >=2:
		state.iron_pickaxe[ID] += 1
		state.ingot[ID] -= 3
		state.stick[ID] -= 2
		state.time[ID] -= 1
		return state
	return False

def op_craft_rail_at_bench (state, ID):
	if state.time[ID] >= 1 and state.bench[ID] >= 1 and state.ingot[ID] >= 6 and state.stick[ID] >=1:
		state.rail[ID] += 16
		state.ingot[ID] -= 6
		state.stick[ID] -= 1
		state.time[ID] -= 1
		return state
	return False

def op_craft_cart_at_bench (state, ID):
	if state.time[ID] >= 1 and state.bench[ID] >= 1 and state.ingot[ID] >= 5:
		state.cart[ID] += 1
		state.ingot[ID] -= 5
		state.time[ID] -= 1
		return state
	return False

def op_mine_with_iron_for_cobble (state, ID):
	if state.time[ID] >= 1 and state.iron_pickaxe[ID] >= 1:
		state.cobble[ID] += 1
		state.time[ID] -= 1
		return state
	return False

def op_mine_with_iron_for_coal (state, ID):
	if state.time[ID] >= 1 and state.iron_pickaxe[ID] >= 1:
		state.coal[ID] += 1
		state.time[ID] -= 1
		return state
	return False

def op_mine_with_iron_for_ore (state, ID):
	if state.time[ID] >= 2 and state.iron_pickaxe[ID] >= 1:
		state.ore[ID] += 1
		state.time[ID] -= 2
		return state
	return False

def op_mine_with_iron_for_wood (state, ID):
	if state.time[ID] >= 1 and state.iron_axe[ID] >= 1:
		state.wood[ID] += 1
		state.time[ID] -= 1
		return state
	return False

pyhop.declare_operators (op_punch_for_wood, op_craft_wooden_axe_at_bench, op_craft_plank, op_craft_stick, op_craft_bench, op_craft_wooden_pickaxe_at_bench, 
						 op_mine_with_wood_for_cobble, op_mine_with_wood_for_coal, op_mine_with_wood_for_wood,
						 op_craft_furnace_at_bench, op_craft_stone_axe_at_bench, op_craft_stone_pickaxe_at_bench,
						 op_mine_with_stone_for_coal, op_mine_with_stone_for_cobble, op_mine_with_stone_for_ore, op_mine_with_stone_for_wood,
						 op_smelt_ore_at_furnace, op_craft_iron_axe_at_bench, op_craft_iron_pickaxe_at_bench, op_craft_rail_at_bench, op_craft_cart_at_bench,
						 op_mine_with_iron_for_coal, op_mine_with_iron_for_cobble, op_mine_with_iron_for_ore, op_mine_with_iron_for_wood)

'''end operators'''

def check_enough (state, ID, item, num):
	if getattr(state,item)[ID] >= num: return []
	return False

def produce_enough (state, ID, item, num):
	return [('produce', ID, item), ('have_enough', ID, item, num)]

def produce (state, ID, item):
	if item == 'wood': 
		"""if state.made_iron_axe[ID] == True:
			return [('produce_iron_wood', ID)]
		elif state.made_stone_axe[ID] == True:
			return [('produce_stone_wood', ID)]
		elif state.made_wooden_axe[ID] == True:
			return [('produce_wood_wood', ID)]
		elif state.wood[ID] >= 3 and state.made_bench[ID] == False:
			state.made_wooden_axe[ID] = True
			return [('produce_wooden_axe', ID)]"""
		return [('produce_wood', ID)]
	# your code here
	elif item == 'plank':
		return [('produce_plank', ID)]
	elif item == 'stick':
		return [('produce_stick', ID)]
	elif item == 'cobble':
		"""if state.made_iron_pickaxe[ID] == True:
			return [('produce_iron_cobble', ID)]
		elif state.made_stone_pickaxe[ID] == True:
			return [('produce_stone_cobble', ID)]
		elif state.made_wooden_pickaxe[ID] == True:
			return [('produce_wood_cobble', ID)]
		state.made_wooden_pickaxe[ID] = True
		return [('produce_wooden_pickaxe', ID)]"""

		return [('produce_cobble', ID)]
	
	elif item == 'coal':
		"""if state.made_iron_pickaxe[ID] == True:
			return [('produce_iron_coal', ID)]
		elif state.made_stone_pickaxe[ID] == True:
			return [('produce_stone_coal', ID)]
		elif state.made_wooden_pickaxe[ID] == True:
			return [('produce_wood_coal', ID)]
		state.made_wooden_pickaxe[ID] = True
		return [('produce_wooden_pickaxe', ID)]"""

		return [('produce_coal', ID)]
	
	elif item == 'ore':
		"""if state.made_iron_pickaxe[ID] == True:
			return [('produce_iron_ore', ID)]
		elif state.made_stone_pickaxe[ID] == True:
			return [('produce_stone_ore', ID)]
		state.made_stone_pickaxe[ID] = True
		return [('produce_stone_pickaxe', ID)]"""

		return [('produce_ore', ID)]
	
	elif item == 'ingot':
		return [('produce_ingot', ID)]
	elif item == 'rail':
		return [('produce_rail', ID)]
	elif item == 'cart':
		return [('produce_cart', ID)]
	
	elif item == 'bench':
		if state.made_bench[ID] is True:
			return False
		else:
			state.made_bench[ID] = True
		return [('produce_bench', ID)]
	
	elif item == 'furnace':
		if state.made_furnace[ID] is True:
			return False
		else:
			state.made_furnace[ID] = True
		return [('produce_furnace', ID)]
	
	elif item == 'stone_pickaxe':
		if state.made_stone_pickaxe[ID] is True:
			return False
		else:
			state.made_stone_pickaxe[ID] = True
		return [('produce_stone_pickaxe', ID)]
	elif item == 'stone_axe':
		if state.made_stone_axe[ID] is True:
			return False
		else:
			state.made_stone_axe[ID] = True
		return [('produce_stone_axe', ID)]
	
	elif item == 'iron_pickaxe':
		if state.made_iron_pickaxe[ID] is True:
			return False
		else:
			state.made_iron_pickaxe[ID] = True
		return [('produce_iron_pickaxe', ID)]
	elif item == 'iron_axe':
		if state.made_iron_axe[ID] is True:
			return False
		else:
			state.made_iron_axe[ID] = True
		return [('produce_iron_axe', ID)]
	
	elif item == 'wooden_pickaxe':
		if state.made_wooden_pickaxe[ID] is True:
			return False
		else:
			state.made_wooden_pickaxe[ID] = True
		return [('produce_wooden_pickaxe', ID)]
	elif item == 'wooden_axe':
		# this check to make sure we're not making multiple axes
		if state.made_wooden_axe[ID] is True:
			return False
		else:
			state.made_wooden_axe[ID] = True
		return [('produce_wooden_axe', ID)]
	else:
		return False

pyhop.declare_methods ('have_enough', check_enough, produce_enough)
pyhop.declare_methods ('produce', produce)

'''begin recipe methods'''

def punch_for_wood (state, ID):
	return [('op_punch_for_wood', ID)]

def craft_plank (state, ID):
	return [('have_enough', ID, 'wood', 1), ('op_craft_plank', ID)]
def craft_bench (state, ID):
	return [('have_enough', ID, 'plank', 4), ('op_craft_bench', ID)]
def craft_stick (state, ID):
	return [('have_enough', ID, 'plank', 2), ('op_craft_stick', ID)]
def craft_cart_at_bench (state, ID):
	return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'ingot', 5), ('op_craft_cart_at_bench', ID)]
def craft_rail_at_bench (state, ID):
	return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'ingot', 6), ('have_enough', ID, 'stick', 2), ('op_craft_rail_at_bench', ID)]

def craft_furnace_at_bench (state, ID):
	return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'cobble', 8), ('op_craft_furnace_at_bench', ID)]
def smelt_ore_at_furnace (state, ID):
	return [('have_enough', ID, 'furnace', 1), ('have_enough', ID, 'coal', 1), ('have_enough', ID, 'ore', 1), ('op_smelt_ore_at_furnace', ID)]

def craft_wooden_axe_at_bench (state, ID):
	return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'stick', 2), ('have_enough', ID, 'plank', 3), ('op_craft_wooden_axe_at_bench', ID)]
def craft_wooden_pickaxe_at_bench (state, ID):
	return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'stick', 2), ('have_enough', ID, 'plank', 3), ('op_craft_wooden_pickaxe_at_bench', ID)]
def craft_stone_axe_at_bench (state, ID):
	return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'stick', 2), ('have_enough', ID, 'cobble', 3), ('op_craft_stone_axe_at_bench', ID)]
def craft_stone_pickaxe_at_bench (state, ID):
	return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'stick', 2), ('have_enough', ID, 'cobble', 3), ('op_craft_stone_pickaxe_at_bench', ID)]
def craft_iron_axe_at_bench (state, ID):
	return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'stick', 2), ('have_enough', ID, 'ingot', 3), ('op_craft_iron_axe_at_bench', ID)]
def craft_iron_pickaxe_at_bench (state, ID):
	return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'stick', 2), ('have_enough', ID, 'ingot', 3), ('op_craft_iron_pickaxe_at_bench', ID)]


def mine_with_wood_for_cobble (state, ID):
	return[('have_enough', ID, 'wooden_pickaxe', 1), ('op_mine_with_wood_for_cobble', ID)]
def mine_with_wood_for_coal (state, ID):
	return[('have_enough', ID, 'wooden_pickaxe', 1), ('op_mine_with_wood_for_coal', ID)]
def mine_with_wood_for_wood (state, ID):
	return[('have_enough', ID, 'wooden_axe', 1), ('op_mine_with_wood_for_wood', ID)]

def mine_with_stone_for_cobble (state, ID):
	return[('have_enough', ID, 'stone_pickaxe', 1), ('op_mine_with_stone_for_cobble', ID)]
def mine_with_stone_for_coal (state, ID):
	return[('have_enough', ID, 'stone_pickaxe', 1), ('op_mine_with_stone_for_coal', ID)]
def mine_with_stone_for_ore (state, ID):
	return[('have_enough', ID, 'stone_pickaxe', 1), ('op_mine_with_stone_for_ore', ID)]
def mine_with_stone_for_wood (state, ID):
	return[('have_enough', ID, 'stone_axe', 1), ('op_mine_with_stone_for_wood', ID)]

def mine_with_iron_for_cobble (state, ID):
	return[('have_enough', ID, 'iron_pickaxe', 1), ('op_mine_with_iron_for_cobble', ID)]
def mine_with_iron_for_coal (state, ID):
	return[('have_enough', ID, 'iron_pickaxe', 1), ('op_mine_with_iron_for_coal', ID)]
def mine_with_iron_for_ore (state, ID):
	return[('have_enough', ID, 'iron_pickaxe', 1), ('op_mine_with_iron_for_ore', ID)]
def mine_with_iron_for_wood (state, ID):
	return[('have_enough', ID, 'iron_axe', 1), ('op_mine_with_iron_for_wood', ID)]
# your code here

#pyhop.declare_methods ('produce_wood', mine_with_iron_for_wood, mine_with_stone_for_wood, mine_with_wood_for_wood, punch_for_wood)
pyhop.declare_methods ('produce_wood', mine_with_wood_for_wood, punch_for_wood)

pyhop.declare_methods ('produce_cobble', mine_with_iron_for_cobble, mine_with_stone_for_cobble, mine_with_wood_for_cobble)

pyhop.declare_methods ('produce_coal', mine_with_iron_for_coal, mine_with_stone_for_coal, mine_with_wood_for_coal)

pyhop.declare_methods ('produce_ore', mine_with_iron_for_ore, mine_with_stone_for_ore)

pyhop.declare_methods ('produce_plank', craft_plank)
pyhop.declare_methods ('produce_bench', craft_bench)
pyhop.declare_methods ('produce_stick', craft_stick)
pyhop.declare_methods ('produce_cart', craft_cart_at_bench)
pyhop.declare_methods ('produce_rail', craft_rail_at_bench)

pyhop.declare_methods ('produce_furnace', craft_furnace_at_bench)
pyhop.declare_methods ('produce_ingot', smelt_ore_at_furnace)

pyhop.declare_methods ('produce_wooden_axe', craft_wooden_axe_at_bench)
pyhop.declare_methods ('produce_wooden_pickaxe', craft_wooden_pickaxe_at_bench)
pyhop.declare_methods ('produce_stone_axe', craft_stone_axe_at_bench)
pyhop.declare_methods ('produce_stone_pickaxe', craft_stone_pickaxe_at_bench)
pyhop.declare_methods ('produce_iron_axe', craft_iron_axe_at_bench)
pyhop.declare_methods ('produce_iron_pickaxe', craft_iron_pickaxe_at_bench)

"""
pyhop.declare_methods ('produce_wood_wood', mine_with_wood_for_wood)
pyhop.declare_methods ('produce_stone_wood', mine_with_stone_for_wood)
pyhop.declare_methods ('produce_iron_wood', mine_with_iron_for_wood)

pyhop.declare_methods ('produce_wood_cobble', mine_with_wood_for_cobble)
pyhop.declare_methods ('produce_stone_cobble', mine_with_stone_for_cobble)
pyhop.declare_methods ('produce_iron_cobble', mine_with_iron_for_cobble)

pyhop.declare_methods ('produce_wood_coal', mine_with_wood_for_coal)
pyhop.declare_methods ('produce_stone_coal', mine_with_stone_for_coal)
pyhop.declare_methods ('produce_iron_coal', mine_with_iron_for_coal)

pyhop.declare_methods ('produce_stone_ore', mine_with_stone_for_ore)
pyhop.declare_methods ('produce_iron_ore', mine_with_iron_for_ore)
"""
#This did not work
#How do we prooduce cobble, produce coal, produce ore for each tools?#

'''end recipe methods'''

# declare state
state = pyhop.State('state')
state.wood = {'agent': 0}
#state.time = {'agent': 4}
state.time = {'agent': 46}
state.wooden_axe = {'agent': 0}
state.made_wooden_axe = {'agent': False}
# your code here 
state.wooden_pickaxe = {'agent': 0}
state.made_wooden_pickaxe = {'agent': False}

state.stone_axe = {'agent': 0}
state.made_stone_axe = {'agent': False}
state.stone_pickaxe = {'agent': 0}
state.made_stone_pickaxe = {'agent': False}

state.iron_axe = {'agent': 0}
state.made_iron_axe = {'agent': False}
state.iron_pickaxe = {'agent': 0}
state.made_iron_pickaxe = {'agent': False}

state.plank = {'agent': 0}
state.stick = {'agent': 0}
state.cobble = {'agent': 0}
state.coal = {'agent': 0}
state.ore = {'agent': 0}
state.ingot = {'agent': 0}
state.cart = {'agent': 0}
state.rail = {'agent': 0}

state.bench = {'agent': 0}
state.made_bench = {'agent': False}
state.furnace = {'agent': 0}
state.made_furnace = {'agent': False}

# pyhop.print_operators()
# pyhop.print_methods()

#pyhop.pyhop(state, [('have_enough', 'agent', 'wood', 1)], verbose=3)
pyhop.pyhop(state, [('have_enough', 'agent', 'wood', 12)], verbose=3)