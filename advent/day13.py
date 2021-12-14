import adventutils
import functools
import sys

def parse_input(input):
    delimiter = input.index('')
    points = [functools.reduce(lambda x,y: (int(x), int(y)), point.split(',')) for point in input[0:delimiter]]
    directions = [functools.reduce(lambda dir, amount: (dir, int(amount)), direction.split()[2].split('=')) for direction in input[delimiter+1:]]
    return (points, directions)

def fold(points, direction):
    (fold_along, amount) = direction

    if fold_along == 'x':
        return [fold_left(point, amount) for point in points]
    else:
        return [fold_up(point, amount) for point in points]   

def fold_up(point, amount):
    (x,y) = point
    return (x, 2*amount-y) if y > amount else (x,y)

def fold_left(point, amount):
    (x,y) = point
    return (2*amount-x, y) if x > amount else (x,y)

def display(points):
    (max_x, max_y) = (max([x for (x,_) in points]), max([y for (_,y) in points]))
    points_lookup = set(points)
    return '\n' + '\n'.join([''.join(['#' if (x,y) in points_lookup else ' ' for x in range(max_x+1)]) for y in range(max_y+1)])

def main():
    sessionId = sys.argv[1]
    url = "https://adventofcode.com/2021/day/13/input"
    input = adventutils.gather_input_data(url, sessionId)

    (points, directions) = parse_input(input)
    print("Part1: {}".format(len(set(fold(points, directions[0])))))
    print("Part2: {}".format(display(functools.reduce(lambda accum, dir: fold(accum, dir), directions, points))))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Need to pass 'python day13.py sessionId' (Arguments={}, Length={})".format(str(sys.argv), len(sys.argv)))
    else:  
        main()