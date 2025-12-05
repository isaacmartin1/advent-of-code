def read_file(filename):
    with open(filename, encoding="utf-8") as file:
        lines = [line.split()[0] for line in file.read().split("\n")]
        return lines
    
def main():
    answer = 0
    filename = "input.csv"
    lines = read_file(filename)
    for bank in lines:
        biggest_battery_index = None
        biggest_battery = 1
        for battery_index in range(len(bank) - 1):
            current_battery = int(bank[battery_index])
            if current_battery > biggest_battery:
                biggest_battery =  current_battery
                biggest_battery_index = battery_index
        second_biggest_battery = 1
        for subsequent_battery_index in range(biggest_battery_index+1, len(bank)):
            proposed_second_battery = int(bank[subsequent_battery_index])
            if proposed_second_battery > second_biggest_battery:
                second_biggest_battery = proposed_second_battery
        biggest_voltage = int(str(biggest_battery) + str(second_biggest_battery))
        answer += biggest_voltage

    return answer

answer = main()
print(answer)
