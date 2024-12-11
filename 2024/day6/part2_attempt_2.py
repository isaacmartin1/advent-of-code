
def read_file():
    with open("input.csv", encoding="utf-8") as file:
        lines = file.read().split("\n")
        return lines

movement_dict = {
    'up': [0, -1],
    'down': [0, 1],
    'right': [1, 0],
    'left': [-1, 0]
}


def create_new_lines_object(height, width, lines):
    lines_copy = lines
    lines_copy = f'{lines_copy[height][:width]}{'#'}{lines_copy[height][width+1:]}'

    return lines_copy


def get_distance_in_direction():
    while True:
        


def check_for_infinite_loop(height, width, lines):
    lines_copy = create_new_lines_object(height, width, lines)
    is_infinite = False
    is_end_ahead = False
    current_position = [width, height]
    direction = movement_dict['up']
    while is_infinite == False and is_end_ahead == False:
        distance, is_end_ahead = get_distance_in_direction()
        check_for_infinite_loop()

    return 1
    



def main():
    lines = read_file()

    answer = 0
    for height in range(len(lines)):
        for width in range(len(lines[0])):
            target_value = lines[height][width]
            if target_value == '^' or target_value == '#':
                continue
            answer += check_for_infinite_loop(height, width, lines)


    return answer


answer = main()

print(answer)