# Advent of Code 2020
# --- Day 2: Password Philosophy ---

import parse

# 8-9 x: xxxxxxxrk
pw_matcher = '''{min:d}-{max:d} {letter}: {password}\n'''


def part1(lines):

    valid = 0

    for line in lines:
        r = parse.parse(pw_matcher, line)
        lmin = r['min']
        lmax = r['max']
        count = 0

        for l in r['password']:
            if l == r['letter']:
                count += 1

        if (count >= lmin) and (count <= lmax):
            valid += 1

    return valid


def part2(lines):

    valid = 0

    for line in lines:
        r = parse.parse(pw_matcher, line)
        pos1 = r['min']-1
        pos2 = r['max']-1
        l = r['letter']
        trail = r['password']

        count = 0

        if trail[pos1] == l:
            count += 1

        if trail[pos2] == l:
            count += 1

        if count == 1:
            valid += 1

    return valid


lines = [line for line in open("input.txt", "r").readlines()]
print('Part 1: valid passwords = {}'.format(part1(lines)))
print('Part 2: valid passwords = {}'.format(part2(lines)))