import re
data = open(
    "/home/odinproject/repos/Advent-Of-Code/2023/Day 2/input.txt", "r").readlines()
data = [line.strip(" ") for line in data]
data = [line.strip("\n") for line in data]
data = [line.replace(" ", "") for line in data]
data = [line.split(":") for line in data]


def part_one():
    valid_game_numbers = []
    for game in data:
        game_valid = True
        game_number = re.findall("\d+", game[0])
        game_number = game_number[0]
        cube_number = game[1]
        cube_rounds = cube_number.split(";")
        for round in cube_rounds:
            starting_cube = {
                "red_cube": 12,
                "green_cube": 13,
                "blue_cube": 14
            }
            round_info = round.split(",")
            for entry in range(len(round_info)):
                number = re.findall("\d+", round_info[entry])
                number = int(number[0])
                text = re.sub(r'\d+', '', round_info[entry])
                if text == "blue":
                    starting_cube.update(
                        {"blue_cube": (starting_cube["blue_cube"] - number)})
                elif text == "red":
                    starting_cube.update(
                        {"red_cube": (starting_cube["red_cube"] - number)})
                elif text == "green":
                    starting_cube.update(
                        {"green_cube": (starting_cube["green_cube"] - number)})
            if all(value >= 0 for value in starting_cube.values()):
                continue
            else:
                game_valid = False
                break
        if game_valid:
            valid_game_numbers.append(game_number)
    valid_game_numbers = [int(x) for x in valid_game_numbers]
    return sum(valid_game_numbers)


def part_two():
    sum = 0
    for game in data:
        starting_cube = {
            "red_cube": 0,
            "green_cube": 0,
            "blue_cube": 0
        }
        game_number = re.findall("\d+", game[0])
        game_number = game_number[0]
        cube_number = game[1]
        cube_rounds = cube_number.split(";")
        for round in cube_rounds:
            round_info = round.split(",")
            for entry in range(len(round_info)):
                number = re.findall("\d+", round_info[entry])
                number = int(number[0])
                text = re.sub(r'\d+', '', round_info[entry])
                if text == "blue":
                    if number > starting_cube["blue_cube"]:
                        starting_cube.update(
                            {"blue_cube": number})
                elif text == "red":
                    if number > starting_cube["red_cube"]:
                        starting_cube.update(
                            {"red_cube": number})
                elif text == "green":
                    if number > starting_cube["green_cube"]:
                        starting_cube.update(
                            {"green_cube": number})
        bag_value = starting_cube["red_cube"] * \
            starting_cube["green_cube"] * starting_cube["blue_cube"]
        sum += bag_value
    return sum


print(part_one())
print(part_two())
