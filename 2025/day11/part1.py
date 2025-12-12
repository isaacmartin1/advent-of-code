from collections import defaultdict
def read_file(filename):
    with open(filename, encoding="utf-8") as file:
        lines = file.read().split("\n")
        return lines
    

def depth_first_search(next_steps, letter_dict, terminal_list, answer):
    print(terminal_list)

    if len(next_steps) > 1:
        for current_step in next_steps:
            terminal_list_copy = terminal_list.copy()
            answer = depth_first_search([current_step], letter_dict, terminal_list_copy, answer)

    elif len(next_steps) == 1:
        current_step = next_steps[0]
        terminal_list.append(current_step)
        if current_step == 'out':
            print(terminal_list)
            answer += 1
            return answer
        elif current_step != 'out':
            next_steps = letter_dict[current_step]
            answer = depth_first_search(next_steps, letter_dict, terminal_list, answer)

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

    # start
    next_steps = letter_dict["you"]

    # DEPTH FIRST SEARCH
    answer = depth_first_search(next_steps, letter_dict, ['you'], answer)

    return answer

answer = main()
print(answer)
