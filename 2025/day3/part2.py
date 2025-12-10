def read_file(filename):
    with open(filename, encoding="utf-8") as file:
        lines = [line.split()[0] for line in file.read().split("\n")]
        return lines

def main():
    answer = 0
    filename = "input.csv"
    lines = read_file(filename)
    for bank in lines:
        voltage = [int(x) for x in list(bank)]
        while len(voltage) > 12:
            removed_item = False
            for battery_idx in range(len(voltage) - 1):
                current_battery = voltage[battery_idx]
                next_battery = voltage[battery_idx + 1]
                if current_battery < next_battery:
                    voltage.pop(battery_idx)
                    removed_item = True
                    break
            if removed_item == False:
                voltage = voltage[0:12]

        answer += int("".join([str(x) for x in voltage]))

    return answer

answer = main()
print(answer)
