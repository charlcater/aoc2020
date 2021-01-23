# Advent of Code 2020
# --- Day 17: Conway Cubes ---

import numpy as np
from copy import deepcopy
from itertools import product

# six cycles, so at most we'll have a 8+12, 8+12 1+12 cube at the end

def doBoot3D(grid):

    itteration = 0
    while itteration < 6:
        print('itteration {}'.format(itteration))
        prev = deepcopy(grid)
        itteration += 1

        for x, xcol in enumerate(prev):
            for y, ycol in enumerate(xcol):
                for z, cube in enumerate(ycol):

                    # # check if active
                    # if cube == '#':
                    #     print('{}, {}, {} == active'.format(x, y, z)) 

                    # check the neighbours of every cube
                    active = check_neighbours3D(prev, x, y, z)

                    if cube == '#':
                        if active == 2 or active == 3:
                            pass
                        else:
                            grid[x][y][z] = '.'
                    elif cube == '.' and active == 3:
                        grid[x][y][z] = '#'

        prev = grid

    return grid


def check_neighbours3D(grid, x, y, z):

    deltas = list(product([-1, 0, 1], repeat=3))
    deltas.remove((0,0,0))

    total = 0

    for dx, dy, dz in deltas:
        xx, yy, zz = x + dx, y + dy, z + dz

        if 0 <= xx <= xdim-1 and 0 <= yy <= ydim-1 and 0 <= zz <= zdim-1:
            total += grid[xx][yy][zz] == '#'

    return total


def check_neighbours4D(grid, x, y, z, w):

    deltas = list(product([-1, 0, 1], repeat=4))
    deltas.remove((0,0,0,0))

    total = 0

    for dx, dy, dz, dw in deltas:
        xx, yy, zz, ww = x + dx, y + dy, z + dz, w + dw

        if 0 <= xx <= xdim-1 and 0 <= yy <= ydim-1 and 0 <= zz <= zdim-1 and 0 <= ww <= wdim-1:
            total += grid[xx][yy][zz][ww] == '#'

    return total


def doBoot4D(grid):

    itteration = 0
    while itteration < 6:
        print('itteration {}'.format(itteration))
        prev = deepcopy(grid)
        itteration += 1

        for x, xcol in enumerate(prev):
            for y, ycol in enumerate(xcol):
                for z, zcol in enumerate(ycol):
                    for w, hcube in enumerate(zcol):

                        # check the neighbours of every hypercube
                        active = check_neighbours4D(prev, x, y, z, w)

                        if hcube == '#':
                            if active == 2 or active == 3:
                                pass
                            else:
                                grid[x][y][z][w] = '.'
                        elif hcube == '.' and active == 3:
                            grid[x][y][z][w] = '#'

        prev = grid

    return grid


def setup3D(input):

    grid = np.array(['.'] * xdim * ydim * zdim)
    grid = grid.reshape(xdim, ydim, zdim)
    # print(empty.shape)

    # shift input up by 6 to center in grid
    for i, line in enumerate(input):
        for j, l in enumerate(line):
            grid[i+6, j+6, 6] = l

    return grid


def setup4D(input):

    grid = np.array(['.'] * xdim * ydim * zdim * wdim)
    grid = grid.reshape(xdim, ydim, zdim, wdim)
    # print(empty.shape)

    # shift input up by 6 to center in grid
    for i, line in enumerate(input):
        for j, l in enumerate(line):
            grid[i+6, j+6, 6, 6] = l

    # check that input is correct
    # print(grid[:,:,6,6])

    return grid


def count_active(grid):
    return np.sum(np.array(grid == '#'))

input = [list(line.strip('\n')) for line in open("input.txt", "r").readlines()]

xdim = 20
ydim = 20
zdim = 13
wdim = 13

pt1_fingrid = doBoot3D(setup3D(input))
print('Part 1: active cubes = {}'.format(count_active(pt1_fingrid)))

pt2_fingrid = doBoot4D(setup4D(input))
print('Part 2: active cubes = {}'.format(count_active(pt2_fingrid)))