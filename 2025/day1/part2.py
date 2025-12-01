def read_file(filename):
    with open(filename, encoding="utf-8") as file:
        lines = [line.split()[0] for line in file.read().split("\n")]
        return lines
    
def main():
    position = 50
    zero_dial_position_count = 0
    maximum_value = 100
    lines = read_file('input.csv')
    print(lines)
    for line in lines:
        direction = line[0]
        distance_turned = int(line[1:])
        raw_new_position = None
        starting_position = position
        if direction == 'R':
            raw_new_position = position + distance_turned
            position = (distance_turned + position) % maximum_value

        elif direction == 'L':
            raw_new_position = position - distance_turned
            position = abs((position - distance_turned) % maximum_value)

        for p in range(min(raw_new_position, starting_position)+1, max(raw_new_position, starting_position)):
            if p == 0:
                zero_dial_position_count += 1

            elif p % maximum_value == 0:
                zero_dial_position_count += 1
        
        if position == 0:
            zero_dial_position_count += 1

    return zero_dial_position_count


answer = main()
print(answer)
