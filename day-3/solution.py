def read_input():
    with open("input.txt", "r") as f:
        return f.read()

def read_input_lines():
    with open("input.txt", "r") as f:
        return [l.strip() for l in f.readlines()]

def read_input_separated(c):
    with open("input.txt", "r") as f:
        return f.read().split(c)


def sol(right, down):
    lines = read_input_lines()
    down_count = down
    trees = 0
    x = 0
    for line in lines:
        if down_count != down:
            down_count += 1
            continue
        else:
            down_count = 1
        if line[x] == "#":
            trees += 1 
        x += right
        if x >= len(line):
            x = x % len(line)
  
    return trees

print(f"PART 1: {sol(3, 1)}")
print(f"PART 2: {sol(1,1) * sol(3, 1) * sol(5, 1) * sol(7, 1) * sol(1, 2)}")