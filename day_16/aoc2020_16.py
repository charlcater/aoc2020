# Advent of Code 2020
# --- Day 16: Ticket Translation ---

# method 1 is my attempt
# method 2 from https://github.com/mebeim/aoc/blob/master/2020/README.md

import re
from math import prod


class DoubeRange:
    __slots__ = ('field', 'a', 'b', 'c', 'd')

    def __init__(self, field, a, b, c, d):
        self.field, self.a, self.b, self.c, self.d = field, a, b, c, d

    def __contains__(self, value):
        return self.a <= value <= self.b or self.c <= value <= self.d


def parse_input(fin):
    ranges = []
    rexp = re.compile(r'([a-z ]*): (\d+)-(\d+) or (\d+)-(\d+)')

    for line in map(str.rstrip, fin):
        if not line:
            break

        f, a, b, c, d = rexp.findall(line)[0]
        aint, bint, cint, dint = map(int, [a, b, c, d])
        ranges.append(DoubeRange(f, aint, bint, cint, dint))

    fin.readline()
    my_ticket = tuple(map(int, fin.readline().split(',')))
    fin.readline()
    fin.readline()

    tickets = []
    for line in fin:
        tickets.append(tuple(map(int, line.split(','))))

    tickets.append(my_ticket)

    return ranges, my_ticket, tickets


def clean_tickets(ticket):
    return all(any(v in r for r in ranges[1:]) for v in ticket)


def invalid_entries(ticket):
    for value in ticket:
        if all(value not in rng for rng in ranges[1:]):
            yield value


def part1(tickets):
    total = sum(map(sum, map(invalid_entries, tickets)))
    return total


def simplify(possible):
    assigned = [None] * len(possible)

    while any(possible):
        for i, poss in enumerate(possible):
            if len(poss) == 1:
                assigned[i] = match = poss.pop()
                # print(assigned[i])
                break

        for other in possible:
            if match in other:
                other.remove(match)

    return assigned


# possible is a list of lists _in order of the vals as they appear on the ticket_ we get a list of possible fields it may belong to
# pos 0  => ['departure location', 'departure station', 'departure track', 'arrival platform', 'duration', 'price', 'type', 'zone']

# to weed this out we must assign each field an index  //  or each index a field?
# check which POSITIONS, only have one field. assign and delete from fields

def simplify1(possible):
    # print(possible)
    assigned = [None] * len(possible)

    # fields_to_assign = deepcopy(fields)

    while any(possible):
        for i, poss in enumerate(possible):
            if len(poss) == 1:
                assigned[i] = match = poss.pop()
                break

        for other in possible:
            if match in other:
                other.remove(match)

    return assigned


