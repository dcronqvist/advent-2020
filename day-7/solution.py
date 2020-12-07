def read_input():
    with open("input.txt", "r") as f:
        return f.read()

def read_input_lines():
    with open("input.txt", "r") as f:
        return [l.strip() for l in f.readlines()]

def read_input_separated(c):
    with open("input.txt", "r") as f:
        return f.read().split(c)


class Node:
    def __init__(self, color, children):
        self.children = children
        self.color = color

def create_tree1():
    lines = read_input_lines()

    nodes = []

    for line in lines:
        if not ("no other bags" in line):
            splitted = [s.strip() for s in line.split("contain")]
            color = splitted[0].split("bags")[0].strip()
            vals = [s.strip().split()[0] for s in splitted[1].split(",")]    
            children_keys = [" ".join(s.strip().split(" ")[1:3]) for s in splitted[1].split(",")]  
            di = dict()
            for i in range(0, len(children_keys)):
                di[children_keys[i]] = vals[i]
            node = Node(color, di)
            nodes.append(node)
        else:
            splitted = [s.strip() for s in line.split("contain")]
            #print(splitted)
            color = splitted[0].split("bags")[0].strip()
            node = Node(color, dict())
            nodes.append(node)

    return nodes

def find_parents(tree, color):
    l = set()
    for node in tree:
        for col in node.children.keys():
            if color in col:
                l.add(node.color)  
                l.update(find_parents(tree, node.color))  
    return l

def calc_contains(tree, color):
    count = 0
    for node in tree:
        if node.color == color:
            for col in node.children:
                amount = int(node.children[col])
                cont = calc_contains(tree, col)
                print(f"BOTTOM: {color} contains {amount} {col}, which each contains {cont} other bags = {amount + amount * cont}")
                count += amount
                count += amount * cont
                print(f"{color} is now up to {count}")
    print(f"{color} CONTAINS {count} bags")
    return count
    

def part1():
    tree = create_tree1()
    p = find_parents(tree, "shiny gold")
    return len(p)

def part2():
    tree = create_tree1()
    c = calc_contains(tree, "shiny gold")
    return c

print(part1())
print(part2())

    

