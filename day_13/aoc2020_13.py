# Advent of Code 2020
# --- Day 13: Shuttle Search ---
# Chinese Remainder solution, especially, from here: https://github.com/mebeim/aoc/blob/master/2020/README.md

import math


def part1():

    with open('input.txt') as f:
        arrival = int(f.readline())
        departures = [int(num) for num in f.readline().split(',') if num != 'x']

    best = math.inf
    busid = -999

    for d in departures:
        n = arrival // d + (arrival % d != 0)
        wait = (d * n) - arrival

        if wait < best:
            best = wait
            busid = d

    print(d)
    print(best)

    return busid * best


from math import gcd
from itertools import count

# find the least common multiple
def lcm(a, b):
    return a * b // gcd(a, b)

def part2simple():

    with open('input.txt') as f:
        arrival = f.readline()
        departures = [d for d in f.readline().strip('\n').split(',')]

    buses = []
    for i, v in filter(lambda iv: iv[1] != 'x', enumerate(departures)):
        buses.append((i, int(v)))

    t, step = buses[0]
    for delta, period in buses[1:]:
        for t in count(t, step):
            if (t + delta) % period == 0:
                break

        step = lcm(step, period)

    return t


# using the chinese remainder theorem
def chinese_remainder_theorem(equations):
    # equations = [(a1, p1), (a2, p2), ...]
    t = 0
    P = 1

    # for _, pi in equations:
    #     P *= pi
    #     # as in p_subscript_i, not pi = 3.1459...

    # or get P using using itemgetter
    P = prod(map(itemgetter(1), equations))

    for ai, pi in equations:
        ni = P // pi
        inv = pow(ni, -1, mod=pi)  # modular inverse
        t = (t + ai * ni * inv) % P

    return t

from math import prod
from operator import itemgetter

def part2crt():

    with open('input.txt') as f:
        arrival = f.readline()
        departures = [d for d in f.readline().strip('\n').split(',')]

    buses = []
    for i, v in filter(lambda iv: iv[1] != 'x', enumerate(departures)):
        buses.append((-i, int(v)))

    time = chinese_remainder_theorem(buses)

    return time


print('Part 1: result = {}'.format(part1()))
print('Part 2: result = {}'.format(part2simple()))
print('Part 2 CRT: result = {}'.format(part2crt()))