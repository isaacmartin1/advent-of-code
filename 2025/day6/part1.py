import numpy as np


def read_file(filename):
    with open(filename, encoding="utf-8") as file:
        numbers = np.empty(0)
        operations = None
        for line in file.read().split("\n"):
            line = line.split()
            new_row = np.empty(0)
            for item in line:
                new_row = np.append(new_row, item)
            if '+' in line or '*' in line:
                operations = new_row
            else:
                # numpy operation
                # prepare new row
                if len(numbers) == 0:
                    # initialize it
                    numbers = new_row
                else:
                    # add to it
                    numbers = np.vstack((numbers, new_row))
            
        return numbers, operations
    
def main():
    answer = 0
    filename = "input.csv"
    numbers, operations = read_file(filename)
    addition = '+'
    multiplucation = '*'

    for idx in range(len(operations)):
        operator = operations[idx]
        column_result = None
        if operator == addition:
            column_result = 0
            for n in numbers[:,idx]:
                column_result += int(n)
        elif operator == multiplucation:
            for n in numbers[:,idx]:
                if column_result is None:
                    column_result = int(n)
                else:
                    column_result *= int(n)
        answer += column_result
                
    import pdb
    pdb.set_trace()
    return answer

answer = main()
print(answer)
