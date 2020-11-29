def read_input():
    with open("input.txt", "r") as f:
        return f.read()

def read_input_lines():
    with open("input.txt", "r") as f:
        return [l.strip() for l in f.readlines()]

def read_input_separated(c):
    with open("input.txt", "r") as f:
        return f.read().split(c)