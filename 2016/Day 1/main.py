data = open("/home/odinproject/repos/Advent-Of-Code/2016/Day 1/input.txt", "r").readlines()
data = [line.strip(" ") for line in data]
data = [line.strip("\n") for line in data]
data = [line.replace(" ", "") for line in data]

data = [x.split(",") for x in data]


def first_part():
    facing = "NORTH"
    current_x = 0
    current_y = 0
    how_far = 0
    for entry in data:
        print("A")
        if facing == "NORTH":
            if entry[0] == "R":
                facing = "EAST"
                current_x += entry[1::]
            elif entry[0] == "L":
                facing = "WEST"
                current_x -= entry[1::]
        elif facing == "EAST":
            if entry[0] == "R":
                facing = "SOUTH"
                current_y -= entry[1::]
            elif entry[0] == "L":
                facing = "NORTH"
                current_y += entry[1::]
        elif facing == "SOUTH":
            if entry[0] == "R":
                facing = "WEST"
                current_x -= entry[1::]
            elif entry[0] == "L":
                facing = "EAST"
                current_x += entry[1::]
        elif facing == "WEST":
            if entry[0] == "R":
                facing = "NORTH"
                current_y += entry[1::]
            elif entry[0] == "L":
                facing = "SOUTH"
                current_y -= entry[1::]
    current_position = (current_x, current_y)
    return current_position
    


print(first_part())
    

