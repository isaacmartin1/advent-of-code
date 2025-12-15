def read_file(filename):
    with open(filename, encoding="utf-8") as file:
        lines = file.read().split("\n")
        return lines
    
def main():
    answer = 0
    filename = "input.csv"
    lines = read_file(filename)
    
    shapes_size = {}
    shape_size_index = 0
    octothorpe_count = 0
    required_presents = []
    for line in lines:
        for idx in range(len(line)):
            if line[idx] == '#':
                octothorpe_count += 1

        if line == '' and len(shapes_size.keys()) < 6:
            shapes_size[shape_size_index] = octothorpe_count
            shape_size_index += 1
            octothorpe_count = 0

        if'x' in line:
            dimension, num_of_each_shape = line.split(':')
            num_of_each_shape = [int(x) for x in num_of_each_shape.split()]
            width, length = [int(x) for x in dimension.split('x')]
            required_presents.append([width, length, num_of_each_shape])

    for width, length, num_of_each_shape in required_presents:
        area_available = width * length
        present_area = 0
        for idx in range(len(num_of_each_shape)):
            shape_area = shapes_size[idx]
            num_required = num_of_each_shape[idx]
            present_area += shape_area * num_required
        
        if present_area <= area_available:
            answer += 1

    return answer

answer = main()
print(answer)
