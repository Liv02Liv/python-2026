#%%

#(Ghost Gobble Arcade Game)

"""Functions for implementing the rules of the classic arcade game Pac-Man."""

def eat_ghost(power_pellet_active, touching_ghost):
    return power_pellet_active and touching_ghost

print(eat_ghost(False, True))

def score(touching_power_pellet, touching_dot):
    return touching_power_pellet or touching_dot

print(score(True, True))

def lose(power_pellet_active, touching_ghost):
    return not power_pellet_active and touching_ghost

print(lose(False, True))

def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    return  has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)

print(win(False, True, False))