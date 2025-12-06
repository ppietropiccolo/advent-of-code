import numpy as np

def solve():
    with open("input.txt") as f:
        text = f.readlines()

    data = []
    for line in text:
        line = line[:-1] # remove ending \n
        line = line[::-1] # invert line
        line = [char for char in line] # make it a list of characters
        data.append(line) # add it to data
    row_len = len(data[0]) # store row length
    data = np.array(data) # make it a numpy matrix
    # print(data[..., :18])

    solutions: list[list] = []
    prev = []
    for i in range(row_len):
        col = data[..., i] # take ith column
        if "".join(col) == "     ": # if empty column
            prev = [] # reset the list of previous
            continue  # and go on
        # if the column is not empty
        number = int("".join(col[:-1]))
        prev.append(number)
        if col[-1] == "+":
            solutions.append(int(np.sum(prev)))
        elif col[-1] == "*":
            solutions.append(int(np.prod(prev)))
    
    print(solutions)
    print(sum(solutions))

solve()