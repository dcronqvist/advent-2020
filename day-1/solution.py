def read_input():
    with open("input.txt", "r") as f:
        return f.read()

def read_input_lines(cast):
    with open("input.txt", "r") as f:
        return [cast(l.strip()) for l in f.readlines()]

def read_input_separated(c):
    with open("input.txt", "r") as f:
        return f.read().split(c)

lines = read_input_lines(int)

# PART 1
def part1():
    for num1 in lines:
        for num2 in lines:
            if num1 + num2 == 2020:
                return num1 * num2

# PART 2
# We only have input of N = 200, N^3 will be 8 * 10^6, will run in a few seconds.
# literal definition spaghetti code <3, but it gets the job done.
def part2():
    for num1 in lines:
        for num2 in lines:
            for num3 in lines:
                if num1 + num2 + num3 == 2020:
                    return num1 * num2 * num3

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
