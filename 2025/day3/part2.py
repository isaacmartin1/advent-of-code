def read_file(filename):
    with open(filename, encoding="utf-8") as file:
        lines = [line.split()[0] for line in file.read().split("\n")]
        return lines

def main():
    answer = 0
    filename = "input.csv"
    lines = read_file(filename)

    for bank in lines:
        num_to_remove = len(bank) - 12
        voltage = []

        for battery in bank:
            battery = int(battery)
            while voltage and num_to_remove > 0 and voltage[-1] < battery:
                voltage.pop()
                num_to_remove -= 1
            voltage.append(battery)

        answer += int("".join([str(battery) for battery in voltage])[0:12])

    return answer

answer = main()
print(answer)
