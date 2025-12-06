import numpy as np

def read_file(filename):
    with open(filename, encoding="utf-8") as file:
        numbers = []
        operations = None
        for line in file.read().split("\n"):
            if '+' in line or '*' in line:
                operations = line
            else:
                numbers.append(line)
        return numbers, operations
    
def main():
    answer = 0
    filename = "input.csv"
    numbers, operations = read_file(filename)
    addition = '+'
    multiplucation = '*'
    row_indexes = []
    for idx in reversed(range(len(operations))):
        operator = operations[idx]
        row_indexes.append(idx)
        if operator is '*' or operator is '+':
            values = []
            for row in row_indexes:
                column_number = ''
                for column in range(len(numbers)):
                    proposed_addition = numbers[column][row]
                    if proposed_addition is not ' ':
                        column_number += numbers[column][row]
                print(column_number)
                if column_number is not '':
                    values.append(int(column_number))
            

            column_result = None
            if operator == addition:
                column_result = 0
                # add
                for v in values:
                    column_result += v
            elif operator == multiplucation:
                # multiply
                for v in values:
                    if column_result is None:
                        column_result = v
                    else:
                        column_result *= v
            answer += column_result
            row_indexes = []

    return answer

answer = main()
print(answer)
