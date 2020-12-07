# Advent of Code 2020
# --- Day 1: Report Repair ---

def part1(lines):

    count = 0
    lineslen = len(lines)
    
    for num1 in lines:
        count += 1

        for num2 in lines[count:lineslen]:
            sum = num1 + num2

            if sum == 2020:
                product = num1 * num2
                return product


def part2(lines):

    count = 0
    lineslen = len(lines)

    for num1 in lines:
        count += 1

        for num2 in lines[count:lineslen]:

            for num3 in lines[count+1:lineslen]:
                sum = num1 + num2 + num3

                if sum == 2020:
                    # print('Found it: {} + {} + {}'.format(num1, num2, num3))
                    product = num1 * num2 * num3
                    return product


lines = [int(line.strip()) for line in open("input.txt", "r").readlines()]
print('Part 1: product = {}'.format(part1(lines)))
print('Part 2: product = {}'.format(part2(lines)))