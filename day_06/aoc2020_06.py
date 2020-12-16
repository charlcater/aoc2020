# Advent of Code 2020
# --- Day 6: Custom Customs ---

import string
qs = string.ascii_lowercase

def part1(groups):

    count = 0

    for group in groups:
        groupanswers = []
        for answers in group:
            groupanswers.append(answers)

        for q in qs:
            if q in groupanswers:
                count += 1

    return count


def part2(groups):

    count = 0

    for group in groups:
        # print('group: \n{}\n'.format(group))
        groupanswers = []
        for answer in group.split('\n'):
            groupanswers.append(answer)
        # print(groupanswers)

        for a in groupanswers[0]:
            lettercount = 1
            for i in range(1, len(groupanswers)):
                if a in groupanswers[i]:
                    lettercount += 1
            if lettercount == len(groupanswers):
                count += 1
            # print(a, lettercount)
        # print('') 

    return count
    

groups = [entry for entry in open("input.txt", "r").read().split('\n\n')]

print('Part 1: sum of anyones = {}'.format(part1(groups)))
print('Part 2: sum of everyones = {}'.format(part2(groups)))
