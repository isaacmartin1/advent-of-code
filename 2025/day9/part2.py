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

    # get a list of largest area and associated coords
    biggest_areas = []
    for x_coord_1, y_coord_1 in list_of_coords:
        for x_coord_2, y_coord_2 in list_of_coords:
            area = (abs(x_coord_1 - x_coord_2) + 1) * (abs(y_coord_1 - y_coord_2) + 1)
            biggest_areas.append([area, [[x_coord_1, y_coord_1], [x_coord_2, y_coord_2]]])

    biggest_areas.sort(reverse=True)
    
    for area, [[x_coord_1, y_coord_1], [x_coord_2, y_coord_2]] in biggest_areas:
        is_found = True
        larger_x, smaller_x = max(x_coord_1, x_coord_2), min(x_coord_1, x_coord_2)
        larger_y, smaller_y = max(y_coord_1, y_coord_2), min(y_coord_1, y_coord_2)

        for idx in range(len(list_of_coords)):
            current_x, current_y = list_of_coords[idx]
            next_x, next_y = list_of_coords[0] if idx + 1 == len(list_of_coords) else list_of_coords[idx + 1]

            # VERTICAL LINE
            if abs(next_y - current_y) > 0:
                y_perimeter_min, y_perimeter_max = [next_y, current_y] if next_y < current_y else [current_y, next_y]
                if smaller_x < current_x < larger_x:
                    if y_perimeter_min < larger_y < y_perimeter_max or y_perimeter_min < smaller_y < y_perimeter_max:
                        is_found = False
                        break
                    elif smaller_y < y_perimeter_min < larger_y or smaller_y < y_perimeter_max < larger_y:
                        is_found = False
                        break
                    elif smaller_y == y_perimeter_min or larger_y == y_perimeter_max:
                        is_found = False
                        break

            # HORIZONTAL LINE
            elif abs(next_x - current_x) > 0:
                x_perimeter_min, x_perimeter_max = [next_x, current_x] if next_x < current_x else [current_x, next_x]
                import pdb
                if smaller_y < current_y < larger_y:
                    if x_perimeter_min < larger_x < x_perimeter_max or x_perimeter_min < smaller_x < x_perimeter_max:
                        is_found = False
                        break
                    elif smaller_x < x_perimeter_min < larger_x or smaller_x < x_perimeter_max < larger_x:
                        is_found = False
                        break
                    elif smaller_x == x_perimeter_min or larger_x == x_perimeter_max:
                        is_found = False
                        break

        if is_found == True:
            largest_area = area
            break

    return largest_area

answer = main()
print(answer)
