def read_file():
    with open("input.csv", encoding="utf-8") as file:
        lines = file.read().split("\n")
        return lines


def clean_line(line):
    line = line.split()
    new_line = []
    for x in line:
        new_line.append(int(x))
    return new_line


def get_direction(line):
    first = line[0]
    second = line[1]
    if first < second:
        return 'Increasing'
    elif first > second:
        return 'Decreasing'
    else:
        return 'Static'


def compare_vals(prev, current, direction):
    dif = abs(prev-current)
    if dif < 1 or dif > 3:
        return False
    if prev < current and direction == 'Decreasing':
        return False
    if prev > current and direction == 'Increasing':
        return False
    if dif == 0:
        return False
    return True

def remove_index(coord, line):
    new_line = []
    length = len(line)
    for x in range(length):
        if x != coord:
            new_line.append(line[x])
    return new_line

def attempt_line(line):
    prev = 0
    length_value = len(line)
    
    direction = get_direction(line)
    if direction == 'Static':
        return False

    for x in range(length_value):
        current = line[x]
        if x == 0:
            prev = current
        else:
            result = compare_vals(prev, current, direction)
            if result == False:
                return False
            prev = current

    return True


def evaluate_line(line):
    result = attempt_line(line)
    if result:
        return True

    for i in range(len(line)):
        modified_line = remove_index(i, line)
        result = attempt_line(modified_line)
        if result:
            return True

    return False


def main():
    lines = read_file()
    answer = 0
    for line in lines:
        line = clean_line(line)
        is_line_valid = evaluate_line(line)
        if is_line_valid == True:
            print(line)
            answer += 1


    return answer

answer = main()

print(answer)