import re

def read_file():
    with open("input.csv", encoding="utf-8") as file:
        lines = file.read().split("\n")
        return lines


def filter_valid_mul(input, do_value):
    valid_mul_list = []
    for x in input:
        if x == "do()":
            do_value = True
        elif x == "don\'t()":
            do_value = False
        else:
            if do_value == True:
                valid_mul_list.append(x)
    return valid_mul_list, do_value


def detect_valid_mul(line, do_value):
    x = re.findall("mul\([0-9]+,[0-9]+\)|don\'t\(\)|do\(\)", line)
    return filter_valid_mul(x, do_value)


def decode_mult(raw_mult):
    total = 0
    for m in raw_mult:
        split_m = m.split(',')
        split_m = [re.findall("[0-9]+", x) for x in split_m]
        split_m = [int(x[0]) for x in split_m]
        total += split_m[0] * split_m[1]
        print(split_m)
    return total


def main():
    lines = read_file()

    answer = 0
    do_value = True
    for line in lines:
        raw_mult, do_value = detect_valid_mul(line, do_value)
        mult_result = decode_mult(raw_mult)
        answer += mult_result

    return answer


answer = main()

print(answer)