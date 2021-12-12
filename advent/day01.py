import adventutils
from collections import deque
import itertools
import sys

# Modified from https://docs.python.org/3/library/collections.html#collections.deque moving_argerage example
def rolling_sum(iterable, n=3):
    iterator = iter(iterable)
    counter = deque(itertools.islice(iterator, n-1))
    counter.appendleft(0)
    rolling_sum = sum(counter)
    for item in iterator:
        rolling_sum += item - counter.popleft()
        counter.append(item)
        yield rolling_sum

def part1(values):
    last_value = None
    inc_count = 0
    for value in values:
        if last_value is None:
            print("{} (N/A - no previous measurement)".format(value))
        else:
            if last_value < value:
                inc_count += 1
                print("{} (increased)".format(value))
            else:
                print("{} (decreased)".format(value))
        last_value = value

    print("Number of larger values: " + str(inc_count))

    return inc_count

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Need to pass 'python day01.py sessionId' (Arguments={}, Length={})".format(str(sys.argv), len(sys.argv)))
    else:  
        sessionId = sys.argv[1]  
        url = "https://adventofcode.com/2021/day/1/input"
        transform = lambda x: int(str(x, "utf-8"))
        values = adventutils.gather_input_data(url, sessionId, transform)

        part1_count = part1(values)
        part2_count = part1(rolling_sum(values))

        print("{} {}".format(part1_count, part2_count))