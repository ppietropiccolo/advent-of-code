import numpy as np
from bisect import insort
from collections import defaultdict

def solve():
    with open("input.txt") as f:
        text = f.readlines()

    boxes = [[int(num) for num in line[:-1].split(",")] for line in text]
    boxes = np.array(boxes)
    boxes_x, boxes_y, boxes_z = boxes.T # works 👍

    length = boxes.shape[0] # number of rows, of boxes

    x_matrix = np.full((length, length), boxes_x) #
    y_matrix = np.full((length, length), boxes_y) # try to parallelize all of these
    z_matrix = np.full((length, length), boxes_z) #
    distance = np.sqrt(np.square(x_matrix - x_matrix.T) + np.square(y_matrix - y_matrix.T) + np.square(z_matrix - z_matrix.T))
    # distance += np.diag([np.inf] * length)

    # my personal sort, O(n^2)
    min_1000 = []
    last = np.inf
    for i, row in enumerate(distance):
        for j, element in enumerate(row):
            if i == j: break # ignore the upper triangle of the matrix, it's symmetric
            if element < last:
                insort(min_1000, (element, i, j))
                if len(min_1000) > 1000:
                    min_1000.pop(1)
    print(min_1000)

    # assigning circuits, O(n^2)
    assigned_circuit = [None] * 1000
    last = 1
    for i in range(1000):
        _, start, end = min_1000[i]
        assigned_start = assigned_circuit[start]
        assigned_end = assigned_circuit[end]
        if assigned_start is None and assigned_end is None:
            circuit = last
        elif assigned_start is None:
            circuit = assigned_end
        elif assigned_end is None:
            circuit = assigned_start
        else: # both already part of different circuits
            circuit = assigned_start
            for j in range(1000):
                if assigned_circuit[j] == assigned_end:
                    assigned_circuit[j] = circuit
        assigned_circuit[start] = circuit
        assigned_circuit[end] = circuit
        last += 1
    print(assigned_circuit)

    # making it a dict, O(n)
    circuits_dict = defaultdict(set)
    for box, circuit in enumerate(assigned_circuit):
        if circuit is None:
            circuit = "None"
        circuits_dict[circuit].add(box)

    # [print(i) for i in circuits_dict.items()]

    max_3 = []
    for circ, bx in circuits_dict.items():
        if circ == "None":
            continue
        dimension = len(bx)
        insort(max_3, dimension)
        if len(max_3) > 3: max_3.pop()
    print(max_3)
         


    # distance2 = np.zeros((length, length))
    # for i in range(length): # here i calculate
    #     for j in range(length):
    #         distance2[i,j] = np.sqrt((boxes[i,x]-boxes[j,x])**2 + (boxes[i,y]-boxes[j,y])**2 + (boxes[i,z]-boxes[j,z])**2)
    # distance2 += np.diag([np.inf] * length)
    # print(np.allclose(distance, distance2))

solve()