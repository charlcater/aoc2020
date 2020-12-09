# Advent of Code 2020
# --- Day 3: Toboggan Trajectory ---

def part1(lines):

    # line length = 31
    # step: right 3, down 1

    slope = [3,1]
    trees = 0

    right, down = (0, 0)

    while down < len(lines):

        if lines[down][right % len(lines[0])] == '#':
            trees += 1

        right += slope[0]
        down += slope[1] 

    return trees
    
def part2(lines):

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    treesproduct = 1

    for slope in slopes:
        trees = 0
        right, down = (0, 0)

        while down < len(lines):

            if lines[down][right % len(lines[0])] == '#':
                trees += 1

            right += slope[0]
            down += slope[1]

        # print(trees)
        treesproduct *= trees

    return treesproduct


lines = [line.strip('\n') for line in open("input.txt", "r").readlines()]
print('Part 1: trees encountered = {}'.format(part1(lines)))
print('Part 2: product of trees encountered = {}'.format(part2(lines)))
