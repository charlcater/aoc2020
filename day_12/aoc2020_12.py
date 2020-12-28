# Advent of Code 2020
# --- Day 12: Rain Risk ---


def part1(instructions):

    pos = [0,0]  #[N(-S), E(-W)]
    facing = 0
    directions = ['E', 'S', 'W', 'N']
    dirfacing = 'E'

    for inst in instructions:
        action = inst[0]
        value = int(inst[1:])

        # moving only
        if action == 'N':
            pos[0] += value
        elif action == 'S':
            pos[0] -= value
        elif action == 'E':
            pos[1] += value
        elif action == 'W':
            pos[1] -= value

        # turn to face a direction
        if action == 'R':
            d = value // 90
            facing = (facing + d) % 4
            dirfacing = directions[facing]
        elif action == 'L':
            d = value // 90
            facing = (facing - d) % 4
            dirfacing = directions[facing]

        # move in facing direction
        if action == 'F':
            if dirfacing == 'N':
                pos[0] += value
            elif dirfacing == 'S':
                pos[0] -= value
            elif dirfacing == 'E':
                pos[1] += value
            elif dirfacing == 'W':
                pos[1] -= value
            

    print(pos)
    mhdist = abs(pos[0]) + abs(pos[1])
    return mhdist


def part2(instructions):

    pos = [0, 0]
    waypos = [10,1]

    for inst in instructions:
        action = inst[0]
        value = int(inst[1:])

        # moving only
        #  this is confusing, keep x on 'horisontal' (E-W) axis [0] and y on N-S axis [1]
        if action == 'N':
            waypos[1] += value
        elif action == 'S':
            waypos[1] -= value
        elif action == 'E':
            waypos[0] += value
        elif action == 'W':
            waypos[0] -= value

        # swop coords
        if action == 'R':
            d1 = waypos[1]
            d2 = -1*waypos[0]
            waypos = [d1, d2]
        elif action == 'L':
            d1 = -1*waypos[1]
            d2 = waypos[0]
            waypos = [d1, d2]


        # move in facing direction
        if action == 'F':
            pos[0] += waypos[0] * value
            pos[1] += waypos[1] * value
            

    print(pos)
    mhdist = abs(pos[0]) + abs(pos[1])
    return mhdist

instructions = [line.strip('\n') for line in open("input.txt", "r").readlines()]

print('Part 1: manhattan distance to destination = {}'.format(part1(instructions)))
print('Part 2: manhattan distance to waypoint destination = {}'.format(part2(instructions)))