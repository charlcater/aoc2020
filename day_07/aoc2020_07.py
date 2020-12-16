# Advent of Code 2020
# --- Day 7: Handy Haversacks ---

import re

def part1(d):

    count = 0
    parents = []

    for key, value in d.items():
        for v in value:
            if 'shiny gold' in v:
                parents.append(key)
    count += len(parents)
    nestings = 1
    counted = parents

    doNest = True
    while doNest:
        nestNew = []
        for key, value in d.items():
            for v in value:
                for bag in parents:
                    if bag in v and key not in counted:
                        nestNew.append(key)  # get the parent bag
                        counted.append(key)
        parents = nestNew

        if len(nestNew) == 0:
            doNest = False
        else:
            # print(len(nestNew))
            count += len(nestNew)
            nestings += 1

    # print('max nesting levels: {}, count: {}'.format(nestings, count))

    return count

def get_bags(d, bag_col):
    if len(d.get(bag_col)) == 0:
        # print('end')
        return 1

    total = 1
    for col, num in d[bag_col].items():
        x = d[bag_col]
        total += int(num) * int(get_bags(d, col))

    return total


rules = [rule for rule in open("testinput.txt", "r").read().split('\n')]

# parsing
d = {}
for line in rules:
    patt1 = re.compile('(\s*)bags(\s*)')
    patt2 = re.compile('(\s*)bag(\s*)')
    rule = patt1.sub(' ', line).strip('. ')
    rule2 = patt2.sub(' ', rule).split()

    key = '{} {}'.format(rule2[0], rule2[1])
    val = (' '.join([word for word in rule2[3:]]).split(' , '))

    innerbag = {}
    for v in val:
        innerkey = v[2:]
        if v[0].isdigit():
            innerval = v[0]
        else:
            continue
        innerbag[innerkey] = innerval

    d[key] = innerbag


# print('Part 1: total bags = {}'.format(part1(d)))
bag_col = 'shiny gold'
print('Part 2: total bags in a {} bag = {}'.format(bag_col, get_bags(d, bag_col)-1))
