# Advent of Code 2020
# --- Day 15: Rambunctious Recitation ---

import re

def part1(nums):

    turns = len(nums)

    while turns < 2020:

        lastval = nums[-1]

        if nums.count(lastval) == 1:
            nums.append(0)
        else:
            nums.reverse()
            r = nums[1:].index(lastval) + 1
            nums.reverse()
            nums.append(r)

        turns += 1

    return nums[-1]


def part2(nums):
    # will need something more robust than part1 since iterating 30mil times takes enormously long
    # using a (long) list to store prev seen turns

    total_turns = 30000000
    last_seen = [0] * total_turns

    prevval = nums[-1]

    for turn, n in enumerate(nums[:-1], 1):  # counting from 1
        last_seen[n] = turn

    for prev_turn in range(len(nums), total_turns):
        current = prev_turn - last_seen[prevval]
        # using the fact that last_seen is initialised to 0
        if current == prev_turn:
            current = 0

        last_seen[prevval] = prev_turn
        prevval = current

    return current


# we can also generalise by feeding in n_turns as a paramater

def play(nums, n_turns):
    last_seen = [0] * n_turns

    prevval = nums[-1]

    for turn, n in enumerate(nums[:-1], 1):  # counting from 1
        last_seen[n] = turn

    for prev_turn in range(len(nums), n_turns):
        current = prev_turn - last_seen[prevval]
        # using the fact that last_seen is initialised to 0
        if current == prev_turn:
            current = 0

        last_seen[prevval] = prev_turn
        prevval = current

    return current



nums = [14,8,16,0,1,17]
# nums = [3,1,2]

print('Part 1: result = {}'.format(play(nums, 2020)))
print('Part 2: result = {}'.format(play(nums, 30000000)))
