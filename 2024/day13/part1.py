import re
import math

def read_file():
    with open("input.csv", encoding="utf-8") as file:
        lines = file.read().split("\n")
        arcade = {}
        index = 0
        Button_A = []
        Button_B = []
        Prize = []
        for x in lines:
            arcade[f"{index}"] = {}
            if 'Button A' in x:
                Button_A = re.findall(r'\d+', x)
            elif 'Button B' in x:
                Button_B = re.findall(r'\d+', x)
            elif 'Prize' in x:
                Prize = re.findall(r'\d+', x)
            if len(Prize) > 0 and len(Button_A) > 0 and len(Button_B) > 0:
                arcade[f"{index}"] = {
                    'a_x': int(Button_A[0]),
                    'a_y': int(Button_A[1]),
                    'b_x': int(Button_B[0]),
                    'b_y': int(Button_B[1]),
                    'prize_x': int(Prize[0]),
                    'prize_y': int(Prize[1])
                }
                Button_A = []
                Button_B = []
                Prize = []
                index += 1
        return arcade

def get_min_tokens(
        a_x,
        a_y,
        b_x,
        b_y,
        prize_x,
        prize_y
):
    # tokens = minimize(num_a * 3 + num_b)
    # prize_x == num_a * a_x + num_b * b_x
    # prize_y == num_a * a_y + num_b * b_y
    possible_solutions = []
    max_a = max(math.floor(prize_x/a_x), math.floor(prize_y/a_y))
    max_b = max(math.floor(prize_x/b_x), math.floor(prize_y/b_y))
    for num_a in range(max_a):
        for num_b in range(max_b):
            if prize_x == num_a * a_x + num_b * b_x and \
                prize_y == num_a * a_y + num_b * b_y:
                possible_solutions.append([num_a, num_b])

    total_considered = []
    for x in possible_solutions:
        print(x)
        total_considered.append(x[0]*3 + x[1])

    if len(total_considered) > 0:
        return min(total_considered)

    return 0



def main():
    arcade = read_file()
    token_sum = 0 
    for _, value in arcade.items():
        token_sum += get_min_tokens(
            value["a_x"],
            value["a_y"],
            value["b_x"],
            value["b_y"],
            value["prize_x"],
            value["prize_y"]
        )
    return token_sum


answer = main()

print(answer)
