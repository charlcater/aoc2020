# Advent of Code 2020
# --- Day 9: Encoding Error ---

def two_sum(nums, target):
    compls = set()

    for x in nums:
        if x in compls:
            return True

        compls.add(target - x)

    return False


def part1(nums):

    # more efficient solution, O(n)
    for i, target in enumerate(nums[25:]):
        if not two_sum(nums[i:i + 25], target):
            break

    return target

    # this is quadrtic time
    # i = 0
    # low = 0
    # high = 25

    # for number in numlist[high:]:
    #     for n in numlist[low+i:high+i]:
    #         valid = 0
    #         nn = number - n

    #         if nn > 0 and nn in numlist[low+i:high+i]:
    #             # print('{} is valid'.format(number))
    #             valid = 1
    #             i += 1
    #             break
    #         else:
    #             pass
            
    #     if valid == 0:
    #         # print('invalid: {}'.format(number))
    #         return(number)


def part2(number, numbers):

    maxlen = len(numbers)
    i = 0 # index in input list

    while i < maxlen-1:
        doSum = True
        j = 1
        total = 0
        while doSum:
            # print(numbers[i:i+j])
            total = sum(x for x in numbers[i:i+j])
            # print(total)

            if total == number:
                # minval = max(numbers[i:i+j])
                # maxval = min(numbers[i:i+j])
                # print(minval, maxval)
                return(min(numbers[i:i+j]) + max(numbers[i:i+j]))
            elif total < number:
                j += 1
            else:
                i += 1
                doSum = False


nums = [int(entry.strip('\n')) for entry in open("input.txt", "r").readlines()]

print('Part 1: first invalid number = {}'.format(part1(nums)))
print('Part 2: encryption weakness = {}'.format(part2(part1(nums), nums)))
