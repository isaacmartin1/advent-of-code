from collections import defaultdict
def read_file(filename):
    with open(filename, encoding="utf-8") as file:
        lines = file.read().split("\n")
        return lines
    

def depth_first_search(next_steps, letter_dict, terminal_set, answer):
    # print(terminal_set)

    if isinstance(next_steps, list):
        for current_step in next_steps:
            terminal_set_copy = terminal_set.copy()
            answer = depth_first_search(current_step, letter_dict, terminal_set_copy, answer)

    else:
        if next_steps in terminal_set:
            return answer
        terminal_set.add(next_steps)
        if next_steps == 'out' and 'fft' in terminal_set and 'dac' in terminal_set:
            print(terminal_set)
            answer += 1
            return answer
        elif next_steps != 'out':
            next_steps = letter_dict[next_steps]
            answer = depth_first_search(next_steps, letter_dict, terminal_set, answer)

    return answer

def main():
    answer = 0
    filename = "input.csv"
    lines = read_file(filename)
    # first construct a dictionary
    letter_dict = defaultdict(list)

    for line in lines:
        start, endings = line.split(':')
        endings = endings.split()
        for end in endings:
            letter_dict[start].append(end)

    # DEPTH FIRST SEARCH
    next_steps = letter_dict["svr"]
    answer = depth_first_search(next_steps, letter_dict, {'svr'}, answer)

    return answer

answer = main()
print(answer)
