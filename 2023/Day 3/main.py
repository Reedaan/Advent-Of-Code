import re
data = open("/home/odinproject/repos/Advent-Of-Code/2023/Day 3/input.txt", "r").readlines()
data = [line.strip(" ") for line in data]
data = [line.strip("\n") for line in data]
data = [line.replace(" ", "") for line in data]

def get_symbols():
    symbols = set()
    for line in data:
        symbol = re.findall(r'[^\d\s.]', line)
        for match in symbol:
            symbols.add(match)
    return symbols
    
symbol_list = get_symbols()       

def first_part():
    hash_map = {}

    for i, row in enumerate(data):
        for j, char in enumerate(row):
            hash_map[(i, j)] = char

    for key, value in hash_map.items():
        print(key, value)
        
    # print(hash_map[0,2])

first_part()

