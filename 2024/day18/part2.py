# breadth first search with binary search adjustment of fallen lines to arrive at answer
def read_file():
    with open("input.csv", encoding="utf-8") as file:
        lines = [line.split() for line in file.read().split("\n")]
        separated_lines = []
        for line in lines:
            x, y = (int(item) for item in line[0].split(','))
            separated_lines.append([x, y])
        return separated_lines


def get_start(lines):
    S = None
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == 'S':
                S = [x, y]
    return S


def get_shortest_path(lines, S, max):
    visited = set()
    queue = [[S]]
    visited.add(tuple(S))

    while queue:
        path = queue.pop(0)
        x, y = path[-1]
        for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:
            new_y = y + dy
            new_x = x + dx
            if 0 <= new_x < len(lines[0]) and 0 <= new_y < len(lines):
                if (new_x, new_y) in visited:
                    continue
                elif new_y == max and new_x == max:
                    return path + [[new_x, new_y]]
                elif lines[new_y][new_x] == '.':
                    visited.add((new_x, new_y))
                    queue.append(path + [[new_x, new_y]])

    return []

def get_grid(lines, min, max, number_fallen):
    grid = []
    fallen_lines = lines[:number_fallen]
    print(fallen_lines)
    for y in range(min, max+1):
        grid_line = []
        for x in range(min, max+1):
            if [x, y] in fallen_lines:
                grid_line.append('#')
            else:
                grid_line.append('.')
        grid.append(grid_line)
    return grid



def main():
    lines = read_file()
    number_fallen = 3033
    grid_length = 70
    grid = get_grid(lines, 0, grid_length, number_fallen)
    path = get_shortest_path(grid, [0,0], grid_length)
    
    return len(path)-1


answer = main()

print(answer)
