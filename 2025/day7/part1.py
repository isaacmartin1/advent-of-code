def read_file(filename):
    with open(filename, encoding="utf-8") as file:
        lines = [line.split()[0] for line in file.read().split("\n")]
        return lines
    
def main():
    answer = 0
    filename = "input.csv"
    lines = read_file(filename)
    tachyon_row_indexes = []
    for line in lines:
        if 'S' in line:
            tachyon_row_indexes = [line.find('S')]
        else:
            index_to_delete = []
            index_to_add = []
            for row_idx in tachyon_row_indexes:
                if line[row_idx] == '^':
                    answer += 1
                    index_to_delete.append(row_idx)
                    for proposed_idx in [row_idx - 1, row_idx +1]:
                        if 0 <= proposed_idx < len(line) and proposed_idx not in index_to_add and proposed_idx not in tachyon_row_indexes:
                            index_to_add.append(proposed_idx)

            # process additions
            new_tachyon_row_indexes = []

            for row_idx in tachyon_row_indexes:
                if row_idx not in index_to_delete:
                    new_tachyon_row_indexes.append(row_idx)

            for row_idx in index_to_add:
                new_tachyon_row_indexes.append(row_idx)
            tachyon_row_indexes = new_tachyon_row_indexes

    return answer

answer = main()
print(answer)
