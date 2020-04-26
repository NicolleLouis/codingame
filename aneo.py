import sys
import math


######### utils #########
def print_log(msg):
    print(msg, file=sys.stderr)


def is_red(speed, distance, duration):
    return (18 * distance) % (10 * speed * duration) >= (5 * speed * duration)

######### utils #########

speed = int(input())

light_count = int(input())
lights = []
for i in range(light_count):
    distance, duration = [int(j) for j in input().split()]
    lights.append(
        {
            "distance": distance,
            "duration": duration
        }
    )

max_speed = 0
for potential_speed in range(speed):
    potential_speed += 1
    does_work = True
    for light in lights:
        does_work = does_work and not is_red(potential_speed, light["distance"], light["duration"])
    if does_work:
        max_speed = potential_speed

print(max_speed)
