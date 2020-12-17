# Advent of Code 2020
# --- Day 8: Handheld Halting ---

def part1(entries):

    accumulator = 0
    pos = 0
    poslist = []

    doAccumulate = True
    while doAccumulate:
        line = entries[pos].split()
        action = line[0]
        sign = line[1][0]
        val = int(line[1][1:])

        if pos not in poslist:
            poslist.append(pos)
            if action == 'acc':
                if sign == '+':
                    accumulator += val
                else:
                    accumulator -= val
                pos += 1
            elif action == 'jmp':
                if sign == '+':
                    pos += val
                else:
                    pos -= val
            elif action == 'nop':
                pos += 1
        else:
            print('infinite loop!')
            doAccumulate = False
            return accumulator


def runProgram(newEntries):

    maxlines = len(newEntries)

    accumulator = 0
    pos = 0
    poslist = []
    i = 0

    doAccumulate = True

    while doAccumulate:
        line = newEntries[pos].split()
        action = line[0]
        sign = line[1][0]
        val = int(line[1][1:])

        if pos not in poslist:
            poslist.append(pos)
            if action == 'acc':
                if sign == '+':
                    accumulator += val
                else:
                    accumulator -= val
                pos += 1

            elif action == 'jmp':
                if sign == '+':
                    pos += val
                else:
                    pos -= val
            elif action == 'nop':
                pos += 1
            # print(pos)

            if pos == maxlines:
                # print('success')
                doAccumulate = False
                return accumulator
            else:
                continue
        else:
            doAccumulate = False
            return -999


def part2(entries):

    a = -999

    for i, entry in enumerate(entries):
        line = entry.split()
        action = line[0]
        newEntries = []
        newEntries = entries.copy()

        if action == 'jmp':
            newEntries[i] = entries[i].replace('jmp', 'nop')
        elif action == 'nop':
            newEntries[i] = entries[i].replace('nop', 'jmp')

        a = runProgram(newEntries)
        del newEntries

        if a == -999:
            continue
        else:
            return a    


entries = [entry.strip('\n') for entry in open("input.txt", "r").readlines()]

print('Part 1: Acc value before loop = {}'.format(part1(entries)))
print('Part 2: Acc at successful completion = {}'.format(part2(entries)))
