import sys
import math


def print_log(msg):
    print(msg, file=sys.stderr)


def dichotomy(current_pos, max_pos, min_pos):
    next_pos = max_pos + min_pos - current_pos
    if next_pos == current_pos:
        next_pos += 1
    if next_pos > max_pos:
        next_pos = max_pos
    if next_pos < min_pos:
        next_pos = min_pos
    return round(next_pos)


def update_dichotomy_result(last_pos, current_pos, max_pos, min_pos, bomb_dir):
    middle = (max_pos + min_pos) / 2
    if bomb_dir == "WARMER":
        if current_pos > last_pos:
            return math.ceil(middle), max_pos
        else:
            return min_pos, math.floor(middle)
    if bomb_dir == "COLDER":
        if current_pos > last_pos:
            return min_pos, math.floor(middle)
        else:
            return math.ceil(middle), max_pos


# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

xmin = 0
ymin = 0
xmax = w - 1
ymax = h - 1

ycurrent = y0
xcurrent = x0
looking_for_x = True
# game loop
while True:
    if xmin == xmax:
        looking_for_x = False

    bomb_dir = input()  # Current distance to the bomb compared to previous distance (COLDER, WARMER, SAME or UNKNOWN)

    if bomb_dir != "UNKNOWN":
        if looking_for_x:
            xmin, xmax = update_dichotomy_result(xlast, xcurrent, xmax, xmin, bomb_dir)
        else:
            ymin, ymax = update_dichotomy_result(ylast, ycurrent, ymax, ymin, bomb_dir)

    ylast = ycurrent
    xlast = xcurrent

    if looking_for_x:
        ycurrent = ylast
        xcurrent = dichotomy(xlast, xmax, xmin)
    else:
        xcurrent = xmin
        ycurrent = dichotomy(ylast, ymax, ymin)

    print("{} {}".format(xcurrent, ycurrent))
