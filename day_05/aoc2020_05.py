# Advent of Code 2020
# --- Day 5: Binary Boarding ---

import numpy as np

def part1(lines):

    # rows 0-127
    # seats 0-7

    seatIDs = []

    for line in lines:

        rows = np.arange(128)
        rowbin = line[0:7]

        for r in rowbin:
            if r == 'F':
                rows = rows[0:int(len(rows)/2)]
            elif r == 'B':
                rows = rows[int(len(rows)/2):len(rows)]

        # print(rows)

        cols = np.arange(8)
        colbin = line[7:]

        for c in colbin:
            if c == 'L':
                cols = cols[0:int(len(cols)/2)]
            elif c == 'R':
                cols = cols[int(len(cols)/2):len(cols)]

        seatID = rows[0]*8 + cols[0]

        seatIDs.append(seatID)

    highID = max(seatIDs)

    return highID
    
def part2(lines):

    mySeat = 0
    allseatIDs = []
    seatIDs = []

    for i in range(128):
        for j in range(8):
            id = i*8 + j
            allseatIDs.append(id)

    for line in lines:

        rows = np.arange(128)
        rowbin = line[0:7]

        for r in rowbin:
            if r == 'F':
                rows = rows[0:int(len(rows)/2)]
            elif r == 'B':
                rows = rows[int(len(rows)/2):len(rows)]

        # print(rows)

        cols = np.arange(8)
        colbin = line[7:]

        for c in colbin:
            if c == 'L':
                cols = cols[0:int(len(cols)/2)]
            elif c == 'R':
                cols = cols[int(len(cols)/2):len(cols)]

        seatID = rows[0]*8 + cols[0]

        seatIDs.append(seatID)

    for seat in allseatIDs:
        if seat not in seatIDs and (seat-1 in seatIDs and seat+1 in seatIDs):
            # print('my seat: {}'.format(seat))
            mySeat = seat  

    return mySeat

lines = [line.strip('\n') for line in open("input.txt", "r").readlines()]
print('Part 1: highest seat ID = {}'.format(part1(lines)))
print('Part 2: my seatID = {}'.format(part2(lines)))
