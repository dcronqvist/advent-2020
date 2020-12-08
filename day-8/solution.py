def read_input():
    with open("input.txt", "r") as f:
        return f.read()

def read_input_lines():
    with open("input.txt", "r") as f:
        return [l.strip() for l in f.readlines()]

def read_input_separated(c):
    with open("input.txt", "r") as f:
        return f.read().split(c)


def part1(p):
    i = 0
    acc = 0
    d = dict()
    last = ("", 0, 0)
    while i < len(p):
        if i == len(p) - 1:
            return acc, None
        if i in d:
            return None, acc
        else:
            d[i] = 1
            
        spl = p[i].split(" ")
        op = spl[0]
        num = spl[1].replace("+", "")
        if op == "acc":
            acc += int(num)
            i += 1
        elif op == "jmp":
            i += int(num)
        else:
            i += 1

def part2():
    lines = read_input_lines()

    for i in range(len(lines)):

        p = lines[:]

        if "jmp" in p[i]:
            p[i] = p[i].replace('jmp', 'nop')
        elif p[i].startswith('nop'):
            p[i] = p[i].replace('nop', 'jmp')
        x, y = part1(p)
        if x:
            print(x)

print(part1(read_input_lines()))
part2()