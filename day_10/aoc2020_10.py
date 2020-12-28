# Advent of Code 2020
# --- Day 10: Adapter Array ---
# part2 solution from: https://github.com/mebeim/aoc/blob/master/2020/solutions/day10.py
# and see for discussion: https://github.com/mebeim/aoc/blob/master/2020/README.md#day-10---adapter-array

def part1(nums):

    ones = 0
    threes = 0
    # for i in range(len(numlist)-1):
    #     diff = numlist[i+1] - numlist[i]

    # solution that uses zip
    for cur, nxt in zip(nums, nums[1:]):
        diff = nxt - cur

        if diff == 1:
            ones += 1
        elif diff == 3:
            threes += 1
        else:
            print('error')
            return -99999

    # print(ones)
    # print(threes)
    return ones * threes


def part2(nums):

    # start with i == 0 to get all possible solutions
    total = possible_solutions(0)

    return total


# dynamic programming technique to finish in a reasonable time.
from functools import lru_cache
@lru_cache()
def possible_solutions(i):
    if i == len(nums) - 1:
        return 1

    tot = 0
    for j in range(i + 1, min(i + 4, len(nums))):   # min() to avoid going past the end of the list
        if nums[j] - nums[i] <= 3:                  # difference <= 3 to enforce the rule
            tot += possible_solutions(j)

    return tot


nums = [int(entry.strip('\n')) for entry in open("input.txt", "r").readlines()]
nums = [0] + nums + [max(nums) + 3]
nums.sort()

print('Part 1: solution = {}'.format(part1(nums)))
print('Part 2: encryption weakness = {}'.format(part2(nums)))
print(possible_solutions.cache_info())