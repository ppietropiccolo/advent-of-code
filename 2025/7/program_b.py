import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

def solve():
    with open("input.txt") as f:
        matrix = [[c for c in line[:-1]] for line in f.readlines()]
    
    rays = {"S", "|"}
    # matrix = [r[60:80] for r in matrix[:15]] # very useful to debug
    matrix_shape = (len(matrix), len(matrix[0]))
    ways_to_arrive = np.zeros(matrix_shape, dtype=np.int64) # wta: stores the counter of timelines that arrive to each cell

    for i, line in enumerate(matrix):
        if i == 0: # skip the first line
            ways_to_arrive[i, line.index("S")] = 1
            continue
        # assert len(line) == dimension # good 👍
        for j, element in enumerate(line):
            upper = matrix[i-1][j]
            if upper not in rays: # no ray arrives to element: ignore it
                continue
            if element == "^": # splitter: add wta to element to both left and right elements
                matrix[i][j-1] = "|" # make previous element a ray
                ways_to_arrive[i, j-1] += ways_to_arrive[i-1, j] # add wta to upper
                matrix[i][j+1] = "|" # make next element a ray
                ways_to_arrive[i, j+1] += ways_to_arrive[i-1, j] # add wta to upper
            else: # ray above and element is "." or "|" (doesn't matter)
                matrix[i][j] = "|" # make the upper ray continue
                ways_to_arrive[i, j] += ways_to_arrive[i-1, j] # add wta to upper


    with open("output.txt", "w") as f: [print("".join(row), file = f) for row in matrix]
    with open("wta.txt", "w") as f: print(ways_to_arrive, file=f)
    print(ways_to_arrive[-1, ...].sum())

solve()