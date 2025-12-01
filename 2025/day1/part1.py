def read_file(filename):
    with open(filename, encoding="utf-8") as file:
        lines = [line.split()[0] for line in file.read().split("\n")]
        return lines
    
def main():
    answer = None
    position = 50
    zero_dial_position_count = 0
    maximum_value = 100
    lines = read_file('input.csv')
    print(lines)
    for line in lines:
        direction = line[0]
        distance_turned = int(line[1:])
        if direction == 'R':
            position = (distance_turned + position) % maximum_value
        elif direction == 'L':
            position = abs((position - distance_turned) % maximum_value)
        
        if position == 0:
            zero_dial_position_count += 1

    return zero_dial_position_count


answer = main()
print(answer)
