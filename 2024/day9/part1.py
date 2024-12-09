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


def find_last_number_position(line):
    reversed_line = line[::-1]
    for x in range(len(reversed_line)):
        if isinstance(reversed_line[x], int):
            return len(line) - 1 - x


def get_completion_status(line):
    str_already_found = False
    for x in line:
        if isinstance(x, str):
            str_already_found = True
        if str_already_found and isinstance(x, int):
            return False
        
    return True


def move_files_to_front(input):
    moved_line = input

    for x in range(len(moved_line)):
        if moved_line[x] == '.':
            if get_completion_status(moved_line):
                return moved_line
            last_number_position = find_last_number_position(moved_line)
            moved_line[x] = moved_line[last_number_position]
            del moved_line[last_number_position]
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

    finalized_line = move_files_to_front(transformed_input)

    return get_checksum(finalized_line)


answer = main()

print(answer)