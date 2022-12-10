import numpy as np
from simulation_engine import *

sim = Simulation()

n = 15
l = 200
a = 10
b = 50
c = 20
d = 5
e = 80
f = 40

SOUTH_RIGHT = (a, b)
SOUTH_LEFT = (-a, b)
NORTH_RIGHT = (-a, -b)
NORTH_LEFT = (a, -b)

SOUTH_RIGHT_START = (a, l+b)
SOUTH_LEFT_START = (-a, l+b)
NORTH_RIGHT_START = (-a, -l-b)
NORTH_LEFT_START = (a, -l-b)

SOUTH_MIDDLE = (0, b-c)
NORTH_MIDDLE = (0, -b+c)

SOUTH_RIGHT_IN = (d, b-c+d)
SOUTH_RIGHT_OUT = (-d, b-c-d)
SOUTH_RIGHT_MIDDLE = (-a, b-2*c)
NORTH_RIGHT_MIDDLE = (-a, -b+2*c)
NORTH_RIGHT_OUT = (-d, -b+c+d)
NORTH_RIGHT_IN = (d, -b+c-d)

SOUTH_LEFT_IN = (-d, b-c+d)
SOUTH_LEFT_OUT = (d, b-c-d)
SOUTH_LEFT_MIDDLE = (a, b-2*c)
NORTH_LEFT_MIDDLE = (a, -b+2*c)
NORTH_LEFT_OUT = (d, -b+c+d)
NORTH_LEFT_IN = (-d, -b+c-d)

SOUTH_RIGHT_TURN = (f, b-c-c/2)
SOUTH_RIGHT_MERGE = (e, 5)

SOUTH_LEFT_TURN = (-f, b-c-c/2)
SOUTH_LEFT_MERGE = (-e, 5)

NORTH_RIGHT_TURN = (f, -b+c+c/2)
NORTH_RIGHT_MERGE = (e, -5)

NORTH_LEFT_TURN = (-f, -b+c+c/2)
NORTH_LEFT_MERGE = (-e, -5)

sim.create_roads([
    ((-l, 2), (l, 2)),
    ((-l, 5), (-e, 5)),
    ((-e, 5), (e, 5)),
    ((e, 5), (l, 5)),

    ((l, -2), (-l, -2)),
    ((l, -5), (e, -5)),
    ((e, -5), (-e, -5)),
    ((-e, -5), (-l, -5)),

    (SOUTH_RIGHT_START, SOUTH_RIGHT),
    (SOUTH_LEFT, SOUTH_LEFT_START),
    (NORTH_RIGHT_START, NORTH_RIGHT),
    (NORTH_LEFT, NORTH_LEFT_START),

    (SOUTH_RIGHT_IN, SOUTH_MIDDLE),
    (SOUTH_MIDDLE, SOUTH_RIGHT_OUT),
    
    (NORTH_RIGHT_OUT, NORTH_MIDDLE),
    (NORTH_MIDDLE, NORTH_RIGHT_IN),

    (SOUTH_RIGHT_MIDDLE, NORTH_RIGHT_MIDDLE),

    (NORTH_LEFT_IN, NORTH_MIDDLE),
    (NORTH_MIDDLE, NORTH_LEFT_OUT),

    (SOUTH_MIDDLE, SOUTH_LEFT_IN),
    (SOUTH_LEFT_OUT, SOUTH_MIDDLE),

    (NORTH_LEFT_MIDDLE, SOUTH_LEFT_MIDDLE),

    (SOUTH_RIGHT_TURN, SOUTH_RIGHT_MERGE),
    (SOUTH_LEFT_MERGE, SOUTH_LEFT_TURN),

    (NORTH_RIGHT_MERGE, NORTH_RIGHT_TURN),
    (NORTH_LEFT_TURN, NORTH_LEFT_MERGE),

    *curve_road(SOUTH_RIGHT, SOUTH_RIGHT_IN, (a, b-c/2), resolution=n),
    *curve_road(SOUTH_RIGHT_OUT, SOUTH_RIGHT_MIDDLE, (-a, b-c-c/2), resolution=n),
    *curve_road(NORTH_RIGHT_MIDDLE, NORTH_RIGHT_OUT, (-a, -b+c+c/2), resolution=n),
    *curve_road(NORTH_RIGHT_IN, NORTH_LEFT, (a, -b+c/2), resolution=n),

    *curve_road(SOUTH_RIGHT, SOUTH_RIGHT_TURN, (SOUTH_RIGHT[0], SOUTH_MIDDLE[1]), resolution=n),
    *curve_road(SOUTH_LEFT_MIDDLE, SOUTH_RIGHT_TURN, (SOUTH_RIGHT[0], SOUTH_MIDDLE[1]), resolution=n),

    *curve_road(NORTH_RIGHT_TURN, NORTH_LEFT, (NORTH_LEFT[0], NORTH_MIDDLE[1]), resolution=n),
    *curve_road(NORTH_RIGHT_TURN, NORTH_LEFT_MIDDLE, (NORTH_LEFT[0], NORTH_MIDDLE[1]), resolution=n),

    *curve_road(SOUTH_LEFT_IN, SOUTH_LEFT, (-a, b-c/2), resolution=n),
    *curve_road(SOUTH_LEFT_MIDDLE, SOUTH_LEFT_OUT, (a, b-c-c/2), resolution=n),
    *curve_road(NORTH_LEFT_OUT, NORTH_LEFT_MIDDLE, (a, -b+c+c/2), resolution=n),
    *curve_road(NORTH_RIGHT, NORTH_LEFT_IN, (-a, -b+c/2), resolution=n),
    
    *curve_road(SOUTH_LEFT_TURN, SOUTH_LEFT, (SOUTH_LEFT[0], SOUTH_MIDDLE[1]), resolution=n),
    *curve_road(SOUTH_LEFT_TURN, SOUTH_RIGHT_MIDDLE, (SOUTH_LEFT[0], SOUTH_MIDDLE[1]), resolution=n),
    
    *curve_road(NORTH_RIGHT, NORTH_LEFT_TURN, (NORTH_RIGHT[0], NORTH_MIDDLE[1]), resolution=n),
    *curve_road(NORTH_RIGHT_MIDDLE, NORTH_LEFT_TURN, (NORTH_RIGHT[0], NORTH_MIDDLE[1]), resolution=n),
])

