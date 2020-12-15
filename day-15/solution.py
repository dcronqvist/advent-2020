def read_input_separated(c):
    with open("input.txt", "r") as f:
        return f.read().split(c)

def part1(num):
    inp = read_input_separated(",")
    inp = [int(x) for x in inp]

    d = dict()
    nums = []
    for turn in range(1, num + 1):
        if turn <= len(inp):
            nums.append(inp[turn - 1])
        else:
            if len(d[nums[-1]]) == 1:
                nums.append(0)
            else:
                nums.append(d[nums[-1]][-1] - d[nums[-1]][-2])

        if nums[-1] not in d:
            d[nums[-1]] = []
        d[nums[-1]].append(turn)

    return nums[-1]

print(f"Part 1: {part1(2020)}")
print(f"Part 2: {part1(30000000)}")