from collections import defaultdict
def read_file(filename):
    with open(filename, encoding="utf-8") as file:
        lines = [line.split()[0] for line in file.read().split("\n")]
        return lines

def main():
    answer = 0
    filename = "input.csv"
    lines = read_file(filename)
    tachyon_row_indexes = defaultdict(int)
    for line in lines:
        if 'S' in line:
            tachyon_row_indexes[line.find('S')] = 1
        else:
            index_to_delete = []
            index_to_add = []
            for row_idx in tachyon_row_indexes.keys():
                if line[row_idx] == '^' and row_idx not in index_to_add:
                    index_to_delete.append(row_idx)
                    for proposed_idx in [row_idx - 1, row_idx +1]:
                        if 0 <= proposed_idx < len(line):
                            index_to_add.append((row_idx, proposed_idx))

            for old, replacement in index_to_add:
                tachyon_row_indexes[replacement] +=  tachyon_row_indexes[old]
            
            for old in index_to_delete:
                tachyon_row_indexes[old] = 0


    for number in tachyon_row_indexes.values():
        answer += number
    return answer

answer = main()
print(answer)
