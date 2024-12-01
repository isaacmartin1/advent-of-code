def read_file():
    with open("input.csv", encoding="utf-8") as file:
        lines = file.read().split("\n")
        return lines

def create_lists(lines):
    left_list = []
    right_list = []
    for x in lines:
        items = x.split()
        left_list.append(int(items[0]))
        right_list.append(int(items[1]))
    left_list.sort()
    right_list.sort()
    return left_list, right_list

def get_similarity_score(target_number, compare_list):
    number_of_matches = 0
    for x in compare_list:
        if x == target_number:
            number_of_matches += 1
    return number_of_matches * target_number

def transform_to_numbers(input_list):
    return list(map(int, input_list))

def get_all_similarity_scores(left_list, right_list):
    similarity_score_dict = {}
    left_list_unique_values = list(set(left_list))
    for x in left_list_unique_values:
        similarity_score_dict[f'{x}'] = get_similarity_score(x, right_list)

    return similarity_score_dict


def main():
    lines = read_file()

    left_list, right_list = create_lists(lines)

    similarity_score_dict = get_all_similarity_scores(left_list, right_list)

    similarity_score = 0
    for x in left_list:
        specific_similarity_score = similarity_score_dict[f'{x}']
        similarity_score += specific_similarity_score

    return similarity_score
            

score = main()

print(score)
