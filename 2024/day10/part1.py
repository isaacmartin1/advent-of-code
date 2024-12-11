
def read_file():
    with open("input.csv", encoding="utf-8") as file:
        lines = file.read().split("\n")
        return lines


def clean_lines(lines):
    lines = [list(x) for x in lines]
    int_lines = []
    for x in lines:
        int_lines.append([int(y) if y != '.' else 100 for y in x])
    return int_lines


def find_all_trails(y, x, lines, target_number, terminal_list):
    for [x, y] in [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]:
        if 0 <= x < len(lines[0]) and 0 <= y < len(lines):
            if lines[y][x] == target_number:
                if target_number == 9 and [x, y] not in terminal_list:
                    terminal_list.append([x, y])
                    print(f"terminal at x: {x} y: {y}")
                terminal_list = find_all_trails(y, x, lines, target_number+1, terminal_list)

    return terminal_list


def main():
    lines = read_file()
    lines = clean_lines(lines)
    answer = 0

    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == 0:
                paths_found = len(find_all_trails(y, x, lines, 1, []))
                print(f"{paths_found} paths found at x: {x}, y: {y}")
                answer += paths_found

    [print(x) for x in lines]

    return answer


answer = main()

print(answer)
