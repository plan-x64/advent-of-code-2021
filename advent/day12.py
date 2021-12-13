import adventutils
from collections import (defaultdict, deque)
import sys

def parse_graph(input):
    graph = defaultdict(set)
    for connection in input:
        (v1, v2) = tuple(connection.split('-'))
        graph[v1].add(v2) 
        graph[v2].add(v1)

    return graph

def part1_path_filter(possible_vertex, current_path):
    return possible_vertex.isupper() or possible_vertex not in current_path

def part2_path_filter(possible_vertex, current_path):
    lower = [vertex for vertex in current_path if vertex.islower()]
    is_small_duplicate = len(lower) != len(set(lower))
    return part1_path_filter(possible_vertex, current_path) or (possible_vertex != 'start' and not is_small_duplicate)

def find_all_paths(graph, path_filter):
    paths = deque([['start']])

    valid_paths = []
    while paths:
        current_path = paths.pop()
        current_vertex = current_path[-1]

        if current_vertex == 'end':
            valid_paths.append(current_path)
            continue

        for connected_vertex in graph[current_vertex]:
            if path_filter(connected_vertex, current_path):
                paths.append(current_path + [connected_vertex])

    return valid_paths

def main():
    sessionId = sys.argv[1]
    url = "https://adventofcode.com/2021/day/12/input"
    input = adventutils.gather_input_data(url, sessionId)

    graph = parse_graph(input)

    print("Part1: {}".format(len(find_all_paths(graph, part1_path_filter))))
    print("Part2: {}".format(len(find_all_paths(graph, part2_path_filter))))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Need to pass 'python day12.py sessionId' (Arguments={}, Length={})".format(str(sys.argv), len(sys.argv)))
    else:  
        main()