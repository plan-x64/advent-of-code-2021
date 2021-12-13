import adventutils
from collections import deque
import itertools
import sys

def surrounding(input, x, y):
    vals = itertools.product(range(x-1, x+2), range(y-1, y+2))
    in_bounds = lambda x_i, y_i: 0 <= x_i < len(input) and 0 <= y_i < len(input[x]) and (x_i, y_i) != (x,y)
    return [(x_i, y_i) for (x_i, y_i) in vals if in_bounds(x_i, y_i)]

def exceeded(input):
    exceeded = []
    for x in range(len(input)):
        for y in range(len(input[x])):
            if input[x][y] > 9:
                exceeded.append((x,y))

    return exceeded            

def step(input):
    values = [[num+1 for num in line] for line in input]

    exceeded_values = exceeded(values)
    flashing = deque(exceeded_values)
    visited = set(exceeded_values)

    while flashing:
        (x, y) = flashing.pop()
        for (x_i, y_i) in surrounding(input, x, y):
            values[x_i][y_i] += 1
            value = values[x_i][y_i]
            if value > 9 and (x_i, y_i) not in visited:
                flashing.append((x_i, y_i))
                visited.add((x_i, y_i))

    return (len(visited), [[num if num <= 9 else 0 for num in line] for line in values])

def count_flashes(input, n):
    current_values = list(input)
    total_flashes = 0
    for _ in range(n):
        (step_flashes, current_values) = step(current_values)
        total_flashes += step_flashes

    return total_flashes

def find_first_all_flash(input, max):
    current_values = list(input)
    for step_num in range(max):
        (step_flashes, current_values) = step(current_values)
        if step_flashes == sum([len(line) for line in current_values]):
            return step_num+1

    return None

def main():
    sessionId = sys.argv[1]
    url = "https://adventofcode.com/2021/day/11/input"
    input = adventutils.gather_input_data(url, sessionId, transform=lambda x: [int(char) for char in str(x, "utf-8").strip('\n')])

    print("Part1: {}".format(count_flashes(input, 100)))
    print("Part2: {}".format(find_first_all_flash(input, 500)))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Need to pass 'python day11.py sessionId' (Arguments={}, Length={})".format(str(sys.argv), len(sys.argv)))
    else:  
        main()