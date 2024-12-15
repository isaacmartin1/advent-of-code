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


def get_robot_quad(r, x_lim, y_lim, sims):
    x = (r['p_x'] + sims*r['v_x']) % x_lim
    y = (r['p_y'] + sims*r['v_y']) % y_lim

    half_x_lim = x_lim/2-.5
    half_y_lim = y_lim/2-.5

    if x == half_x_lim or y == half_y_lim:
        return None
    if x > half_x_lim:
        if y > half_y_lim:
            return 'lower_right'
        elif y < half_y_lim:
            return 'upper_right'
    elif x < half_x_lim:
        if y < half_y_lim:
            return 'upper_left'
        elif y > half_y_lim:
            return 'lower_left'


def get_quadrant_score(quadrants):
    factor = 1
    for _, value in quadrants.items():
        factor *= value
    return factor


def main():
    robots = read_file()
    x_lim = 101
    y_lim = 103
    sims = 100
    quadrants = {
        'upper_right': 0,
        'upper_left': 0,
        'lower_right': 0,
        'lower_left': 0
    }
    for _, r in robots.items():
        q = get_robot_quad(r, x_lim, y_lim, sims)
        if q is not None:
            quadrants[q] += 1
    
    return get_quadrant_score(quadrants)


answer = main()

print(answer)
