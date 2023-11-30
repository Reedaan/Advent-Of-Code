data = open("/home/odinproject/repos/Advent-Of-Code/2015/Day 5/input.txt", "r").readlines()
data = [line.strip(" ") for line in data]
data = [line.strip("\n") for line in data]
data = [line.replace(" ", "") for line in data]

print(data)
nice_strings = []

#Part one
#Nice string of letters is a string that:
#At least 3 vowels (aeiou) [done]
#At least one letter that appears twice in a row example ->(xx)
#DOESNT contain the strings "ab" | "cd" | "pq" | "xy" [done]

# def part_one():
#     for line in data:
#         #Check if the string doesnt contain "ab" | "cd" | "pq" | "xy"
#         if "ab" in line or "cd" in line or "pq" in line or "xy" in line:
#             pass
#         else:
#             #Count the vowels in string
#             vowel_count = 0
#             for letter in range(len(line)):
#                 if "a" == line[letter] or "e" == line[letter] or "i" == line[letter] or "o" == line[letter] or "u" == line[letter]:
#                     vowel_count += 1
#             if vowel_count >= 3:
#                 #Check if any letter appears twice in a row
#                 for index, letter in enumerate(line):
#                     try:
#                         if line[index + 1] == letter:
#                             nice_strings.append(line)
#                             break
#                     except IndexError:
#                         pass
#     return len(nice_strings)

# print(part_one())

#Part two
#Pair of two letters that appear at least twice (without overlapping)
#Contains at least one letter, which repeats with exactly one letter between them (xyx, efe) [done]

def part_two():
    for line in data:
        repeated = False
        for index, letter in enumerate(line):
            #At least one letter which repeats with exactly one between them
            try:
                if line[index + 2] == letter:
                    repeated = True
            except IndexError:
                pass
        if repeated:
            
        
            
                


print(part_two())
