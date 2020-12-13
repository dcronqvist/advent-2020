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

    # 0 = EAST
    # 1 = SOUTH
    # 2 = WEST
    # 3 = NORTH
    direction = 0

    X = 0
    Y = 0

    for line in lines:
        
        action = line[0]
        num = int(line[1:])

        if action == "L":
            direction -= int(num / 90)
        elif action == "R":
            direction += int(num / 90)
        direction = direction % 4

        if action == "F":
            if direction == 0:
                X += num
            elif direction == 1:
                Y += num
            elif direction == 2:
                X -= num
            elif direction == 3:
                Y -= num
        
        if action == "N":
            Y -= num
        elif action == "S":
            Y += num
        elif action == "E":
            X += num
        elif action == "W":
            X -= num

    return X + Y

def rotate_vector_clockwise(x, y):
    return y, -x

def part2():
    lines = read_input_lines()
    X = 10
    Y = 1
    s_X = 0
    s_Y = 0

    for line in lines:    
        action = line[0]
        num = int(line[1:])
        if action == "L":
            amount = int(num / 90)
            for _ in range(4 - amount):
                X, Y = rotate_vector_clockwise(X, Y)
        elif action == "R":
            amount = int(num / 90)
            for _ in range(amount):
                X, Y = rotate_vector_clockwise(X, Y)
        elif action == "F":
            s_X += num * X
            s_Y += num * Y      
        if action == "N":
            Y += num
        elif action == "S":
            Y -= num
        elif action == "E":
            X += num
        elif action == "W":
            X -= num
    return abs(s_X) + abs(s_Y)


print(part1())
print(part2())
