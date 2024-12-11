
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
            print('collision')
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
        print('true found', guard_y+1, len(lines)-1)
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

def adjust_for_new_location(guard_x, guard_y, location_list):
    if [guard_x, guard_y] not in location_list:
        location_list.append([guard_x, guard_y])
    return location_list

def get_guard_route(guard_x, guard_y, lines):
    # start moving up
    direction = 'up'
    is_end_ahead = False
    location_list = []
    lines[guard_y] = lines[guard_y][:guard_x] + 'X' + lines[guard_y][guard_x + 1:]
    while is_end_ahead != True:
        is_collision_ahead = check_for_collision(guard_x, guard_y, direction, lines)
        if is_collision_ahead:
            direction = turn_right(direction)
        is_end_ahead = check_for_ending(guard_x, guard_y, direction, lines)

        print(guard_x, guard_y, direction)

        guard_x, guard_y = move_guard(guard_x, guard_y, direction)
        lines[guard_y] = lines[guard_y][:guard_x] + 'X' + lines[guard_y][guard_x + 1:]
        location_list = adjust_for_new_location(guard_x, guard_y, location_list)


    return len(location_list)


def main():
    lines = read_file()
    answer = 0

    # given: guard is facing up
    guard_x, guard_y = get_guard_position(lines)
    total = get_guard_route(guard_x, guard_y, lines)
    answer = total


    return answer


answer = main()

print(answer)