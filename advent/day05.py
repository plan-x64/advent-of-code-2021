import adventutils
from collections import Counter
import itertools
import sys

def parse_input(input):
    vectors = []
    for line in input:
        vector = [(int(x), int(y)) for (x,y) in tuple([point.split(',') for point in line.split(" -> ")])]
        vectors.append(vector)
    
    return vectors

def vec_to_pts(vector, include_diagonals):
    ((x1, y1), (x2, y2)) = vector
    if x1 == x2:
        return [(x1, y) for y in (range(y1, y2+1) if y1<y2 else range(y2, y1+1))]
    elif y2 == y1:
        return [(x, y1) for x in (range(x1, x2+1) if x1<x2 else range(x2, x1+1))]
    elif include_diagonals:
        slope = round((y2-y1) / (x2-x1))
        intercept = y2-slope*x2
        return [(x, round(slope*x+intercept)) for x in (range(x1, x2+1) if x1<x2 else range(x2, x1+1))]
    else:
        return []
     
def find_overlap_pts(vectors, include_diagonals):
    all_points = itertools.chain(*[vec_to_pts(vector, include_diagonals) for vector in vectors])
    occurrences = Counter(all_points)
    return [(point, count) for (point, count) in occurrences.items() if count > 1]

def main():
    sessionId = sys.argv[1]  
    url = "https://adventofcode.com/2021/day/5/input"
    input = adventutils.gather_input_data(url, sessionId)
    vecs = parse_input(input)
    
    pt1_overlapped_points = find_overlap_pts(vecs, include_diagonals=False)
    print("Part1: {}".format(len(pt1_overlapped_points)))

    pt2_overlapped_points = find_overlap_pts(vecs, include_diagonals=True)
    print("Part2: {}".format(len(pt2_overlapped_points)))
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Need to pass 'python day05.py sessionId' (Arguments={}, Length={})".format(str(sys.argv), len(sys.argv)))
    else:  
        main()