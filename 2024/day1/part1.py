def read_file():
    with open("input.csv", encoding="utf-8") as file:
        lines = file.read().split("\n")
        return lines

def transform_to_numbers(input_list):
    return list(map(int, input_list))

def create_lists(lines):
    left_list = []
    right_list = []
    for x in lines:
        items = x.split()
        left_list.append(int(items[0]))
        right_list.append(int(items[1]))
    left_list.sort()
    right_list.sort()
    return left_list, right_list

def main():
    lines = read_file()

    left_list, right_list = create_lists(lines)

    total_distance = 0
    total_length = len(left_list)
    for x in range(total_length):
        left_list_val = left_list[x]
        right_list_val = right_list[x]
        total_distance += abs(left_list_val-right_list_val)
    return total_distance
            

distance = main()

print(distance)