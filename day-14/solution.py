def read_input_lines():
    with open("input.txt", "r") as f:
        return [l.strip() for l in f.readlines()]

def get_num(s, mask):
    num = ""
    for i in range(len(mask)):
        if mask[i] != "X":
            num += mask[i]
        else:
            num += s[i]
    return num.zfill(36)

def get_addresses(s, mask):
    # 0 in mask -> s[i] unchanged
    # 1 in mask -> s[i] is overwritten with 1
    # X in mask -> s[i] is floating, 0 and 1
    addresses = []
    new = ""
    for i in range(len(mask)):
        if mask[i] == "0":
            new += s[i]
        elif mask[i] == "1":
            new += "1"
        else:
            new += "X"

    addresses.append("")
    for i in range(len(new)):
        if new[i] != "X":
            for j in range(len(addresses)):
                addresses[j] += new[i]
        else:
            news = []
            for j in range(len(addresses)):
                news.append(addresses[j] + "0")
                addresses[j] += "1"
            addresses.extend(news)

    return addresses

    

def part1():
    mem = dict()
    lines = read_input_lines()
    lines = [(line.split("=")[0].strip(), line.split("=")[1].strip()) for line in lines]
    mask = "X" * 36
    
    for (s, num) in lines:
        if "mask" in s:
            # We're setting the mask
            mask = num
        elif "mem" in s:
            address = s.split("[")[1][:-1]
            mem[address] = get_num((str(bin(int(num))[2:])).zfill(36), mask)

    return sum([int(mem[k], 2) for k in mem])

def part2():
    mem = dict()
    lines = read_input_lines()
    lines = [(line.split("=")[0].strip(), line.split("=")[1].strip()) for line in lines]
    mask = "X" * 36
    
    for (s, num) in lines:
        if "mask" in s:
            # We're setting the mask
            mask = num
        elif "mem" in s:

            address = s.split("[")[1][:-1]
            addr = get_addresses(bin(int(address))[2:].zfill(36), mask)

            for ad in addr:
                mem[ad] = (str(bin(int(num))[2:])).zfill(36)

    return sum([int(mem[k], 2) for k in mem])

print(part1())
print(part2())