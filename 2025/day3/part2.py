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
        for battery_index in range(len(bank) - 11):
            current_battery = int(bank[battery_index])
            if current_battery > biggest_battery:
                biggest_battery =  current_battery
                biggest_battery_index = battery_index
        voltage = ''        

        batteries_to_remove = len(bank) - biggest_battery_index - 12 
        battery_indexes_to_remove = []
        while batteries_to_remove > 0:
            for lowest_number in range(1, 10):
                for battery_index in range(biggest_battery_index+1, len(bank)):
                    if batteries_to_remove == 0:
                        break
                    if int(bank[battery_index]) == lowest_number: 
                        if len(bank) - battery_index > batteries_to_remove:
                            if battery_index not in battery_indexes_to_remove:
                                valid_indexes_to_right = []
                                for current_battery_index in range(battery_index + 1, len(bank)):
                                    if current_battery_index not in battery_indexes_to_remove:
                                        valid_indexes_to_right.append(current_battery_index)
                                if len(valid_indexes_to_right) > 0:
                                    for valid_index_to_right in valid_indexes_to_right:
                                        if int(bank[battery_index]) < int(bank[valid_index_to_right]):
                                            if battery_index not in battery_indexes_to_remove:
                                                battery_indexes_to_remove.append(battery_index)
                                                batteries_to_remove -= 1
                        else:
                            battery_indexes_to_remove.append(battery_index)
                            batteries_to_remove -= 1
        for battery_index in range(biggest_battery_index, len(bank)):
            if battery_index not in battery_indexes_to_remove:
                voltage += bank[battery_index]
        answer += int(voltage)

    return answer

answer = main()
print(answer)
