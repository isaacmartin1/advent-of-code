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

    # get a list of largest area and assoc coords
    largest_area = 0
    biggest_areas = []
    largest_x = 0
    largest_y = 0
    for x_coord_1, y_coord_1 in list_of_coords:
        for x_coord_2, y_coord_2 in list_of_coords:
            area = (abs(x_coord_1 - x_coord_2) + 1) * (abs(y_coord_1 - y_coord_2) + 1)
            biggest_areas.append([area, [[x_coord_1, y_coord_1], [x_coord_2, y_coord_2]]])
            if x_coord_1 > largest_x:
                largest_x = x_coord_1
            if y_coord_1 > largest_y:
                largest_y = y_coord_1

    biggest_areas.sort(reverse=True)


    perimeter = []

    for idx in range(len(list_of_coords)):
        if idx != len(list_of_coords) - 1:
            current_x, current_y = list_of_coords[idx]
            next_x, next_y = list_of_coords[idx + 1]
        else:
            current_x, current_y = list_of_coords[idx]
            next_x, next_y = list_of_coords[0]
        larger_x, smaller_x = max(current_x, next_x), min(current_x, next_x)
        larger_y, smaller_y = max(current_y, next_y), min(current_y, next_y)
        x_diff = larger_x - smaller_x
        y_diff = larger_y - smaller_y
        perimeter.append([current_x, current_y])
        if y_diff > 0:
            for new_y in range(y_diff):
                perimeter.append([smaller_x, new_y + smaller_y])
        elif x_diff > 0:
            for new_x in range(x_diff):
                perimeter.append([new_x + smaller_x, smaller_y])
    
    for area, [[x_coord_1, y_coord_1], [x_coord_2, y_coord_2]] in biggest_areas:
        is_found = True
        larger_x, smaller_x = max(x_coord_1, x_coord_2), min(x_coord_1, x_coord_2)
        larger_y, smaller_y = max(y_coord_1, y_coord_2), min(y_coord_1, y_coord_2)

        monitored_values = []
        for x_coord, y_coord in perimeter:

            if (x_coord == x_coord_1 and y_coord == y_coord_1) or (x_coord == x_coord_2 and y_coord == y_coord_2):
                continue
            elif smaller_x < x_coord < larger_x and smaller_y < y_coord < larger_y:
                is_found = False
                monitored_values.append([x_coord, y_coord])

        if is_found == True:
            largest_area = area
            break


    return largest_area

answer = main()

print(answer)
