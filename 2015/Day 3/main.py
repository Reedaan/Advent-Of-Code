data = open("Day 3/input.txt", "r").readlines()
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
