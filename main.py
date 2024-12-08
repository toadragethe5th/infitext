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

    room_title = "You entered a " + size + " " + descriptor + " " + room + "."
