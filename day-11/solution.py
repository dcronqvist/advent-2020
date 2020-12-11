def read_input():
    with open("input.txt", "r") as f:
        return f.read()

def read_input_lines(cast=lambda x: x):
    with open("input.txt", "r") as f:
        return [cast(l.strip()) for l in f.readlines()]

def read_input_separated(c):
    with open("input.txt", "r") as f:
        return f.read().split(c)

def empty(lines, x, y):
    
    up = False
    if y-1 >= 0:
        up = lines[y-1][x] == "#"

    left = False
    if x-1 >= 0:
        left = lines[y][x-1] == "#"

    right = False
    if x+1 < len(lines[0]):
        right = lines[y][x+1] == "#"

    down = False
    if y+1 < len(lines):
        down = lines[y+1][x] == "#"

    up_left = False
    if y-1 >= 0 and x-1 >= 0:
        up_left = lines[y-1][x-1] == "#"

    up_right = False
    if y-1 >= 0 and x + 1 < len(lines[0]):
        up_right = lines[y-1][x+1] == "#"

    down_right = False
    if x+1 < len(lines[0]) and y + 1 < len(lines):
        down_right = lines[y+1][x+1] == "#"

    down_left = False
    if y+1 < len(lines) and x-1 >= 0:
        down_left = lines[y+1][x-1] == "#"

    middle = lines[y][x] == "L"

    return middle and not (left or up or down or right or up_left or up_right or down_left or down_right)

def empty2(lines, x, y):
    middle = lines[y][x] == "L"
    adj = []

    if middle:
        for _x in [-1, 0, 1]:
            for _y in [-1, 0, 1]:
                if _x == 0 and _y == 0:
                    continue

                i = 1
                while 0 <= y + i*_y < len(lines) and 0 <= x + i*_x < len(lines[0]):
                    if lines[y + i*_y][x + i*_x] != ".":
                        adj.append(lines[y + i*_y][x + i*_x])
                        break
                    i += 1

    return middle and "#" not in adj

def occupied1(lines, x, y, amount):
    middle = lines[y][x] == "#"
    up = False
    if y-1 >= 0:
        up = lines[y-1][x] == "#"

    left = False
    if x-1 >= 0:
        left = lines[y][x-1] == "#"

    right = False
    if x+1 < len(lines[0]):
        right = lines[y][x+1] == "#"

    down = False
    if y+1 < len(lines):
        down = lines[y+1][x] == "#"

    up_left = False
    if y-1 >= 0 and x-1 >= 0:
        up_left = lines[y-1][x-1] == "#"

    up_right = False
    if y-1 >= 0 and x + 1 < len(lines[0]):
        up_right = lines[y-1][x+1] == "#"

    down_right = False
    if x+1 < len(lines[0]) and y + 1 < len(lines):
        down_right = lines[y+1][x+1] == "#"

    down_left = False
    if y+1 < len(lines) and x-1 >= 0:
        down_left = lines[y+1][x-1] == "#"

    return middle and ((left + up + down + right + up_left + up_right + down_right + down_left) >= amount)

def occupied2(lines, x, y, amount):
    middle = lines[y][x] == "#"
    adj = []

    if middle:
        for _x in [-1, 0, 1]:
            for _y in [-1, 0, 1]:
                if _x == 0 and _y == 0:
                    continue

                i = 1
                while 0 <= y + i*_y < len(lines) and 0 <= x + i*_x < len(lines[0]):
                    if lines[y + i*_y][x + i*_x] != ".":
                        adj.append(lines[y + i*_y][x + i*_x])
                        break
                    i += 1
    return middle and adj.count("#") >= amount

def count_occupied(lines):
    count = 0
    for line in lines:
        for char in line:
            if char == "#":
                count += 1
    return count

def step1(grid):
    new_grid = []

    for y in range(0, len(grid)):
        new_row = ""
        for x in range(0, len(grid[y])):
            if empty(grid, x, y):
                new_row += "#"
                continue
            elif occupied1(grid, x, y, 4):
                new_row += "L"
                continue
            
            new_row += grid[y][x]
        new_grid.append(new_row)
            
    return new_grid

def step2(grid):
    new_grid = []

    for y in range(0, len(grid)):
        new_row = ""
        for x in range(0, len(grid[y])):
            if empty2(grid, x, y):
                new_row += "#"
                continue
            elif occupied2(grid, x, y, 5):
                new_row += "L"
                continue
            
            new_row += grid[y][x]
        new_grid.append(new_row)
            
    return new_grid

def part1():
    lines = [line for line in read_input_lines()]
    grid = lines
    while True:
        after = step1(grid)
        if grid == after:
            return count_occupied(after)
        grid = after
    None

def part2():
    lines = [line for line in read_input_lines()]
    grid = lines
    counter = 0
    while True:
        print(counter)
        after = step2(grid)
        #print(grid[0][:20])
        #print(after[0][:20])
        if grid == after:
            return count_occupied(after)
        grid = after
        counter += 1
    None

#print(part1())
print(part2())


