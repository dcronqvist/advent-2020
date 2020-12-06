def read_input():
    with open("input.txt", "r") as f:
        return f.read()

def read_input_lines():
    with open("input.txt", "r") as f:
        return [l.strip() for l in f.readlines()]

def read_input_separated(c):
    with open("input.txt", "r") as f:
        return f.read().split(c)

def part1():
    lines = read_input_lines()

    groups = []

    c_group = []

    for line in lines:
        if line != '':
            c_group.append(line)
        else:
            groups.append(c_group)
            c_group = []

    s = set()
    counter = 0

    for group in groups:
        for g in group:
            for char in g:
                s.add(char)
        counter += len(s)
        s = set()

    return counter

def part2():
    lines = read_input_lines()

    groups = []

    c_group = []

    for line in lines:
        if line != '':
            c_group.append(line)
        else:
            groups.append(c_group)
            c_group = []

    counter = 0

    for group in groups:
        group_answered = dict()
        group_lenght = len(group)
        for g in group:
            for char in g:
                if char in group_answered:
                    group_answered[char] += 1
                else:
                    group_answered[char] = 1

        s = 0
        for char in group_answered.keys():
            if group_answered[char] == group_lenght:
                s += 1
        counter += s

    return counter

print(f"PART 1: {part1()}")
print(f"PART 2: {part2()}")