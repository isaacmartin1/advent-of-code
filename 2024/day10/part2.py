
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


def find_all_trails(y, x, lines, target_number, terminal_dict):
    for [x, y] in [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]:
        if 0 <= x < len(lines[0]) and 0 <= y < len(lines):
            if lines[y][x] == target_number:
                if target_number == 9:
                    if f"{x}, {y}" in terminal_dict.keys():
                        terminal_dict[f"{x}, {y}"] = terminal_dict.get(f"{x}, {y}") + 1
                    else:
                        terminal_dict[f"{x}, {y}"] = 1
                terminal_dict = find_all_trails(y, x, lines, target_number+1, terminal_dict)

    return terminal_dict


def extract_value(terminal_dict):
    total = 0
    for x in terminal_dict:
        total += terminal_dict.get(x)
    return total


def main():
    lines = read_file()
    lines = clean_lines(lines)
    answer = 0

    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == 0:
                terminal_dict = find_all_trails(y, x, lines, 1, {})                
                answer += extract_value(terminal_dict)

    return answer


answer = main()

print(answer)