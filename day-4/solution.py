def read_input():
    with open("input.txt", "r") as f:
        return f.read()

def read_input_lines():
    with open("input.txt", "r") as f:
        return [l.strip() for l in f.readlines()]

def read_input_separated(c):
    with open("input.txt", "r") as f:
        return f.read().split(c)


sample = {
    "byr": [1920, 2002],
    "iyr": [2010, 2020],
    "eyr": [2020, 2030],
    "hgt": {"cm": [150, 193], "in": [59, 76]},
    "hcl": 0,
    "ecl": 0,
    "pid": 0,
}

def check_pass(d):
    if "byr" in d:
        if not (int(d["byr"]) >= 1920 and int(d["byr"]) <= 2002):
            return False
    else:
        return False
    if "iyr" in d:
        if not (int(d["iyr"]) >= 2010 and int(d["iyr"]) <= 2020):
            return False
    else:
        return False
    if "eyr" in d:
        if not (int(d["eyr"]) >= 2020 and int(d["eyr"]) <= 2030):
            return False
    else:
        return False
    if "hgt" in d:
        if "cm" in d["hgt"]:
            num = int(d["hgt"].split("c")[0])
            if not (num >= 150 and num <= 193):
                return False
        if "in" in d["hgt"]:
            num = int(d["hgt"].split("i")[0])
            if not (num >= 59 and num <= 76):
                return False
    else:
        return False
    if "hcl" in d:
        if d["hcl"][0] != "#":
            return False
        else:
            if not (len(d["hcl"]) == 7):
                return False
            else:
                if not all([(x.isalpha() or x.isdigit()) for x in d["hcl"][1:]]):
                    return False
    else:
        return False
    if "ecl" in d:
        if not (d["ecl"] == "amb" or d["ecl"] == "blu" or d["ecl"] == "brn" or d["ecl"] == "gry" or d["ecl"] == "grn" or d["ecl"] == "hzl" or d["ecl"] == "oth"):
            return False
    else:
        return False
    if "pid" in d:
        if not len(d["pid"]) == 9:
            return False
    else:
        return False
    return True

def check_part1(passport, sample):
    for key in sample:
        if not (key in passport):
            return False
    return True

def part1():
    text = read_input_separated('\n')
    
    passports = []

    current = []
    for t in text:
        if t == "":
            # we are done with this passport
            passports.append(current)
            current = []            
        else:
            current.append(t)

    valids = 0

    for passport in passports:
        this_passport = {}
        for kvp in passport:
            multiple = kvp.split(" ")

            for keys in multiple:
                this_passport[keys.split(":")[0]] = keys.split(":")[1]

        if check_part1(this_passport, sample):
            valids += 1

    return valids

def part2():
    text = read_input_separated('\n')
    
    passports = []

    current = []
    for t in text:
        if t == "":
            # we are done with this passport
            passports.append(current)
            current = []            
        else:
            current.append(t)

    valids = 0

    for passport in passports:
        this_passport = {}
        for kvp in passport:
            multiple = kvp.split(" ")

            for keys in multiple:
                this_passport[keys.split(":")[0]] = keys.split(":")[1]

        if check_pass(this_passport):
            valids += 1

    return valids

print(f"PART 1: {part1()}")
print(f"PART 2: {part2()}")