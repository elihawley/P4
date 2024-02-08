Heuristics:
- Already reached goal, so finish (includes trivial case: where we start with the goal items).
- No time left, so finish.
- If a tool has already been made, don't make more of it.
- Don't produce more of an item if you already have enough for the current task. (Special case: Coal and ore depend on how many ingots we need)
- Skip making an unneeded axe if we have one with the same speed (stone_axe, iron_axe)
- Building axes from scratch usually not worth it unless we have a lot of time or need them for goal.
- Don't bother making or using a pickaxe if we have a better one