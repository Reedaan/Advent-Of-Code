data = open("/home/odinproject/repos/Advent-Of-Code/2023/Day 1/input.txt", "r").readlines()
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
        return "1"
    elif word == "two":
        return "2"
    elif word == "three":
        return "3"
    elif word == "four":
        return "4"
    elif word == "five":
        return "5"
    elif word == "six":
        return "6"
    elif word == "seven":
        return "7"
    elif word == "eight":
        return "8"
    elif word == "nine":
        return "9"


def second_part():
    number_strings = ["one", "two", "eight", "seven", "three", "nine", "five", "four", "six"]
    number_strings.sort(key=len, reverse=True)
    
    for line in data:
        for word in number_strings:
            index = input_string.find(word)
            if index != -1:
                input_string = input_string[:index] + replace_string_with_number(word) + input_string[index + len(word):]

    print(input_string)

    # for line in data:
    #     for index in range(len(number_strings)):
    #         if number_strings[index] in line:
    #             line = line.replace(number_strings[index], replace_string_with_number(number_strings[index]))
    #     sorted_data.append(line)
    # print(sorted_data)
                
    
    
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
    #     print(first_number, second_number)
    # number_list_int = [int(x) for x in number_list]
    # return sum(number_list_int)

    
                    

                


# print(first_part())
second_part()



