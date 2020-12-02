def read_input():
    with open("input.txt", "r") as f:
        return f.read()

def read_input_lines():
    with open("input.txt", "r") as f:
        return [l.strip() for l in f.readlines()]

def read_input_separated(c):
    with open("input.txt", "r") as f:
        return f.read().split(c)

def countchar(s, c):
    count = 0
    for k in s:
        if k == c:
            count += 1
    return count

def sol():
    lines = read_input_lines()
    counter = 0
    for line in lines:
        colon = line.split(":")
        char = colon[0][-1]
        times = colon[0][:-2]
        times = times.split("-")
        min_times = int(times[0])
        max_times = int(times[1])
        if countchar(colon[1].strip(), char) >= min_times and countchar(colon[1].strip(), char) <= max_times:
            counter += 1
    return counter

def xor(a, b):
    return (a and not b) or (b and not a)

def sol2():
    lines = read_input_lines()
    counter = 0
    for line in lines:
        colon = line.split(":")
        s = colon[1].strip()
        char = colon[0][-1]
        times = colon[0][:-2]
        times = times.split("-")
        pos_1 = int(times[0])
        pos_2 = int(times[1])
        x = xor(s[pos_1 - 1] == char, s[pos_2 - 1] == char)
        if x:
            counter += 1
    return counter


print(f"SOL RETURN: {sol()}")
print(f"SOL2 RETURN: {sol2()}")