def road(a): return range(a, a+n)

sim.create_gen({
    'vehicle_rate': 90,
    'vehicles': [
        [15, {'path': [0]}], #cars at constant rate on middle highway top lane of left to right
        [15, {'path': [4]}], #cars at constant rate on middle highway bottom lane of right to left
        [3, {'path': [1, 2, 3]}], #cars at constant rate on middle highway bottom lane of left to right
        [3, {'path': [5, 6, 7]}], #cars at constant rate on middle highway top lane of right to left

        [5, {'path': [1, 23, *road(26+12*n), 9]}], #come from bottom lane of L2R, take the exit, hang right to exit bottom
        [3, {'path': [1, 23, *road(26+13*n), 16, *road(26+2*n), 14, 15, *road(26+3*n), 11]}],  #come from bottom lane of L2R, take the exit, hang left to exit top left
        [1, {'path': [1, 23, *road(26+13*n), 16, *road(26+15*n), 25, 7]}], #come from bottom lane of L2R, take the exit, hang right to merge back on highway

        [2, {'path': [8, *road(26+4*n), 22, 3]}], #come from bottom right, merge on to highway
        [4, {'path': [8, *road(26), 12, 13, *road(26+n), 16, *road(26+2*n), 14, 15, *road(26+3*n), 11]}], #come from bottom right, hang left then right to exit top right
        [2, {'path': [8, *road(26), 12, 13, *road(26+n), 16, *road(26+15*n), 25, 7]}], #come from bottom right, hang left then left to merge on to highway

        [5, {'path': [5, 24, *road(26+6*n), 11]}], #come from top lane of R2L, take the exit, hang right to exit top
        [3, {'path': [5, 24, *road(26+7*n), 21, *road(26+9*n), 20, 19, *road(26+8*n), 9]}], #come from top lane of R2L, take the exit, hang left to exit bottom left
        [1, {'path': [5, 24, *road(26+7*n), 21, *road(26+5*n), 22, 3]}], #come from top lane of R2L, take the exit, hang left to merge back on highway in opposite direction

        [2, {'path': [10, *road(26+14*n), 25, 7]}], #come from top left, immediately merge onto highway
        [4, {'path': [10, *road(26+11*n), 17, 18, *road(26+10*n), 21, *road(26+9*n), 20, 19, *road(26+8*n), 9]}], #come from top left, hang left to exit bottom left
        [2, {'path': [10, *road(26+11*n), 17, 18, *road(26+10*n), 21, *road(26+5*n), 22, 3]}], #come from top left, hang left then merge on to highway
    ]
})

# Start Simulation
win = Window(sim)
win.zoom = 6
win.run(steps_per_update=5)
