def read_file(filename):
    with open(filename, encoding="utf-8") as file:
        lines = [line for line in file.read().split("\n")]
        return lines
    
def main():
    answer = 0
    filename = "input.csv"
    paper = '@'
    lines = read_file(filename)
    for y in range(len(lines)):
        line = lines[y]
        for x in range(len(line)):
            if line[x] == paper:
                # check if its valid
                surrounding_papers = 0
                for x_dir in [-1, 0, 1]:
                    for y_dir in [-1, 0, 1]:
                        if x_dir == 0 and y_dir == 0:
                            continue
                        proposed_x = x + x_dir
                        proposed_y = y + y_dir
                        if proposed_x < 0 or proposed_y < 0:
                            continue
                        elif proposed_y >= len(lines) or proposed_x >= len(line):
                            continue
                        elif lines[proposed_y][proposed_x] == '@':
                            surrounding_papers += 1
                print('x', x, 'y', y, 'surrounding papers', surrounding_papers)
                if surrounding_papers < 4:
                    answer += 1

    return answer

answer = main()
print(answer)
