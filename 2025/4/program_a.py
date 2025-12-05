import numpy as np

def convolution(matrix):
    padded = np.pad(matrix, 1)
    kernel = np.array([[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]])
    
    n_neighbors = np.zeros(matrix.shape, dtype=np.uint8)
    for i in range(n_neighbors.shape[0]):
        for j in range(n_neighbors.shape[1]):
            n_neighbors[i,j] = np.sum(padded[i:i+3, j:j+3] * kernel)

    print(n_neighbors)
    accessible = matrix * (n_neighbors < 4)
    return accessible

def solve():
    with open("input.txt") as f:
        text = f.readlines()

    rows = []    
    for line in text:
        row = [1 if char == "@" else 0 for char in line[:-1]]
        rows.append(row)

    matrix = np.array(rows)
    result = convolution(matrix)
    print(np.sum(result))

solve()