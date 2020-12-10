# Advent of Code 2020
# --- Day 4: Passport Processing ---

def part1(entries):

    valid = 0

    for entry in entries:
        d = {}
        for field in entry.split():
            (key, val) = field.split(':')
            d[key] = val

        if (len(d) == 8) or (len(d) == 7 and 'cid' not in d):
            valid += 1
        else:
            pass

    return valid

def part2(entries):

    correct = 0

    for entry in entries:
        d = {}
        eyecol = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        for field in entry.split():
            (key, val) = field.split(':')
            d[key] = val

        valid = True

        if not ((len(d) == 8) or (len(d) == 7 and 'cid' not in d)):
            valid = False
        if 'byr' in d and not (1920 <= int(d['byr']) <= 2002):
            valid = False
            # print('byr: {}'.format(d.get('byr')))
        if 'iyr' in d and not (2010 <= int(d['iyr']) <= 2020):
            # print('iyr: {}'.format(d.get('iyr')))
            valid = False
        if 'eyr' in d and not (2020 <= int(d['eyr']) <= 2030):
            # print('eyr: {}'.format(d.get('eyr')))
            valid = False
        if 'hgt' in d  and not (( 'cm' in d['hgt'] and ( 150 <= int(d['hgt'].strip('cm')) <= 193)) or ( 'in' in d['hgt'] and ( 59 <= int(d['hgt'].strip('in')) <= 76))):
            # print('hgt: {}'.format(d.get('hgt')))
            valid = False
        if 'hcl' in d and not (d['hcl'].strip('#').isalnum() and len(d['hcl']) == 7):
            # print('hcl: {}'.format(d.get('hcl')))
            valid = False
        if 'ecl' in d and not (d['ecl'] in eyecol):
            # print('ecl: {}'.format(d.get('ecl')))
            valid = False
        if 'pid' in d and not (len(d['pid']) == 9):
            # print('pid: {}'.format(d.get('pid')))
            valid = False

        if valid == True:
            correct += 1

    return correct

entries = [entry.strip('\n') for entry in open("input.txt", "r").read().split('\n\n')]

print('Part 1: valid passports = {}'.format(part1(entries)))
print('Part 2: valid passports = {}'.format(part2(entries)))
