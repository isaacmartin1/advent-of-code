def read_file(filename):
    with open(filename, encoding="utf-8") as file:
        lines = [line.split()[0] for line in file.read().split("\n")]
        return lines
    
def main():
    answer = 0
    filename = "input.csv"
    passwords = read_file(filename)[0].split(',')
    for p in passwords:
        min, max = p.split('-')
        min, max = int(min), int(max)

        # max + 1 because range is [inclusive, exclusive)
        for code in range(min, max + 1):
            code = str(code)
            first_half = code[len(code)//2:]
            second_half = code[:len(code)//2]
            if first_half == second_half and first_half[0] != '0':
                answer += int(code)
    return answer

answer = main()
print(answer)
