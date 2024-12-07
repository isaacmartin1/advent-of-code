import math
from itertools import product

def read_file():
    with open("input.csv", encoding="utf-8") as file:
        lines = file.read().split("\n")
        return lines


def clean_input(lines):
    cleaned_lines = []
    for x in lines:
        initial_split = x.split(':')
        left_side = int(initial_split[0])
        right_side = [int(y) for y in initial_split[1].split(' ')[1:]]
        cleaned_lines.append([left_side, right_side])
    return cleaned_lines


def get_result(test_numbers, ops):
    total = 0
    for x in range(len(test_numbers)):
        if x == 0:
            total += test_numbers[x]
        elif ops[x-1] == '*':
            total *= test_numbers[x]
        elif ops[x-1] == '+':
            total += test_numbers[x]
        elif ops[x-1] == '|':
            total = int(str(total)+str(test_numbers[x]))
    return total


def check_validity(test_value, test_numbers):
    for ops in product("|+*", repeat=len(test_numbers)-1):
        if test_value == get_result(test_numbers, ops):
            return True
    return False


def main():
    lines = read_file()
    answer = 0
    cleaned_lines = clean_input(lines)
    print(cleaned_lines)
    for line in cleaned_lines:
        test_value = line[0]
        test_numbers = line[1]
        if check_validity(test_value, test_numbers):
            answer += test_value

    return answer


answer = main()

print(answer)