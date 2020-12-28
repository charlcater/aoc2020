# Advent of Code 2020
# --- Day 11: Seating System ---

from copy import deepcopy

def part1(seats):

    iteration = 0
    while 1:
        # prev = seats.copy()
        prev = deepcopy(seats)
        iteration += 1

        for r, row in enumerate(prev):
            for s, seat in enumerate(row):
                if seat == '.':
                    continue

                occ = occ_neighbours(prev, r, s)

                # do evolution
                if seat == 'L' and occ == 0:
                    seats[r][s] = '#'
                elif seat == '#' and occ >= 4:
                    seats[r][s] = 'L'

        if seats == prev:
            print(iteration)
            return sum(row.count('#') for row in seats)

        prev = seats


def occ_neighbours(seats, row, col):

    deltas = (
        (-1, 0), ( 1,  0), (0, 1), ( 0, -1),
        (-1, 1), (-1, -1), (1, 1), ( 1, -1)
    )

    total = 0
    for dr, dc in deltas:
        rr, cc = row + dr, col + dc
        if 0 <= rr <= rows and 0 <= cc <= cols:
            total += seats[rr][cc] == '#'

    return total 



def part2(nums):

    return -999



seats = [list(line.strip('\n')) for line in open("input.txt", "r").readlines()]
rows = len(seats) - 1
cols = len(seats[0]) - 1
print(seats[0][5])

print('Part 1: occupied seats = {}'.format(part1(seats)))
# print('Part 2: encryption weakness = {}'.format(part2(nums)))