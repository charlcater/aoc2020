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

    valid = 0

    for entry in entries:
        d = {}
        eyecol = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        for field in entry.split():
            (key, val) = field.split(':')
            d[key] = val

        if (len(d) == 8) or (len(d) == 7 and 'cid' not in d):
            if (int(d.get('byr')) >= 1920 and int(d.get('byr')) <= 2002):
                # print('byr: {}'.format(d.get('byr')))
                if (int(d.get('iyr')) >= 2010 and int(d.get('iyr')) <= 2020):
                    # print('iyr: {}'.format(d.get('iyr')))
                    if (int(d.get('eyr')) >= 2020 and int(d.get('eyr')) <= 2030):
                        # print('eyr: {}'.format(d.get('eyr')))
                        if ((( 'cm' in d.get('hgt')) and ( int(d.get('hgt').strip('cm')) >= 150 and int(d.get('hgt').strip('cm')) <= 193)) \
                            or (( 'in' in d.get('hgt')) and ( int(d.get('hgt').strip('in')) >= 59 and int(d.get('hgt').strip('in')) <= 76))):
                            # print('hgt: {}'.format(d.get('hgt')))
                            if (d.get('hcl').strip('#').isalnum() and len(d.get('hcl')) == 7):
                                # print('hcl: {}'.format(d.get('hcl'))
                                if (d.get('ecl') in eyecol):
                                    # print('ecl: {}'.format(d.get('ecl')))
                                    if (len(d.get('pid')) == 9):
                                        # print('pid: {}'.format(d.get('pid')))
                                        valid += 1
        else:
            pass

    return valid

entries = [entry.strip('\n') for entry in open("input.txt", "r").read().split('\n\n')]

print('Part 1: valid passports = {}'.format(part1(entries)))
print('Part 2: valid passports = {}'.format(part2(entries)))
