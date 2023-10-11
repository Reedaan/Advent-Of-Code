data = open("input.txt", "r").readlines()
data = [line.strip(" ") for line in data]
data = [line.strip("\n") for line in data]
data = [line.replace(" ", "") for line in data]

data_sorted = [x.split("x") for x in data]
paper_needed = []
ribbon_needed = []

#First part
def first_part():
    for present in data_sorted:
        l = int(present[0])
        w = int(present[1])
        h = int(present[2])
        present = [int(x) for x in present]
        present.sort()
        present_paper = (2 * l * w) + (2 * w * h) + (2 * h * l) + (int(present[0]) * int(present[1]))
        paper_needed.append(present_paper)
    result = sum(paper_needed)
    return result
#Second part

print(first_part())

def second_part():
    for present in data_sorted:
        l = int(present[0])
        w = int(present[1])
        h = int(present[2])
        present = [int(x) for x in present]
        present.sort()
        present_ribbon = (present[0] * 2) + (present[1] * 2) + (l * w * h)
        ribbon_needed.append(present_ribbon)
    result = sum(ribbon_needed)
    return result

print(second_part())

