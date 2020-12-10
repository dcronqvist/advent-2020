def read_input():
    with open("input.txt", "r") as f:
        return f.read()

def read_input_lines(cast):
    with open("input.txt", "r") as f:
        return [cast(l.strip()) for l in f.readlines()]

def read_input_separated(c):
    with open("input.txt", "r") as f:
        return f.read().split(c)

def part1():
    one_jolt_diff = 1
    three_jolt_diff = 1

    lines = read_input_lines(int)
    lines.sort()
    current_adapter = lines[0]
    i = 1

    while i < len(lines):

        diff = lines[i] - current_adapter

        if diff == 1:
            one_jolt_diff += 1
        elif diff == 3:
            three_jolt_diff += 1

        current_adapter = lines[i]

        i += 1

    return one_jolt_diff * three_jolt_diff

print(f"Part 1: {part1()}")

d = dict()
def part2(current, lines):
    if lines:
        if (current, len(lines)) in d:
            return d[(current, len(lines))]

        if len(lines) == 1:
            return 1
        elif len(lines) == 0:
            return 0

        valids = 0
        for i in range(0, len(lines)):
            if lines[i] - 3 <= current:
                valids += part2(lines[i], lines[1+i:])

        d[(current, len(lines))] = valids

        return valids
    else:
        return 0

print(f"Part 2: {2 * part2(0, sorted(read_input_lines(int)))}")
    
    




