import re
import math

def read_file():
    with open("input.csv", encoding="utf-8") as file:
        lines = [line.split() for line in file.read().split("\n")]
        robots = {}
        index = 0
        p = []
        v = []
        for line in lines:
            for section in line:
                robots[f"{index}"] = {}
                if 'p' in section:
                    p = re.findall(r'-?\d+', section)
                elif 'v' in section:
                    v = re.findall(r'-?\d+', section)
                if len(p) > 0 and len(v) > 0:
                    robots[f"{index}"] = {
                        'p_x': int(p[0]),
                        'p_y': int(p[1]),
                        'v_x': int(v[0]),
                        'v_y': int(v[1])
                    }
                    p = []
                    v = []
                    index += 1
        return robots

class color:
   GREEN = '\033[92m'
   BASE = '\033[0m'

def get_tree_print(robots, x_lim, y_lim, sim):
    print('--------------------')
    print('seconds', sim+1)
    lines = []
    for _ in range(y_lim):
        line = []
        for _ in range(x_lim):
            line.append(' ')
        lines.append(line)


    for _, r in robots.items():
        x = (r['p_x'] + sim*r['v_x']) % x_lim
        y = (r['p_y'] + sim*r['v_y']) % y_lim
        lines[y][x] = 'o'
    

    for line in lines:
        print(''.join(line).replace('o', color.GREEN + 'o' + color.BASE))
    print('--------------------')

# clusters
# 72, 120, 173, 223, 274

def main():
    robots = read_file()
    x_lim = 101
    y_lim = 103
    sims = 100

    sim_list = []
    # try different commbinations
    for iteration in range(5929, 8051, 101):
            sim_list.append(iteration)
    for iteration in range(5990, 8051, 103):
            sim_list.append(iteration)

    for sim in sim_list:
        get_tree_print(robots, x_lim, y_lim, sim)
