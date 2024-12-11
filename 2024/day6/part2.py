
def read_file():
    with open("input.csv", encoding="utf-8") as file:
        lines = file.read().split("\n")
        return lines


def get_guard_position(lines):
    for x in range(len(lines)):
        for y in range(len(lines[x])):
            if lines[y][x] == '^':
                return x, y

def check_for_collision(guard_x, guard_y, direction, lines):
    if direction == 'up':
        if lines[guard_y-1][guard_x] == '#':
            return True
    elif direction == 'down':
        if lines[guard_y+1][guard_x] == '#':
            return True
    elif direction == 'right':
        if lines[guard_y][guard_x+1] == '#':
            return True
    elif direction == 'left':
        if lines[guard_y][guard_x-1] == '#':
            return True
    return False


def check_for_ending(guard_x, guard_y, direction, lines):
    if direction == 'up' and guard_y-1 < 0:
        return True
    if direction == 'down' and guard_y+1 == len(lines)-1:
        return True
    if direction == 'right' and guard_x+1 == len(lines[0])-1:
        return True
    if direction == 'left' and guard_x-1 < 0:
        return True
    return False

def turn_right(direction):
    if direction == 'up':
        return 'right'
    elif direction == 'right':
        return 'down'
    elif direction == 'down':
        return 'left'
    elif direction == 'left':
        return 'up'

def move_guard(guard_x, guard_y, direction):
    if direction == 'up':
        return guard_x, guard_y-1
    if direction == 'down':
        return guard_x, guard_y+1
    if direction == 'right':
        return guard_x+1, guard_y
    if direction == 'left':
        return guard_x-1, guard_y

def adjust_for_new_location(guard_x, guard_y, direction, location_list):
    if [guard_x, guard_y, direction] not in location_list:
        location_list.append([guard_x, guard_y, direction])
        return location_list, False
    else:
        return location_list, True

def is_guard_loop_infinite(x, y, guard_x, guard_y, lines):
    # start moving up
    lines[y] = lines[y][:x] + '#' + lines[y][x + 1:]
    direction = 'up'
    is_end_ahead = False
    location_list = []
    is_infinite = False
    while (is_infinite == False) and (is_end_ahead != True):
        is_collision_ahead = check_for_collision(guard_x, guard_y, direction, lines)
        if is_collision_ahead:
            direction = turn_right(direction)

        is_end_ahead = check_for_ending(guard_x, guard_y, direction, lines)


        guard_x, guard_y = move_guard(guard_x, guard_y, direction)

        location_list, is_infinite = adjust_for_new_location(guard_x, guard_y, direction, location_list)
    return is_infinite

def create_modded_lines(input_x, input_y, lines):
    new_lines = []
    for x in range(len(lines)):
        new_string = lines[x]
        if x == input_x:
            string_list = list(new_string)
            string_list[input_y] = '#'
            new_string = "".join(string_list)
        new_lines.append(new_string)
    return new_lines



def main():
    lines = read_file()
    answer = 0

    # given: guard is facing up
    guard_x, guard_y = get_guard_position(lines)
    for x in range(len(lines)):
        for y in range(len(lines[x])):
            if x == guard_x and y == guard_y:
                continue
            if lines[y][x] == '#':
                continue
            modded_lines = create_modded_lines(x, y, lines)
            is_infinite = is_guard_loop_infinite(x, y, guard_x, guard_y, modded_lines)
            if is_infinite:
                print('y', x, 'x', y)
                answer += 1


    return answer


answer = main()

print(answer)
