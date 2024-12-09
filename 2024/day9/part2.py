def read_file():
    with open("input.csv", encoding="utf-8") as file:
        lines = file.read().split("\n")
        return lines


def clean_input(line):
    transformed_input = []
    id = 0
    input_list = [int(x) for x in list(line)]
    for x in range(len(input_list)):
        if x % 2 == 0:
            for y in range(input_list[x]):
                transformed_input.append(id)
            id += 1
        else:
            for y in range(input_list[x]):
                transformed_input.append('.')
        
    return transformed_input


def get_value_count(line):
    value_count_dict = {}
    for x in range(len(line)):
        if isinstance(line[x], int):
            if line[x] not in value_count_dict:
                value_count_dict[line[x]] = [x]
            else:
                value_count_dict[line[x]].append(x)
    return value_count_dict


def find_required_positions(line, value_count_dict, target_key):
    replacement_list = []
    file_length = len(value_count_dict[target_key])

    for x in range(len(line)):
        if line[x] == '.':
            replacement_list.append(x)

        else:
            if file_length <= len(replacement_list):
                return replacement_list, value_count_dict[target_key]
            if line[x] == target_key:
                return [], []
            else:
                replacement_list = []


def move_files_to_front(input):
    moved_line = input
    value_count_dict = get_value_count(input)

    for x in reversed(value_count_dict.keys()):
        if len(list(value_count_dict)) == 0:
            return moved_line
        replacement_list, last_number_positions = find_required_positions(moved_line, value_count_dict, x)
        for z in range(len(last_number_positions)):
            moved_line[replacement_list[z]] = moved_line[last_number_positions[z]]
            moved_line[last_number_positions[z]] = '.'
    return moved_line


def get_checksum(input):
    total = 0
    for x in range(len(input)):
        if isinstance(input[x], int):
            total += x * input[x]
    return total


def main():
    line = read_file()[0]
    transformed_input = clean_input(line)
    print(transformed_input)
    finalized_line = move_files_to_front(transformed_input)
    print(finalized_line)
    return get_checksum(finalized_line)


answer = main()

print(answer)
