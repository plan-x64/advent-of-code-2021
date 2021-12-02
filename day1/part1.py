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

def main(values):
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

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Need to pass 'python part2.py sessionId' (Arguments={}, Length={})".format(str(sys.argv), len(sys.argv)))
    else:  
        sessionId = sys.argv[1]  
        url = "https://adventofcode.com/2021/day/1/input"
        main(gather_input_data(url, sessionId))