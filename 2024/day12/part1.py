def read_file():
    with open("input.csv", encoding="utf-8") as file:
        lines = [list(x) for x in file.read().split("\n")]
        return lines


def get_letter_coords(graph):
    dict = {}
    for y in range(len(graph)):
        for x in range(len(graph[0])):
            if graph[y][x] in dict.keys():
                dict[graph[y][x]].append([x, y])
            else:
                dict[graph[y][x]] = [[x, y]]
    return dict


def find_garden(connected_plots, coord_list):
    init_connected_plots_length = len(connected_plots)
    for plot in connected_plots:
        x = plot[0]
        y = plot[1]
        for test_coord in coord_list:
            test_x = test_coord[0]
            test_y = test_coord[1]
            if ((x + 1 == test_x and y == test_y) or \
            (x - 1 == test_x and y == test_y) or \
            (x == test_x and y+1 == test_y) or \
            (x == test_x and y-1 == test_y)) and \
            test_coord not in connected_plots:
                connected_plots.append(test_coord)
    if init_connected_plots_length == len(connected_plots):
        return connected_plots
    else:
        find_garden(connected_plots, coord_list)
    return connected_plots

           

def get_unique_gardens(coord_list):
    gardens_dict = {}

    num_found = 0
    all_lists_found = []
    while num_found < len(coord_list)-1:
        for coord in coord_list:
            x = coord[0]
            y = coord[1]
            list_found =  find_garden([[x,y]], coord_list)
            if len(all_lists_found) == 0:
                all_lists_found.append(list_found)
                num_found += len(list_found)
            already_in_list = False
            for z in all_lists_found:
                if sorted(z) == sorted(list_found):
                    already_in_list = True

            if not already_in_list:
                all_lists_found.append(list_found)
                num_found += len(list_found)

    index = 0
    for x in all_lists_found:
        gardens_dict[f"{index}"] = x
        index += 1
    
    return gardens_dict


def check_boundaries(x, y, coord_list):
    num_boundaries = 0
    if [x+1, y] not in coord_list:
        num_boundaries += 1
    if [x-1, y] not in coord_list:
        num_boundaries += 1
    if [x, y+1] not in coord_list:
        num_boundaries += 1
    if [x, y-1] not in coord_list:
        num_boundaries += 1
    return num_boundaries
    

def get_value(gardens_dict):
    total_value = 0
    for key, coord_list in gardens_dict.items():
        area = len(coord_list)
        parimeter = 0
        for coord in coord_list:
            parimeter += check_boundaries(coord[0], coord[1], coord_list)
        # print(f"{area} * {parimeter} = {area * parimeter}")
        total_value += area * parimeter
    return total_value


def decipher_letter_dict(dict):
    total = 0
    for key, coord_list in dict.items():
        unique_gardens = get_unique_gardens(coord_list)
        total += get_value(unique_gardens)
    return total


def main():
    graph = read_file()
    letter_dict = get_letter_coords(graph)
    answer = decipher_letter_dict(letter_dict)
    return answer


answer = main()

print(answer)
