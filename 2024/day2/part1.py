def read_file():
    with open("input.csv", encoding="utf-8") as file:
        lines = file.read().split("\n")
        return lines


def get_direction(line):
    first = int(line[0])
    second = int(line[1])
    if first < second:
        return 'Increasing'
    elif first > second:
        return 'Decreasing'
    else:
        return 'Static'

def evaluate_line(line):
    target_array = line.split()
    
    prev = 0
    length_value = len(target_array)

    direction = get_direction(target_array)

    if direction == 'Static':
        return False

    for x in range(length_value):
        current = int(target_array[x])
        if x == 0:
            prev = current
        else:
            result = compare_vals(prev, current, direction)
            if result == False:
                return False
            prev = current
    return True

def compare_vals(prev, current, direction):
    dif = abs(prev-current)
    if dif < 1 or dif > 3:
        print('returned here', dif)
        return False
    if prev <= current and direction == 'Decreasing':
        return False
    if prev >= current and direction == 'Increasing':
        return False
    

def main():
    lines = read_file()

    answer = 0
    for line in lines:
        is_line_valid = evaluate_line(line)
        if is_line_valid:
            answer += 1


    return answer


answer = main()

print(answer)