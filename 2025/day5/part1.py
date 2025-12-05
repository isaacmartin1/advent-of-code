def read_file(filename):
    with open(filename, encoding="utf-8") as file:
        lines = file.read().split("\n")
        return lines
    
def main():
    answer = 0
    filename = "input.csv"
    lines = read_file(filename)
    ranges = []
    for line in lines:
        if '-' in line:
            # process range
            lower_bound, upper_bound = line.split('-')
            ranges.append([int(lower_bound), int(upper_bound) + 1])
        elif line != '':
            ingredient_id = int(line)
            is_fresh = False
            for lower_bound, upper_bound in ranges:
                if is_fresh == True:
                    break

                if ingredient_id in range(lower_bound, upper_bound):
                    is_fresh = True
            if is_fresh:
                answer += 1

    return answer

answer = main()
print(answer)
