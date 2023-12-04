import re
import timeit

data = open("/home/redan/repos/Advent-Of-Code/2023/Day 1/input.txt", "r").readlines()
data = [line.strip(" ") for line in data]
data = [line.strip("\n") for line in data]
data = [line.replace(" ", "") for line in data]

def first_part():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    number_list = []
    for line in data:
        first_number = 0
        second_number = 0
        for letter in line:
            try:
                if int(letter) in numbers:
                    first_number = letter
                    break
            except ValueError:
                pass
        for letter in line[::-1]:
            try:
                if int(letter) in numbers:
                    second_number = letter
                    break
            except ValueError:
                pass
        number_list.append(first_number + second_number)
    number_list_int = [int(x) for x in number_list]
    return sum(number_list_int)

def replace_string_with_number(word):
    if word == "one":
        return 1
    elif word == "two":
        return 2
    elif word == "three":
        return 3
    elif word == "four":
        return 4
    elif word == "five":
        return 5
    elif word == "six":
        return 6
    elif word == "seven":
        return 7
    elif word == "eight":
        return 8
    elif word == "nine":
        return 9



def second_part():
    start = timeit.default_timer()
    sum = 0
    for line in data:
        pattern = re.compile(r"(?=(one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9))")
        matches = pattern.findall(line)
        if matches[0].isdigit():
            sum += int(matches[0]) * 10
        else:
            sum += replace_string_with_number(matches[0]) * 10
        if matches[-1].isdigit():
            sum += int(matches[-1])
        else:
            sum += replace_string_with_number(matches[-1]) 
            
    stop = timeit.default_timer()
    print('Time: ', stop - start)
    return sum


        
    
    # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # first_number = 0
    # second_number = 0
    # number_list = []
    # for line in sorted_data:
    #     for letter in line:
    #         try:
    #             if int(letter) in numbers:
    #                 first_number = letter
    #                 break
    #         except ValueError:
    #             pass
    #     for letter in line[::-1]:
    #         try:
    #             if int(letter) in numbers:
    #                 second_number = letter
    #                 break
    #         except ValueError:
    #             pass
    #     number_list.append(first_number + second_number)
    # number_list_int = [int(x) for x in number_list]
    
    # return sum(number_list_int)

# print(first_part())
print(second_part())





