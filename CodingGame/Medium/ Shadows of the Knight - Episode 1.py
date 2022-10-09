import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = 4, 8
# n = int(input())  # maximum number of turns before game over.
x0, y0 = 2, 3

infx, supx = 0, w
infy, supy = 0, h

def update(infx, supx, infy, supy, dir, x, y):
    xchange = False
    if "U" in dir:
        supy = y
    elif "D" in dir:
        infy = y+1
    if "R" in dir:
        xchange = True
        infx = x+1
    elif "L" in dir:
        xchange = True
        supx = x
    
    if len(dir) == 1:
        if not xchange:
            infx = x
            supx = x+1
        else:
            infy = y
            supy = y+1
    return infx, supx, infy, supy

def best_place(infx, supx, infy, supy):
    x = (infx + supx) //2
    y = (infy + supy) //2
    return x, y


x, y = x0, y0
# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    infx, supx, infy, supy = update(infx, supx, infy, supy, bomb_dir, x, y)
    print(infx, supx, infy, supy)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    x, y = best_place(infx, supx, infy, supy)

    # the location of the next window Batman should jump to.
    print(f"{x} {y}")
