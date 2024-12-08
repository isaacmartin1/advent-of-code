from itertools import product

def read_file():
    with open("input.csv", encoding="utf-8") as file:
        lines = file.read().split("\n")
        return lines


def clean_input(lines):
    antennas = {}
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] != '.'and lines[y][x] != '#':
                if lines[y][x] in antennas:
                    antennas[lines[y][x]].append([x, y])
                else:
                    antennas[lines[y][x]] = [[x, y]]
    return antennas


def coord_within_range(x, y, lines):
    if x < 0 or y < 0:
        return False
    elif y > len(lines)-1:
        return False
    elif x > len(lines[0])-1:
        return False
    return True


def get_points_in_direction(x, y, x_delt, y_delt, lines):
    points = []

    valid_point = True
    while valid_point == True:
        new_x = x + x_delt
        new_y = y + y_delt
        if not coord_within_range(new_x, new_y, lines):
            valid_point = False
        else:
            points.append([new_x, new_y])
            x = new_x
            y = new_y

    return points


def get_antinodes_from_antenna_pair(a_1, a_2, lines):
    x_delt = a_2[0] - a_1[0]
    y_delt = a_2[1] - a_1[1]

    antinodes = []
    [antinodes.append(x) for x in (get_points_in_direction(a_1[0], a_1[1], x_delt, y_delt, lines))]
    [antinodes.append(x) for x in (get_points_in_direction(a_2[0], a_2[1], -x_delt, -y_delt, lines))]

    return antinodes


def get_antinodes(lines, antennas):
    all_antinodes = []
    for key in antennas:
        current_antennas = antennas[key]
        specific_antinodes = []
        for x in range(len(current_antennas)):
            for y in range(len(current_antennas)):
                if x != y:
                    antinode_results = get_antinodes_from_antenna_pair(
                        current_antennas[y],
                        current_antennas[x],
                        lines
                    )
                    for z in antinode_results:
                        if z not in specific_antinodes:
                            specific_antinodes.append(z)
        for x in specific_antinodes:
            if x not in all_antinodes:
                all_antinodes.append(x)
    return len(all_antinodes)


def main():
    lines = read_file()
    antennas = clean_input(lines)
    answer = get_antinodes(lines, antennas)

    return answer


answer = main()

print(answer)
