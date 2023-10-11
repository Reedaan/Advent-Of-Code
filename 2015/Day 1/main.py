data = open("/home/odinproject/repos/Advent-Of-Code/2015/Day 1/input.txt", "r").readlines()
data = [line.strip(" ") for line in data]
data = [line.strip("\n") for line in data]
data = [line.replace(" ", "") for line in data]

def part_one():
    floor = 0
    for element in range(len(data[0])):
        if data[0][element] == "(":
            floor += 1
            
        elif data[0][element] == ")":
            floor -= 1
    return floor
    
def part_two():
    floor = 0
    for element in range(len(data[0])):
        if data[0][element] == "(":
            floor += 1
        elif data[0][element] == ")":
            floor -= 1
            if floor < 0:
                position_string = data[0][:element]
                return len(position_string) + 1
    return floor

#Part two
#Find the position that causes him to enter basement

print(part_one())
print(part_two())