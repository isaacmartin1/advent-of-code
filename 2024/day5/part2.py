import math

def read_file():
    with open("input.csv", encoding="utf-8") as file:
        lines = file.read().split("\n")
        return lines


def separate_inputs(lines):
    for i in range(len(lines)):
        if lines[i] == '':
            return lines[:i], lines[i+1:]


def get_rules_dict(rules):
    rules_dict = {}
    for r in rules:
        right_value, left_value = [int(x) for x in r.split('|')]
        # right side case
        if rules_dict.get(right_value) == None:
            rules_dict[right_value] = {
                'before': set(),
                'after': {left_value}
            }
        else:
            rules_dict[right_value]['after'].add(left_value)
        # left side case
        if rules_dict.get(left_value) == None:
            rules_dict[left_value] = {
                'before': {right_value},
                'after': set()
            }
        else:
            rules_dict[left_value]['before'].add(right_value)
    return rules_dict


def is_item_valid(position, u, rules_dict):
    for iteration in  range(len(u)):
        if iteration != position:
            if iteration < position:
                if u[iteration] in rules_dict[u[position]]['after']:
                    return False
            if iteration > position:
                if u[iteration] in rules_dict[u[position]]['before']:
                    return False
    return True
          

def get_middle_value(u):
    return u[math.floor(len(u)/2)]


def send_back(position, u, fixed_list, rules_dict):
    lowest_value = None
    for iteration in range(len(fixed_list)):
        if fixed_list[iteration] in rules_dict[u[position]]['after']:
            return iteration

    return lowest_value


def fix_update(u, rules_dict):
    fixed_list = []
    for position in range(len(u)):
        if position == 0:
            fixed_list.append(u[position])
        else:
            backwards_index = send_back(position, u, fixed_list, rules_dict)
            if backwards_index != None:
                fixed_list.insert(backwards_index, u[position])
            else:
                fixed_list.append(u[position])

    return fixed_list


def get_update_value(rules_dict, u):
    u = [int(x) for x in u.split(',')]
    invalid_count = 0
    for position in range(len(u)):
        is_valid = is_item_valid(position, u, rules_dict)
        if not is_valid:
            invalid_count += 1

    if invalid_count == 0:
        return 0
    
    reordered_u = fix_update(u, rules_dict)
    middle_number = get_middle_value(reordered_u)
    print('returning midle', middle_number)
    return middle_number


def main():
    lines = read_file()
    rules, updates = separate_inputs(lines)
    rules_dict = get_rules_dict(rules)
    answer = 0

    for u in updates:
        middle_value = get_update_value(rules_dict, u)
        answer += middle_value

    return answer


answer = main()

print(answer)