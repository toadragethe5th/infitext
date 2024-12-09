import random
import math
from vars import *


def generate_room(keyroom_found):
    roomspecs = []
    size = random.choice(room_sizes)
    if (keyroom_found):
        room = rooms[random.randint(0, len(rooms))]
    else:
        room = rooms[random.randint(0, len(rooms)-1)]

    descriptor = random.choice(room_descriptors)
    
    r = random.randint(1,10)

    if (r >= 7):
    	attr = "This room has a monster!"
    room_title = "You entered a " + size + " " + descriptor +  " " + room + ".\n" + attr 
    roomspecs.append(room_title)
    
    if (size == "small"):
    	loot_size = 1
    elif (size == "medium"):
    	loot_size = 2
    elif (size == "large"):
    	loot_size = 3
    else:
    	loot_size = 4
	
    for i in range(loot_size):
    	
