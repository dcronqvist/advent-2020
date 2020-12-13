def read_input():
    with open("input.txt", "r") as f:
        return f.read()

def read_input_lines():
    with open("input.txt", "r") as f:
        return [l.strip() for l in f.readlines()]

def read_input_separated(c):
    with open("input.txt", "r") as f:
        return f.read().split(c)

def check_bus(bus, timestamp):
    temp = bus
    while temp < timestamp:
        temp += bus
    return temp - timestamp

def part1():
    lines = read_input_lines()
    timestamp = int(lines[0])
    buses = [int(bus) for bus in lines[1].split(",") if bus != "x"]
    diffs = [(bus, check_bus(bus, timestamp)) for bus in buses]
    diffs = sorted(diffs, key=lambda x: x[1])
    return diffs[0][0] * diffs[0][1]

# This uses the chinese remainder theorem
def part2():
    lines = read_input_lines()
    buses = lines[1].split(",")

    pairs = [(int(buses[i]), int(buses[i]) - i) for i in range(0,len(buses)) if buses[i] != "x"]

    M = 1
    for num, m_i in pairs:
        M *= num

    total = 0
    for num, m_i in pairs:
        b = int(M / num)
        total += m_i * b * pow(b, num-2, num)
        total %= M

    return total

print(part1())
print(part2())