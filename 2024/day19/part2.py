from functools import cache


with open("input.csv", encoding="utf-8") as file:
    lines = [line.split() for line in file.read().split("\n")]
    combinations = []
    patterns_list = []
    passed_half = False
    for line in lines:
        if line == []:
            passed_half = True
        elif passed_half:
            combinations.append(line)
        else:
            patterns_list = [item.replace(',','') for item in line]


@cache
def get_viability(combination):
    if combination == "":
        return 1
    else:
        count = 0
        for pattern in patterns_list:
            if combination.startswith(pattern):
                count += get_viability(combination[len(pattern):])
        return count


def main():
    num_possible = 0
    for combination in combinations:
        num_possible += get_viability(combination[0])
    return num_possible


answer = main()

print(answer)