# 20 fields, 201 valid tickets
def part2(my_ticket, tickets):
    n_tickets = len(tickets)
    n_fields = len(my_ticket)
    fields = [ranges[i].field for i in range(len(ranges))]

    # list with full range of posibilities for each value on ticket
    # in the order they are listed in input (zone / 19 last)
    possible1 = [[field for field in fields] for _ in range(len(ranges))]
    # possible[0] == all fields, possible[1] = all fields, etc. len = 20
    possible2 = [set(range(n_fields)) for _ in range(len(ranges))]

    # print('num tickets (pre clean): {}'.format(n_tickets))

    # take each ticket
    # take at each val in ticket
    # take ranges and possible fields
    # remove fields for which val don't fit
    for ticket in filter(clean_tickets, tickets):
        for i, value in enumerate(ticket):
            for rng in ranges:
                if value not in rng and rng.field in possible1[i]:
                    possible1[i].remove(rng.field)

    # print('___')
    # print(possible1)
    # for p in possible1:
    #     print(len(p))
    # print('___')

    # take each ticket
    # take ranges and possible fields
    # take each val in that ticket:
    # remove fields for which ticket val is out of range
    for ticket in filter(clean_tickets, tickets):
        for rng, poss in zip(ranges, possible2):
            for i, value in enumerate(ticket):
                if value not in rng and i in poss:
                    poss.remove(i)
    
    # print(possible2)
    
    indexes1 = simplify1(possible1)
    # print('indexes1: \n{}\n'.format(indexes1))
    # in order of pos on ticket, each pos' related field
    # have value, use key to look up field?
    # [value, fieldname] -> [key: go to field] -> [value assigned to field]
    # [pos0 <= 'duration', pos1 <= 'seat', pos2 <= 'arrival platform', pos3 <= 'row', ..., pos19 <= 'departure location']

    # in: 113,53,97,59,139,73,89,109,67,71,79,127,149,107,137,83,131,101,61,103  (ticket)
    # key: ['class', 'seat', 'arr platform', ... 'wagon', 'zone' ,'dep location']
    # out: 113 = class, 53 = seat, 97 = arr platform, ..., wagon = 101, zone = 61, dep location = 103 

    # NOT ['zone', 'train', 'class', 'route', 'duration', 'arrival location', 'arrival platform', 'seat', 'departure platform', 'departure time', 'departure location', 'price', 'departure date', 'row', 'departure track', 'departure station', 'arrival track', 'arrival station', 'type', 'wagon']
    # i.e. [pos0 = zone, pos1 = train, pos2 = class, ... pos19 = wagon]
    # this is WRONGly lokked up from the possible fields below
    
    indexes2 = simplify(possible2)
    # print('indexes2: \n{}\n'.format(indexes2))
    # in order of fields, each field's pos on ticket
    # i.e look at _fields_ -> go to pos on ticket to get value
    # have field, use key to look up value
    # [fields] -> [key: go to pos on ticket] -> [value]
    # [19, 16, 10, 13, 11, 6, 8, 15, 2, 5, 0, 12, 4, 14, 3, 1, 9, 7, 17, 18]
    # [0: departure location => pos19, 1: departure station => pos16, 2: departure platform => pos10, ... zone = pos18]

    # in: [19, 16, 10, 13, 11, 6, 8, 15, 2, 5, 0, 12, 4, 14, 3, 1, 9, 7, 17, 18]
    # key: 113,53,97,59,139,73,89,109,67,71,79,127,149,107,137,83,131,101,61,103  (ticket)
    # out: pos 0 > field 0, dep location & tpos 19: 103:  dep location = 103
    #      pos 1 > field 1, dep station, & tpos 16: 131:  dep station = 131
    #      pos 2 > field 2, dep platform, & tpos 10: 79:  dep platform = 79
    #      pos 3 > field 3, dep track, & tpos 13: 107:    dep track = 107
    #      pos 4 > field 4, dep date & tpos 11: 127       dep date = 127
    #      pos 5 > field 5, dep time & tpos 6: 89         dep time = 89
    #      pos 6 > field 6, arr loc & tpos 8: 67          arr location = 67
    #      ...
    #      pos 8  > field 8,  arr platform & tpos 2: 97   seat = 97 
    #      pos 10 > field 10, class & tpos 0:             class = 113
    #      pos 11 > field 11, duration & tpos 12: 149     duration = 149
    #      pos 12 > field 12, price & tpos 4: 139         price = 139
    #      pos 14 > field 14, row & tpos 3: 59            row = 59
    #      pos 15 > field 15, seat & tpos 1: 53           seat = 53
    #      pos 18 > field 18, wagon & tpos 17: 101        wagon = 101
    #      pos 19 > field 19, zone, & tpos 18: 61:        zone = 61


    total1 = prod(my_ticket[i] for i, f in enumerate(indexes1) if 'departure' in f)
    # print(total1)

    total2 = prod(my_ticket[i] for i in indexes2[:6])
    # print(total2)

    return total1


# --------------

with open("input.txt", "r") as f:
    ranges, my_ticket, tickets = parse_input(f)


print('Part 1: result = {}'.format(part1(tickets)))
print('Part 2: result = {}'.format(part2(my_ticket, tickets)))
