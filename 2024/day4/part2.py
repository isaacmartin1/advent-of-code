
def read_file():
    with open("input.csv", encoding="utf-8") as file:
        lines = file.read().split("\n")
        return lines


def is_valid_coord(coord, maximum):
    if coord < 0 or coord > maximum:
        return False
    return True


def validate_x_mas(x, y, lines, length, width):
    right_slant = ['M', 'S']
    left_slant = ['M', 'S']
    for y_diff in [-1, 1]:
        for x_diff in [-1, 1]:
            current_x = x+x_diff
            current_y = y+y_diff
            if not is_valid_coord(current_y, length):
                return 0
            if not is_valid_coord(current_x, width):
                return 0
            if lines[current_y][current_x] in right_slant and abs(x_diff + y_diff) == 2:
                right_slant.remove(lines[current_y][current_x])
            if lines[current_y][current_x] in left_slant and abs(x_diff + y_diff) == 0:
                left_slant.remove(lines[current_y][current_x])
            if len(right_slant) == 0 and len(left_slant) == 0:
                print(f"x: {x}, y: {y}")
                return 1

    return 0


def find_xmas(lines):
    xmas_count = 0
    length = len(lines)-1
    width = len(lines[0])-1

    for y in range(len(lines)):
        line = lines[y]
        for x in range(len(line)):
            letter = line[x]
            if letter == 'A':
                result = validate_x_mas(x, y, lines, length, width)
                xmas_count += result
    return xmas_count


def main():
    lines = read_file()
    xmas_count = find_xmas(lines)
    return xmas_count


answer = main()

print(answer)