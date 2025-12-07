import numpy as np

def solve():
    with open("input.txt") as f:
        matrix = [[c for c in line[:-1]] for line in f.readlines()]
    
    counter = 0
    rays = {"S", "|"}
    for i, line in enumerate(matrix[1:]): # skip the first row
        # assert len(line) == dimension # good 👍
        for j, element in enumerate(line):
            upper = matrix[i-1][j]
            if upper not in rays:
                continue
            if element == "^": # splitter
                matrix[i][j-1] = "|" # make previous element a ray
                matrix[i][j+1] = "|" # make next element a ray
                counter += 1
            else: # ray above and element is "."
                matrix[i][j] = "|" # make the upper ray continue


                
    print(counter)

def numpy_solve():
    with open("input.txt") as f:
        matrix = [[c for c in line[:-1]] for line in f.readlines()]
    matrix = np.array(matrix)

    ray_above = np.zeros(matrix.shape)
    # ray_above[1:, ...] = matrix[:-1, ...] in {"S", "|"}
    print(ray_above[1])

solve()