import time
start = time.perf_counter()
from collections import defaultdict


def read_file():
    with open("input.csv", encoding="utf-8") as file:
        initial_list = file.read().split("\n")[0]

        dict = {}
        for x in initial_list.split():
            if x != ' ':
                dict[x] = 1
        return dict


def apply_rules(s):
    int_s = int(s)
    len_s = len(s)
    if int_s == 0:
        return [str(1)]
    elif len_s % 2 == 0:
        half = len(s)//2
        return [str(int(s[:half])), str(int(s[half:]))]
    else:
        return[str(int_s*2024)]


def get_new_dict(dict):
    new_dict = {}
    for stone, count in dict.items():
        new_stones = apply_rules(stone)
        for s in new_stones:
            if s not in new_dict.keys():
                new_dict[s] = count
            else:
                new_dict[s] += count
    return new_dict


def main():
    dict = read_file()

    answer = 0
    i = 0
    while i < 75:
        dict = get_new_dict(dict)
        print(f'processing {i}')
        print(dict)
        i += 1
    for x in dict:
        answer += dict[x]
    return answer


answer = main()

print(answer)

end = time.perf_counter()
print(end - start)
