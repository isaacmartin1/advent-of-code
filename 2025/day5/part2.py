def read_file(filename):
    with open(filename, encoding="utf-8") as file:
        lines = file.read().split("\n")
        return lines
    
def main():
    filename = "input.csv"
    lines = read_file(filename)
    answer = 0
    valid_ids = set()
    for line in lines:
        if '-' in line:
            # process range
            new_lower, new_upper = line.split('-')
            new_lower, new_upper = int(new_lower), int(new_upper)
            valid_ids.add((new_lower, new_upper))
            overlap_mins = [new_lower]
            overlap_maxes = [new_upper]
            candidate_valid_ids = set()
            if len(valid_ids) > 0:
                for old_lower, old_upper in valid_ids:
                    if new_lower <= old_lower <= new_upper or new_lower <= old_upper <= new_upper:
                        overlap_mins.append(old_lower)
                        overlap_maxes.append(old_upper)
                    elif old_lower <= new_lower <= old_upper or old_lower <= new_upper <= old_upper:
                        overlap_mins.append(old_lower)
                        overlap_maxes.append(old_upper)
                    else:
                        candidate_valid_ids.add((old_lower, old_upper))
            if len(overlap_mins) > 1:
                candidate_valid_ids.add((min(overlap_mins), max(overlap_maxes)))
                valid_ids = candidate_valid_ids
            else:
                valid_ids.add((new_lower, new_upper))

    for lower, upper in valid_ids:
        answer += upper + 1 - lower
    return answer

answer = main()
print(answer)


