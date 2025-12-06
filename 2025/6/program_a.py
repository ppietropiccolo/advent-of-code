import numpy as np

def solve():
    with open("input.txt") as f:
        text = f.readlines()
    
    data = []
    for line in text:
        line = line.strip().split()
        data.append(line)
    n_of_problems = len(data[0])
    data = np.array(data)

    result = np.zeros(n_of_problems, dtype=np.int64)
    for i in range(n_of_problems): # horizontal indexing
        numbers = np.array([int(number) for number in data[:-1, i]])
        operator = data[-1, i]
        solution = numbers.sum() if operator == "+" else numbers.prod()
        result[i] = solution
    print(result.sum())


solve()