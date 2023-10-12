data = open("/home/odinproject/repos/Advent-Of-Code/2015/Day 3/input.txt", "r").read()
data = [line.strip(" ") for line in data]
data = [line.strip("\n") for line in data]
data = [line.replace(" ", "") for line in data]

def part_one():
    x = 0
    y = 0
    current_position = (x,y)
    already_visited = [(0,0)]

    data_list = list(data[0])

    for element in data_list:
        #North
        if element == "^":
            y += 1
            current_position = (x,y)
            if current_position in already_visited:
                pass
            else:
                already_visited.append(current_position)
        #South  
        elif element == "v":
            y -= 1
            current_position = (x,y)
            if current_position in already_visited:
                pass
            else:
                already_visited.append(current_position)
        #East
        elif element == ">":
            x += 1
            current_position = (x,y)
            if current_position in already_visited:
                pass
            else:
                already_visited.append(current_position)
        #West
        elif element == "<":
            x -= 1
            current_position = (x,y)
            if current_position in already_visited:
                pass
            else:
                already_visited.append(current_position)
            
    return(len(already_visited))
        
def part_two():
    x_santa = 0
    y_santa = 0
    
    x_robot = 0
    y_robot = 0

    current_position_santa = (x_santa, y_santa)
    current_position_robot = (x_robot, y_robot)

    already_visited = set()  

    for index, element in enumerate(data):
        if index % 2 == 0:
            current_position = (x_santa, y_santa)
        else:
            current_position = (x_robot, y_robot)

        if element == '^':
            current_position = (current_position[0], current_position[1] + 1)
        elif element == 'v':
            current_position = (current_position[0], current_position[1] - 1)
        elif element == '>':
            current_position = (current_position[0] + 1, current_position[1])
        elif element == '<':
            current_position = (current_position[0] - 1, current_position[1])

        already_visited.add(current_position)

        if index % 2 == 0:
            x_santa, y_santa = current_position
        else:
            x_robot, y_robot = current_position

    return len(already_visited)

    

print(part_two())
