import adventutils
from collections import deque
import functools
import sys

def surrounding(input, x, y):
    vals = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    return [(x_i, y_i) for (x_i, y_i) in vals if 0 <= x_i < len(input) and 0 <= y_i < len(input[x])]

def is_min(input, x, y):
    for (x_i, y_i) in surrounding(input, x, y):
        if input[x][y] == 9 or input[x_i][y_i] < input[x][y]:
            return False
    return True

def find_mins(input):
    mins = []
    for row in range(len(input)):
        for column in range(len(input[row])):
            if is_min(input, row, column):
                mins.append((row, column))
    return mins

def find_basin(input, x, y):
    basin = []
    visited = set()
    queue = deque([(x,y)])
    
    while queue:
        (x_i, y_i) = queue.pop()

        if (x_i, y_i) in visited:
            continue
        else:
            visited.add((x_i, y_i))
            if input[x_i][y_i] != 9:
                basin.append((x_i, y_i))
                queue.extend([(x_j, y_j) for (x_j, y_j) in surrounding(input, x_i, y_i) if (x_j, y_j) not in visited])

    return basin

def main():
    sessionId = sys.argv[1]
    url = "https://adventofcode.com/2021/day/9/input"
    transform = lambda line: [int(char) for char in str(line, "utf-8").strip('\n')]
    input = adventutils.gather_input_data(url, sessionId, transform)

    mins = find_mins(input)
    basins = [find_basin(input, x, y) for (x, y) in mins]

    print("Part1: {}".format(sum([input[x][y]+1 for (x,y) in mins])))
    print("Part2: {}".format(functools.reduce(lambda a,b: a*b, sorted([len(basin) for basin in basins], reverse=True)[0:3])))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Need to pass 'python day09.py sessionId' (Arguments={}, Length={})".format(str(sys.argv), len(sys.argv)))
    else:  
        main()