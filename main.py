import random
import math
from vars import *

# https://www.w3schools.com/python/ref_func_any.asp
# HOLY CRAP


def generate_room(keyroom_found):
    roomspecs = []
    size = random.choice(room_sizes)
    if (keyroom_found):
        room = rooms[random.randint(0, len(rooms))]
    else:
        room = rooms[random.randint(0, len(rooms)-1)]

    descriptor = random.choice(room_descriptors)
    
    r = random.randint(1,10)
    
    roomspecs.append(size)
    roomspecs.append(descriptor)
    roomspecs.append(room_title)
    roomspecs.append(attr)
    
    """
    if (size == "small"):
    	loot_size = 1
    elif (size == "medium"):
    	loot_size = 2
    elif (size == "large"):
    	loot_size = 3
    else:
    	loot_size = 4
    """
    return roomspecs

def main():
	running = True # Pygame style loop
	coords = (0,0)
	try:
		file = open("gamesave")

	while (running):
		directive = input("Enter what you want to do (or HELP): ")
		directive = directive.lower()
		if directive == "help":
			print("""north - move north
				 south - move south
				 east  - move east
				 west  - move west
				 attack - attack an enemy
				 scavenge - scavenge for stuff
				 list - list inventory
				 equip - equip an item
				 exit  - leave (why would you do this?)
				 loadpath - Changes where the game is saved and the filename.
				 The game autosaves on exit.

				 """
		elif directive == "north":
			coords[1] += 1
			loadRoom(roomDict, 
