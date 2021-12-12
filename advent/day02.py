import adventutils
import sys

class Tracker:
    def __init__(self):
        self.x = 0
        self.y = 0

    def parse(self, command):
        (action, amount) = command

        if action == 'forward':
            self.x += amount
        elif action == 'up':
            self.y = max(self.y-amount, 0) # our sub cannot fly?
        elif action == 'down':
            self.y += amount
        else:
            raise NotImplementedError("unsupported action {}".format(action))

class BetterTracker:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.aim = 0

    def parse(self, command):
        (action, amount) = command

        if action == 'forward':
            self.x += amount
            self.y = max(0, self.y + (self.aim * amount)) # our sub cannot fly?
        elif action == 'up':
            self.aim -= amount
        elif action == 'down':
            self.aim += amount
        else:
            raise NotImplementedError("unsupported action {}".format(action))


def parse_input(line):
    vals = str(line, "utf-8").split()
    return (vals[0], int(vals[1]))

def calculate_position(values, tracker):
    for value in values:
        tracker.parse(value)

    return (tracker.x, tracker.y)

def print_value(result):
    print("(x={},y={}) {}".format(result[0], result[1], (result[0] * result[1])))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Need to pass 'python day02.py sessionId' (Arguments={}, Length={})".format(str(sys.argv), len(sys.argv)))
    else:  
        sessionId = sys.argv[1]  
        url = "https://adventofcode.com/2021/day/2/input"
        transform = lambda x: (str(x, "utf-8").split()[0], int(str(x, "utf-8").split()[1]))
        values = adventutils.gather_input_data(url, sessionId, transform)

        part1_result = calculate_position(values, Tracker())
        print_value(part1_result)

        part2_result = calculate_position(values, BetterTracker())
        print_value(part2_result)