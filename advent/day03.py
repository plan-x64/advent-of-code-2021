import adventutils
from collections import Counter
import sys

def bin_to_int(binary):
    string_binary = "".join(str(bit) for bit in binary)
    return int(string_binary, 2)

def transpose(values):
    return [[row[i] for row in values] for i in range(len(values[0]))]

def frequency(column, max, tiebreaker):
    counter = Counter(column)
    if counter[0] > counter[1]:
        return 0 if max else 1
    elif counter[0] < counter[1]:
        return 1 if max else 0
    else:
        return tiebreaker    

def binary_gamma(data):
    return list(map(lambda x: frequency(x, max=True, tiebreaker=1), data))

def binary_epsilon(data):
    return list(map(lambda x: frequency(x, max=False, tiebreaker=0), data))

def filter_data(data, bitmask_generator):
    filtered = data
    for index in range(0, len(data[0])):
        if len(filtered) == 1:
            return filtered[0]

        remaining = []
        bitmask = bitmask_generator(filtered)
        for datum in filtered:
            if datum[index] == bitmask[index]:
               remaining.append(datum) 
        
        filtered = remaining

    return filtered[0]

def part2(values):
    binary_oxygen = filter_data(values, lambda x: binary_gamma(transpose(x)))
    binary_co2 = filter_data(values, lambda x: binary_epsilon(transpose(x)))

    oxygen = bin_to_int(binary_oxygen)
    co2 = bin_to_int(binary_co2)

    return (oxygen, co2)

def part1(values):
    columns = transpose(values)
    
    gamma = bin_to_int(binary_gamma(columns))
    epsilon = bin_to_int(binary_epsilon(columns))

    return (gamma, epsilon)

def main():
    sessionId = sys.argv[1]  
    url = "https://adventofcode.com/2021/day/3/input"
    transform = lambda x: [int(digit) for digit in list(str(x, "utf-8").strip('\n'))]
    values = adventutils.gather_input_data(url, sessionId, transform)

    # values = [[0,0,1,0,0],
    #         [1,1,1,1,0],
    #         [1,0,1,1,0],
    #         [1,0,1,1,1],
    #         [1,0,1,0,1],
    #         [0,1,1,1,1],
    #         [0,0,1,1,1],
    #         [1,1,1,0,0],
    #         [1,0,0,0,0],
    #         [1,1,0,0,1],
    #         [0,0,0,1,0],
    #         [0,1,0,1,0]]

    (gamma, epsilon) = part1(values)
    (oxygen, co2) = part2(values)

    print("Part 1: {} ({}, {})".format(gamma*epsilon, gamma, epsilon))
    print("Part 2: {} ({}, {})".format(oxygen*co2, oxygen, co2))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Need to pass 'python day03.py sessionId' (Arguments={}, Length={})".format(str(sys.argv), len(sys.argv)))
    else:  
        main()