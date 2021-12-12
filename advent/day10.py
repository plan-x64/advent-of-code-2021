import adventutils
from collections import (deque, defaultdict)
import functools
import sys

char_groups = [('(', ')'), ('{', '}'), ('[', ']'), ('<', '>')]
char_pairs = {**{start:end for (start, end) in char_groups}, **{end:start for (start, end) in char_groups}}
start_chars = set([char for (char, _) in char_groups])
end_chars = set([char for (_, char) in char_groups])

def parse_line(line):
    char_stack = deque()
    for char in line:
        if char in start_chars:
            char_stack.append(char)
        else:
            start_char = char_stack.pop()
            if char_pairs[start_char] != char:
                return ('corrupted', char)

    if char_stack:
        return ('incomplete', list(reversed([char_pairs[starting] for starting in char_stack])))
    else:
        return ('valid', None)


def parse(lines):
    results = defaultdict(list)
    for line in lines:
        (result_type, value) = parse_line(line)
        results[result_type].append(value)
    
    return results

def part1(corrupted):
    syntax_cost = {
        ')': 3, 
        ']': 57,
        '}': 1197,  
        '>': 25137
    }

    return sum([syntax_cost[char] for char in corrupted])

def part2(incomplete):
    autocomplete_cost = {
        ')': 1, 
        ']': 2, 
        '}': 3, 
        '>': 4
    }

    scores = []
    for line in incomplete:
        base_costs = [autocomplete_cost[char] for char in line]
        cost_calc = lambda a, c: 5*a+c
        scores.append(functools.reduce(cost_calc, base_costs, 0))
    scores.sort()
    return scores[len(scores)//2]

def main():
    sessionId = sys.argv[1]
    url = "https://adventofcode.com/2021/day/10/input"
    input = adventutils.gather_input_data(url, sessionId, transform=lambda x: [char for char in str(x, "utf-8").strip('\n')])

    results = parse(input)

    print("Part1: {}".format(part1(results['corrupted'])))
    print("Part2: {}".format(part2(results['incomplete'])))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Need to pass 'python day10.py sessionId' (Arguments={}, Length={})".format(str(sys.argv), len(sys.argv)))
    else:  
        main()