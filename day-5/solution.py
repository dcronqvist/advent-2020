def read_input():
    with open("input.txt", "r") as f:
        return f.read()

def read_input_lines():
    with open("input.txt", "r") as f:
        return [l.strip() for l in f.readlines()]

def read_input_separated(c):
    with open("input.txt", "r") as f:
        return f.read().split(c)


def sol():
    lines = read_input_lines()

    seat_ids = []
    all_ids = []

    for row in range(0, 128):
        for column in range(0, 8):
            all_ids.append(row * 8 + column)

    for line in lines:
        #print(line)

        # CALC ROWS
        lower = 0
        upper = 127

        middle = int((upper + lower) / 2)
        counter = 0

        while counter < 7:
            #print(f"{lower}-{upper}")
            if line[counter] == "F":
                upper = middle
            else:
                lower = middle + 1
            counter += 1
            middle = int((upper + lower) / 2)

        #print(middle)

        # MIDDLE WILL BE OUR ROW

        #print(f"We got {middle} as row")

        column = 0
        lower = 0
        upper = 7

        c_middle = int((upper + lower) / 2)
        #c_middle = 0

        while column < 3:
            #print(f"{lower}-{upper}")
            if line[counter + column] == "R":
                lower = c_middle + 1
            else:
                upper = c_middle
            column += 1
            c_middle = int((upper + lower) / 2)
        #print(c_middle)

        #print(f"We got {c_middle} as column")
        
        seat_ids.append(middle * 8 + c_middle)
        #return seat_ids[0]

    seat_ids.sort()

    max_seat = seat_ids[-1]

    yours = 0
    for i in range(0, len(seat_ids)-1):
        if seat_ids[i+1] - seat_ids[i] == 2:
            yours = seat_ids[i] + 1

    return yours, max_seat

print(f"{sol()}")
            
