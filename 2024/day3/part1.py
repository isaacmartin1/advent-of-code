import re

def read_file():
    with open("input.csv", encoding="utf-8") as file:
        lines = file.read().split("\n")
        return lines

def detect_all_mul(line):
    x = re.findall("mul\([0-9]+,[0-9]+\)", line)
    print(x)
    return(x)

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
    for line in lines:
        raw_mult = detect_all_mul(line)
        mult_result = decode_mult(raw_mult)
        answer += mult_result

    return answer


answer = main()

print(answer)