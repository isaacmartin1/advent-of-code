from z3 import *

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
        # Prepare Data
        line = line.split()
        buttons = [button.replace('(','').replace(')','').split(',') for button in line[1:len(line)-1]]
        
        # joltage now needed
        joltage_reqs = line[-1].replace('{', '').replace('}', '').replace(',', '')
        new_line_base = "".join(['0' for _ in range(len(joltage_reqs))])

        # convert buttons to string reps of binary
        for button_set_idx in range(len(buttons)):
            current_line = new_line_base
            for index in [int(button) for button in buttons[button_set_idx]]:
                current_line = current_line[:index] + '1' + current_line[index+1:]
            buttons[button_set_idx] = current_line
        import pdb
        pdb.set_trace()
        # GET possible combinations in ascending order
        combinations = []
        for num_presses in range(1, 1000):
            print('trying press #', num_presses)
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
                            rolling_total = int(rolling_total) + int(combo[idx])
                        else:
                            rolling_total = int(f"{rolling_total:0{len(new_line_base)}}") + int(combo[idx])

                if not isinstance(rolling_total, str):
                    # import pdb
                    # pdb.set_trace()
                    rolling_total = f"{rolling_total:0{len(new_line_base)}}"

                if rolling_total == joltage_reqs:
                    print('solved', answers_solved)
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
