def read_file(filename):
    with open(filename, encoding="utf-8") as file:
        lines = [line.split(',') for line in file.read().split("\n")]
        return lines
    
def main():
    filename = "input.csv"
    lines = read_file(filename)

    list_of_coords = []

    for line in lines:
        x_coord, y_coord = [int(x) for x in line]
        list_of_coords.append([x_coord, y_coord])

    largest_area = 0
    for x_coord_1, y_coord_1 in list_of_coords:
        for x_coord_2, y_coord_2 in list_of_coords:
            area = (abs(x_coord_1 - x_coord_2) + 1) * (abs(y_coord_1 - y_coord_2) + 1)
            if area > largest_area:
                largest_area = area

    return largest_area

answer = main()
print(answer)
