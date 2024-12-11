import time
start = time.perf_counter()


def read_file():
    with open("input.csv", encoding="utf-8") as file:
        lines = file.read().split("\n")
        return lines


def apply_rules(line):
    transformed_line = []
    for x in line:
        int_x = int(x)
        len_x = len(x)
        if int_x == 0:
            transformed_line.append(str(1))
        elif len_x % 2 == 0:
            transformed_line.append(str(int(x[:len_x//2])))
            transformed_line.append(str(int(x[len_x//2:])))
        else:
            transformed_line.append(str(int_x*2024))
    return transformed_line


def main():
    line = read_file()[0].split()
    answer = 0
    i = 0
    for x in line:
        x = [x]
        while i < 25:
            x = apply_rules(x)
            print(f'processing {i}')
            i += 1
        i = 0
        print(x)
        answer += len(x)
    return answer


answer = main()

print(answer)

end = time.perf_counter()
print(end - start)