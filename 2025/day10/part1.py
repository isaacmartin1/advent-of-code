def read_file(filename):
    with open(filename, encoding="utf-8") as file:
        lines = [line for line in file.read().split("\n")]
        return lines
    
def main():
    answer = 0
    filename = "input.csv"
    lines = read_file(filename)
    for line in lines:
        # Prepare Data (Ignore Junctions)
        line = line.split()
        target_machine_state = line.pop(0)
        target_machine_state = target_machine_state[1:len(target_machine_state) - 1]
        buttons = [button.replace('(','').replace(')','').split(',') for button in line[0:len(line)-1]]
        for button_set_idx in range(len(buttons)):
            buttons[button_set_idx] = [int(target_machine) for target_machine in buttons[button_set_idx]]

        import pdb
        pdb.set_trace()

    return answer

answer = main()
print(answer)
