import numpy as np

def solve():
    with open("input.txt") as f:
        text = f.readlines()

    boxes = [[int(num) for num in line[:-1].split(",")] for line in text]
    boxes = np.array(boxes)
    boxes_x, boxes_y, boxes_z = boxes.T # works 👍



    x,y,z = 0,1,2
    length = boxes.shape[0] # number of rows, of boxes

    x_matrix = np.full((length, length), boxes_x)
    y_matrix = np.full((length, length), boxes_y)
    z_matrix = np.full((length, length), boxes_z)
    distance = np.sqrt(np.square(x_matrix - x_matrix.T) + np.square(y_matrix - y_matrix.T) + np.square(z_matrix - z_matrix.T))

    # distance2 = np.zeros((length, length))
    # for i in range(length): # here i calculate
    #     for j in range(length):
    #         distance2[i,j] = np.sqrt((boxes[i,x]-boxes[j,x])**2 + (boxes[i,y]-boxes[j,y])**2 + (boxes[i,z]-boxes[j,z])**2)
    # distance2 += np.diag([np.inf] * length)

    print(np.allclose(distance, distance2))

solve()