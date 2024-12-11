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
    i = 0
    while i < 75:
        line = apply_rules(line)
        print(f'processing {i}')
        i += 1
    return len(line)


answer = main()

print(answer)

end = time.perf_counter()
print(end - start)