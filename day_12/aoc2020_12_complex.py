# Advent of Code 2020
# --- Day 12: Rain Risk ---


def part1(instructions):

    pos = 0 + 0j  #[N(-S), E(-W)]
    dirfacing = directions['E']

    for inst in instructions:
        action = inst[0]
        value = int(inst[1:])

        if action == 'R':
            dirfacing *= 1j ** (-value//90)
        elif action == 'L':
            dirfacing *= 1j ** (value//90)
        elif action == 'F':
            pos += dirfacing * value
        else:
            pos += directions[action] * value
            

    print('final position: {}'.format(pos))
    mhdist = int(abs(pos.real) + abs(pos.imag))
    return mhdist


def part2(instructions):

    pos = 0 + 0j
    waypos = 10 + 1j
    dirfacing = directions['E']

    for inst in instructions:
        action = inst[0]
        value = int(inst[1:])

        if action == 'R':
            waypos *= 1j ** (-value//90)
        elif action == 'L':
            waypos *= 1j ** (value//90)
        elif action == 'F':
            pos += waypos * value
        else:
            waypos += directions[action] * value
            

    print('final position: {}'.format(pos))
    mhdist = int(abs(pos.real) + abs(pos.imag))
    return mhdist

instructions = [line.strip('\n') for line in open("input.txt", "r").readlines()]

directions = {
    'N': 0 + 1j,
    'E': 1 + 0j,
    'S': 0 - 1j,
    'W': -1 +0j
    }

print('Part 1: manhattan distance to destination = {}'.format(part1(instructions)))
print('Part 2: manhattan distance to waypoint destination = {}'.format(part2(instructions)))