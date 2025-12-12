def read_file(filename):
    with open(filename, encoding="utf-8") as file:
        lines = [line for line in file.read().split("\n")]
        return lines
    
def main():
    answer = 0
    filename = "input.csv"
    lines = read_file(filename)
    answers_solved = 0
    for line in lines:
        # Prepare Data (Ignore Junctions)
        line = line.split()
        target_machine_state = line.pop(0).replace('.', '0').replace('#', '1')
        target_machine_state = target_machine_state[1:len(target_machine_state) - 1]
        buttons = [button.replace('(','').replace(')','').split(',') for button in line[0:len(line)-1]]
        new_line_base = target_machine_state.replace('1', '0')
 
        # convert buttons to string reps of binary
        for button_set_idx in range(len(buttons)):
            current_line = new_line_base
            for index in [int(buttons) for buttons in buttons[button_set_idx]]:
                current_line = current_line[:index] + '1' + current_line[index+1:]
            buttons[button_set_idx] = current_line

        # int(number, base) -> base means base of 2 which is binary
        # answer = int(buttons[0], 2) ^ int(buttons[1], 2)
        # f"{answer:0{len(new_line_base)}b}"
        # PRINTS '0100'

        # GET possible combinations in ascending order
        combinations = []
        for num_presses in range(1, 1000):
            if num_presses == 1:
                for button_set in buttons:
                    combinations.append([button_set])
            else:
                new_combinations = []
                for combo in combinations:
                    for button_set in buttons:
                        temp_combo = combo.copy()
                        temp_combo.append((button_set))
                        new_combinations.append(temp_combo)
                combinations = new_combinations
            
            # evaluate each candidate
            answer_found = False
            for combo in combinations:
                rolling_total = None
                for idx in range(len(combo)):
                    if idx == 0:
                        rolling_total = combo[idx]
                    else:
                        if isinstance(rolling_total, str):
                            rolling_total = int(rolling_total, 2) ^ int(combo[idx], 2)
                        else:
                            rolling_total = int(f"{rolling_total:0{len(new_line_base)}b}", 2) ^ int(combo[idx], 2)

                if not isinstance(rolling_total, str):
                    rolling_total = f"{rolling_total:0{len(new_line_base)}b}"

                if rolling_total == target_machine_state:
                    answers_solved += 1
                    answer += len(combo)
                    answer_found = True
                    break
            if answer_found == True:
                answer_found = False
                break

    return answer

answer = main()
print(answer)
