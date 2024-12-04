
def read_file():
    with open("input.csv", encoding="utf-8") as file:
        lines = file.read().split("\n")
        return lines


def is_valid_coord(coord, maximum):
    if coord < 0 or coord > maximum:
        return False
    return True


def find_all_paths(x, y, lines, length, width):
    total_count = 0
    for x_diff in range(-1, 2):
        for y_diff in range(-1, 2):
            m_y = y - y_diff
            m_x = x - x_diff
            if not is_valid_coord(m_y, length):
                continue
            if not is_valid_coord(m_x, width):
                continue
            if lines[m_y][m_x] == 'M':
                    a_success, a_x, a_y = find_specific_direction(lines, 'A', x, y, m_x, m_y, length, width)
                    if a_success == True:
                        s_success, s_x, s_y = find_specific_direction(lines, 'S', m_x, m_y, a_x, a_y, length, width)
                        if s_success == True:
                            print(f"x: {x}, {y}")
                            total_count += 1
    return total_count


def find_specific_direction(lines, target, x, y, recent_x, recent_y, length, width):
    x_velocity = recent_x - x
    y_velocity = recent_y - y
    current_y = recent_y + y_velocity
    current_x = recent_x + x_velocity

    if not is_valid_coord(current_y, length):
        return False, None, None
    if not is_valid_coord(current_x, width):
        return False, None, None
    if lines[current_y][current_x] == target:
        return True, current_x, current_y
    else:
        return False, current_x, current_y


def find_xmas(lines):
    xmas_count = 0
    length = len(lines)-1
    width = len(lines[0])-1

    for y in range(len(lines)):
        line = lines[y]
        for x in range(len(line)):
            letter = line[x]
            if letter == 'X':
                result = find_all_paths(x, y, lines, length, width)
                xmas_count += result
    return xmas_count


def main():
    lines = read_file()

    xmas_count = find_xmas(lines)

    return xmas_count


answer = main()

print(answer)