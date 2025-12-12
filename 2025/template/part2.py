def read_file(filename):
    with open(filename, encoding="utf-8") as file:
        lines = [line.split() for line in file.read().split("\n")]
        return lines
    
def main():
    answer = 0
    filename = "input.csv"
    lines = read_file(filename)

    return answer

answer = main()
print(answer)
