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


def get_antinode_pair(a_1, a_2, lines):
    x_delt = a_2[0] - a_1[0]
    y_delt = a_2[1] - a_1[1]
    print(f"coords, {a_1}, {a_2}")
    print(f"x_delt {x_delt}, y_delt {y_delt}")


    antinode_1 = [a_1[0] - x_delt, a_1[1] - y_delt]
    antinode_2 = [a_2[0] + x_delt, a_2[1] + y_delt]


    valid_antinodes = []
    print(antinode_1, antinode_2)
    for coord in [antinode_1, antinode_2]:
        if coord_within_range(coord[0], coord[1], lines):
            valid_antinodes.append(coord)

    return valid_antinodes


def get_antinodes(lines, antennas):
    all_antinodes = []
    for key in antennas:
        current_antennas = antennas[key]
        specific_antinodes = []
        for x in range(len(current_antennas)):
            for y in range(len(current_antennas)):
                if x != y:
                    antinode_pair = get_antinode_pair(
                        current_antennas[y],
                        current_antennas[x],
                        lines
                    )
                    for z in antinode_pair:
                        # print(y)
                        if z not in specific_antinodes:
                            specific_antinodes.append(z)
        for x in specific_antinodes:
            if x not in all_antinodes:
                all_antinodes.append(x)
            
    print(all_antinodes)
    return len(all_antinodes)


def main():
    lines = read_file()
    antennas = clean_input(lines)
    answer = get_antinodes(lines, antennas)

    return answer


answer = main()

print(answer)