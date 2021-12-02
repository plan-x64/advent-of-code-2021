from collections import deque
import itertools
import sys
import urllib.request

def gather_input_data(url, sessionId):
    request = urllib.request.Request(url)
    request.add_header("cookie", "session={}".format(sessionId)) # Source the data directly from AoC

    values = []
    with urllib.request.urlopen(request) as data:
        for line in data:
            number = int(str(line, "utf-8"))
            values.append(number)

    return values

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

def main(values):
    last_sum = None
    inc_count = 0
    for current_sum in rolling_sum(values):
        if last_sum is None:
            print("{} (N/A - no previous sum)".format(current_sum))
        else:
            if last_sum < current_sum:
                inc_count += 1
                print("{} (increased)".format(current_sum))
            elif last_sum > current_sum:
                print("{} (decreased)".format(current_sum))
            else:
                print("{} (no change)".format(current_sum))
        last_sum = current_sum

    print("Number of larger values: " + str(inc_count))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Need to pass 'python part2.py sessionId' (Arguments={}, Length={})".format(str(sys.argv), len(sys.argv)))
    else:  
        sessionId = sys.argv[1]  
        url = "https://adventofcode.com/2021/day/1/input"
        main(gather_input_data(url, sessionId))
