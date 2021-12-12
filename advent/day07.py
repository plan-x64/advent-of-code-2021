import adventutils
import sys

def find_min_fuel(input, cost_fn):
    ordered_input = sorted(input)
    (min, max) = (ordered_input[0], ordered_input[-1])
    costs = [(maybe_min, cost_fn(maybe_min, ordered_input)) for maybe_min in range(min, max)]
    return sorted(costs, key = lambda x: x[1])[0]

def main():
    sessionId = sys.argv[1]
    url = "https://adventofcode.com/2021/day/7/input"
    transform = lambda x: [int(day) for day in str(x, "utf-8").split(',')]
    input = next(iter(adventutils.gather_input_data(url, sessionId, transform)))

    pt1_cost_fn = lambda x_min, xs: sum([abs(x - x_min) for x in xs])
    pt2_cost_fn = lambda x_min, xs: sum([(abs(x - x_min)**2+abs(x - x_min))//2 for x in xs])

    print("Part1: {}".format(find_min_fuel(input, pt1_cost_fn)))
    print("Part2: {}".format(find_min_fuel(input, pt2_cost_fn)))
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Need to pass 'python day07.py sessionId' (Arguments={}, Length={})".format(str(sys.argv), len(sys.argv)))
    else:  
        main()