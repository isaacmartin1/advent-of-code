def read_file(filename):
    with open(filename, encoding="utf-8") as file:
        lines = [line.split()[0] for line in file.read().split("\n")]
        return lines
    
def main():
    answer = 0
    filename = "input.csv"
    lines = read_file(filename)[0].split(',')

    return answer

answer = main()
print(answer)
