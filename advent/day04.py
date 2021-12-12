import adventutils
import itertools
import sys

def parse_input(input):
    drawn_nums = [int(x) for x in input[0].split(",")]
    boards = parse_boards(input[2:])
    return (drawn_nums, boards)

def parse_boards(input):
    groups = (list(group) for key, group in itertools.groupby(input, key = lambda x: x != '') if key)
    return [[list(map(lambda x: int(x), str.split())) for str in group] for group in groups]

def check_board(drawn_nums, board):
    for row in board:
        matched_nums = set(row).intersection(drawn_nums)
        if len(matched_nums) == len(row):
            return True

    for column in list(zip(*board)):
        matched_nums = set(column).intersection(drawn_nums)
        if len(matched_nums) == len(column):
            return True

    return False

def drawer(drawn_nums):
    drawn = []
    for num in drawn_nums:
        drawn.append(num)
        yield drawn

def matcher(nums, boards):
    unmatched_boards = boards
    for drawn_nums in drawer(nums):
        for board in unmatched_boards:
            if check_board(drawn_nums, board):
                unmatched_boards.remove(board)
                yield (board, drawn_nums)  

        if len(unmatched_boards) == 0:
            break;
    
def find_first_match(nums, boards):
    return next(matcher(nums, boards))

def find_last_match(nums, boards):
    results = [match for match in matcher(nums, boards)]
    return results[-1] 

def find(draw_nums, boards, match_fn):
    (matched_board, drawn_nums) = match_fn(draw_nums, boards)

    unused_sum= sum([sum([x for x in row if x not in drawn_nums]) for row in matched_board])
    last_drawn = drawn_nums[-1]

    return (unused_sum, last_drawn)

def main():
    sessionId = sys.argv[1]  
    url = "https://adventofcode.com/2021/day/4/input"
    input = adventutils.gather_input_data(url, sessionId)
    
    (drawn_nums, boards) = parse_input(input)
    
    (pt1_unused_sum, pt1_last_drawn) = find(drawn_nums, boards, lambda n,b: find_first_match(n, b))
    print("Part1: {} ({}, {})".format(pt1_unused_sum*pt1_last_drawn, pt1_unused_sum, pt1_last_drawn))

    (pt2_unused_sum, pt2_last_drawn) = find(drawn_nums, boards, lambda n,b: find_last_match(n, b))
    print("Part2: {} ({}, {})".format(pt2_unused_sum*pt2_last_drawn, pt2_unused_sum, pt2_last_drawn))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Need to pass 'python day04.py sessionId' (Arguments={}, Length={})".format(str(sys.argv), len(sys.argv)))
    else:  
        main()