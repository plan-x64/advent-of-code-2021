import adventutils
import sys

def initial_population(input):
    population = [0] * 9
    for fish_age in input:
        population[fish_age] += 1
    
    return population

def grow_population(initial, days_to_grow):
    """
    Track the fish population growth from an initial population, growing over days_to_grow number of days. 
    To make this efficient two optimizations have been made:

    1. Instead of tracking individual fish (which doubles every approx. 8 days which will result O(10^9)
    fish over 256 days), we instead compute the sum of fish with the same due date and use the due date
    as the offset into the current popluation list. For example, if 5 fish have a timer of 1 and 2 fish
    have a timer of 4 the population would be tracked as: [0, 5, 0, 0, 2, 0, 0, 0, 0]
        
    2. Modulo arithmetic is used instead of fully iterating through the entire list to decrement the due 
    date of each fish every day. Using modula arithmetic provides a projection into the fish data that
    looks like its changing each day without needing O(n) operations and instead we can update the list
    in constant time regardless of the number of different ages for fish.
    """

    current = list(initial)

    if days_to_grow == 0:
        return current

    for day in range(0, days_to_grow):
        due_index = day % 9
        due_count = current[due_index]

        current[(day+7)%9] += due_count
        current[(day+9)%9] += due_count        
        current[due_index] = max(0, current[due_index] - due_count)
        
    return current

def main():
    sessionId = sys.argv[1]  
    url = "https://adventofcode.com/2021/day/6/input"
    transform = lambda x: [int(day) for day in str(x, "utf-8").split(',')]
    input = next(iter(adventutils.gather_input_data(url, sessionId, transform)))

    print("Part1: {}".format(sum(grow_population(initial_population(input), 80))))
    print("Part2: {}".format(sum(grow_population(initial_population(input), 256))))
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Need to pass 'python day06.py sessionId' (Arguments={}, Length={})".format(str(sys.argv), len(sys.argv)))
    else:  
        main()
        