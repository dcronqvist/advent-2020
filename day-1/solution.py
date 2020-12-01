def read_input():
    with open("input.txt", "r") as f:
        return f.read()

def read_input_lines(cast):
    with open("input.txt", "r") as f:
        return [cast(l.strip()) for l in f.readlines()]

def read_input_separated(c):
    with open("input.txt", "r") as f:
        return f.read().split(c)

def binary_search(li, item):
    li.sort()
    upper = len(li) - 1
    lower = 0
    middle = int((upper + lower) / 2)
    while li[middle] != item:
        if li[middle] > item:
            upper = middle
        elif li[middle] < item:
            lower = middle
        middle = int((upper + lower) / 2)
        if upper <= lower + 1:
            break
        if li[middle] == item:
            return True
    return False

lines = read_input_lines(int)

# PART 1
def part1(lines):
    for num1 in lines:
        remainder = 2020 - num1
        if binary_search(lines, remainder):
            return num1 * remainder

# PART 2
# We only have input of N = 200, N^3 will be 8 * 10^6, will run in a few seconds.
# literal definition spaghetti code <3, but it gets the job done.
def part2():
    for num1 in lines:
        remainder = 2020 - num1
        for num2 in lines:
            if binary_search(lines, remainder - num2):
                    return num1 * num2 * (remainder - num2)

print(f"Part 1: {part1(lines)}")
print(f"Part 2: {part2()}")
    
