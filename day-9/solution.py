def read_input():
    with open("input.txt", "r") as f:
        return f.read()

def read_input_lines():
    with open("input.txt", "r") as f:
        return [l.strip() for l in f.readlines()]

def read_input_separated(c):
    with open("input.txt", "r") as f:
        return f.read().split(c)

def twosum(nums, num):
    
    for n in nums:
        rem = num - n
        if rem in nums:
            return True
    return False

def part1():
    nums = [int(line) for line in read_input_lines()]

    for i in range(25, len(nums)):
        previous = nums[i - 25:i]
        if not twosum(previous, nums[i]):
            return nums[i]
    return -1

print(f"PART 1: {part1()}")

def part2():
    nums = [int(line) for line in read_input_lines()]
    k = part1()
    for i in range(0, len(nums)):
        for j in range(i, len(nums)):
            temp = nums[i:j+1]
            if sum(temp) == k:
                return min(temp) + max(temp)
    return -1
    

print(f"PART 2: {part2()}")





