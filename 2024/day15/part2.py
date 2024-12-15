def read_file():
    with open("input.csv", encoding="utf-8") as file:
        lines = [line.split() for line in file.read().split("\n")]
        passed_half = False
        map = []
        movements = []
        for line in lines:
            if len(line) == 0:
                passed_half = True
            elif passed_half == False:
                current_line = []
                [current_line.append(char) for char in list(line[0])]
                map.append(current_line)
            else:
                [movements.append(char) for char in list(line[0])]
        part_2_map = []
        for line in map:
            new_line = []
            for char in line:
                if char == '#':
                    new_line.append('#')
                    new_line.append('#')
                elif char == 'O':
                    new_line.append('[')
                    new_line.append(']')
                elif char == '.':
                    new_line.append('.')
                    new_line.append('.')
                elif char == '@':
                    new_line.append('@')
                    new_line.append('.')
            part_2_map.append(new_line)

        return part_2_map, movements


def handle_brackets(connected_objects, map, y_change, target_x, target_y, result):
        connected_objects.append([target_x, target_y])
        checkpoint = map[target_y][target_x]

        if map[target_y+y_change][target_x] == '#':
            return connected_objects, False
        elif map[target_y+y_change][target_x] == '[' or map[target_y+y_change][target_x] == ']':
            connected_objects, result = handle_brackets(connected_objects, map, y_change, target_x, target_y+y_change, result)

        if checkpoint == '[':
            connected_objects.append([target_x+1, target_y])
            if map[target_y+y_change][target_x+1] == '[' or map[target_y+y_change][target_x+1] == ']':
               connected_objects, result = handle_brackets(connected_objects, map, y_change, target_x+1, target_y+y_change, result)
            if map[target_y+y_change][target_x+1] == '#':
                return connected_objects, False

        elif checkpoint == ']':
            connected_objects.append([target_x-1, target_y])
            if map[target_y+y_change][target_x-1] == '[' or map[target_y+y_change][target_x-1] == ']':
                connected_objects, result = handle_brackets(connected_objects, map, y_change, target_x-1, target_y+y_change, result)
            if map[target_y+y_change][target_x-1] == '#':
                return connected_objects, False

        if result != False:
            return connected_objects, True
        else:
            return connected_objects, False


def get_connected_objects(map, x_change, y_change, robot_x, robot_y):
    target_x = robot_x
    target_y = robot_y
    connected_objects = [[robot_x, robot_y]]
    while True:
        target_x += x_change
        target_y += y_change
        checkpoint = map[target_y][target_x]
        if checkpoint == '[' or checkpoint == ']':
            if y_change != 0:
                connected_objects, result = handle_brackets(connected_objects, map, y_change, target_x, target_y, True)
                if result == False:
                    return connected_objects, result
            else:
                connected_objects.append([target_x, target_y])
            # if going up, grab the side character of the robot
            if y_change != 0:
                if checkpoint == '[':
                    connected_objects.append([target_x+1, target_y])
                    if map[target_y+y_change][target_x+1] == '#':
                        return list(reversed(connected_objects)), False
                elif checkpoint == ']':
                    connected_objects.append([target_x-1, target_y])
                    if map[target_y+y_change][target_x-1] == '#':
                        return list(reversed(connected_objects)), False
        elif checkpoint == '#':
            return list(reversed(connected_objects)), False
        elif checkpoint == '.':
            output = []
            for x in list(reversed(connected_objects)):
                if x not in output:
                    output.append(x)
            return output, True



def rearrange_map(map, objects, x_change, y_change):
    if y_change == -1:
        objects = sorted(objects , key=lambda k: [k[1], k[0]])
    elif y_change == 1:
        objects = list(reversed(sorted(objects , key=lambda k: [k[1], k[0]])))
    for object in objects:
        map[object[1] + y_change][object[0] + x_change] = map[object[1]][object[0]]
        map[object[1]][object[0]] = '.'
    return map


def simulate_moves(map, move, robot_x, robot_y):
    if move == '^':
   
        x_change = 0
        y_change = -1
        objects, is_move_valid = get_connected_objects(map, x_change, y_change, robot_x, robot_y)
        if is_move_valid:
            return rearrange_map(map, objects, x_change, y_change)           
   
    elif move == '>':

        x_change = 1
        y_change = 0
        objects, is_move_valid = get_connected_objects(map, x_change, y_change, robot_x, robot_y)
        if is_move_valid:
            return rearrange_map(map, objects, x_change, y_change)

    elif move == '<':

        x_change = -1
        y_change = 0
        objects, is_move_valid = get_connected_objects(map, x_change, y_change, robot_x, robot_y)
        if is_move_valid:
            return rearrange_map(map, objects, x_change, y_change)

    elif move == 'v':

        x_change = 0
        y_change = 1
        objects, is_move_valid = get_connected_objects(map, x_change, y_change, robot_x, robot_y)
        if is_move_valid:
            return rearrange_map(map, objects, x_change, y_change)

    return map


def get_robot_position(map):
    for y in range(len(map)-1):
        for x in range(len(map[0])):
            if map[y][x] == '@':
                return x, y


def get_coord_sum(map):
    total = 0
    for y in range(len(map)-1):
        for x in range(len(map[0])):
            if map[y][x] == '[':
                total += 100*y+x
    return total


def main():
    map, movements = read_file()
    iteration = 0
    for move in movements:
        robot_x, robot_y = get_robot_position(map)
        map = simulate_moves(map, move, robot_x, robot_y)
        iteration += 1

    return get_coord_sum(map)


answer = main()

print(answer)
