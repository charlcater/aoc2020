# Advent of Code 2020
# --- Day 14: Docking Data ---

import re

def part1(lines):

    table = str.maketrans('1X', '01')
    mem = {}

    # first do bitwise AND to create a 'real' mask
    # this sets which values are 'allowed' through / unaffected
    # then do bitwise OR to set out value

    # eg, if
    # mask       = X11XXX0X, then
    # mask_clear = 10011101  and
    # set mask   = 01100000

    # value = 42 = 00101010 &
    # clear mask = 10011101 =
    # masked val = 00001000

    # masked val = 00001000 +
    # set mask   = 01100000 =
    # final val  = 01101000 --> write to mem

    for line in lines:
        if line.startswith('mask'):
            mask = line[7:]
            mask_clear = int(mask.translate(table), 2)
            mask_set = int(mask.replace('X', '0'), 2)
        else:
            addr, value = map(int, rexp.findall(line)[0])
            mem[addr] = (value & mask_clear) | mask_set

    total = sum(mem.values())
    return total

def part2(lines):
    # now decode the memory address, leave values intact

    mem2 = {}

    for line in lines:
        if line.startswith('mask'):
            mask = line[7:]
        else:
            addr, value = map(int, rexp.findall(line)[0])

            addr = '{:036b}'.format(addr)
            for a in all_addrs(addr, mask):
                mem2[a] = value

    total2 = sum(mem2.values())
    return total2


from itertools import product

def all_addrs(addr, mask):
    args = []

    for addr_bit, mask_bit in zip(addr, mask):
        if mask_bit == '0':
            args.append(addr_bit)
        elif mask_bit == '1':
            args.append('1')
        else:
            args.append('01')

    for a in product(*args):
        yield int(''.join(a), 2)


# alternative to using itertools
def all_addrs_alt(addr, mask=None):
    if mask is not None:
        addr = ''.join(a if m == '0' else m for a, m in zip(addr, mask))

    if 'X' in addr:
        yield from all_addrs(addr.replace('X', '0', 1))
        yield from all_addrs(addr.replace('X', '1', 1))
    else:
        yield int(addr, 2)

# list(all_addrs('100', '1XX')) -> [0b100, 0b101, 0b110, 0b111] == [4, 5, 6, 7]


rexp = re.compile(r'mem\[(\d+)\] = (\d+)')
lines = [line.strip() for line in open("input.txt", "r").readlines()]

print('Part 1: result = {}'.format(part1(lines)))
print('Part 2: result = {}'.format(part2(lines)))
