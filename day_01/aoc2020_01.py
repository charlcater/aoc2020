# Advent of Code 2020
# --- Day 1: Report Repair ---

def part1(lines):

    # quadratic time, O(n^2)
    # count = 0
    # lineslen = len(lines)
    
    # for num1 in lines:
    #     count += 1

    #     for num2 in lines[count:lineslen]:
    #         sum = num1 + num2

    #         if sum == 2020:
    #             product = num1 * num2
    #             return product

    # linear time, O(n)
    compls  = set()
    for x in lines:
        y = 2020 - x

        if x in compls:
            return  x * y

        compls.add(y)


def part2(lines):

    # Cubic time (!), O(n^3)
    # count = 0
    # lineslen = len(lines)

    # for num1 in lines:
    #     count += 1

    #     for num2 in lines[count:lineslen]:

    #         for num3 in lines[count+1:lineslen]:
    #             sum = num1 + num2 + num3

    #             if sum == 2020:
    #                 # print('Found it: {} + {} + {}'.format(num1, num2, num3))
    #                 product = num1 * num2 * num3
    #                 return product

    # quatratic time, O(n^2)
    for i, x in enumerate(lines):
        compls = set()
        yz = 2020 - x

        for y in lines[i + 1:]:
            z = yz - y

            if y in compls:
                return x * y * z

            compls.add(z)


lines = [int(line.strip()) for line in open("input.txt", "r").readlines()]
print('Part 1: product = {}'.format(part1(lines)))
print('Part 2: product = {}'.format(part2(lines)))