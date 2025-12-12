from collections import defaultdict
def read_file(filename):
    with open(filename, encoding="utf-8") as file:
        lines = file.read().split("\n")
        return lines
    

def depth_first_search(current_node, letter_dict, visited, target_end, all_solutions):
    visited.append(current_node)

    if current_node == target_end:
        all_solutions.append(visited)
        return

    next_nodes = letter_dict[current_node]

    for node in next_nodes:
        depth_first_search(node, letter_dict, visited.copy(), target_end, all_solutions)

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
    fft_strings = []
    depth_first_search("svr", letter_dict, [], 'fft', fft_strings)
    print(fft_strings)

    dac_strings = []
    depth_first_search("svr", letter_dict, [], 'dac', dac_strings)
    print(dac_strings)
    return answer

answer = main()
print(answer)
