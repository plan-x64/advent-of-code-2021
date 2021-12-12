import adventutils
import sys

def transform_input(line):
    raw_str = str(line, "utf-8").strip('\n').split(' ')
    delimiter_index = raw_str.index('|')
    return ([set(chars) for chars in raw_str[:delimiter_index]], [set(chars) for chars in raw_str[delimiter_index+1:]])

def decode_line(segments):
    (examples, code) = segments
    examples = sorted(examples, key=len)
    examples[3:6] = sorted(examples[3:6], key=lambda x: (examples[1].issubset(x), len(examples[2].intersection(x))))
    examples[6:9] = sorted(examples[6:9], key=lambda x: (examples[2].issubset(x), examples[1].issubset(x)))
    decoded_segments = [examples[index] for index in (7, 0, 3, 5, 2, 4, 6, 1, 9, 8)]

    value = ""
    for num in [set(chars) for chars in code]:
        for index, segment in enumerate(decoded_segments):
            if num == segment:
                value += str(index)
    return int(value)

def main():
    sessionId = sys.argv[1]
    url = "https://adventofcode.com/2021/day/8/input"
    input = adventutils.gather_input_data(url, sessionId, transform=transform_input)

    print("Part 1: {}".format(sum([len(list(filter(lambda x: len(x) in (2,3,4,7), val))) for (_, val) in input])))
    print("Part 2: {}".format(sum([decode_line(line) for line in input])))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Need to pass 'python day08.py sessionId' (Arguments={}, Length={})".format(str(sys.argv), len(sys.argv)))
    else:  
        main()