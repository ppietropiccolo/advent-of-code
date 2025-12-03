with open("input.txt") as f:
    text = f.readlines()

rotations = [(line[0], int(line[1:-1])) for line in text]

position = 50
counter = 0
counter_while = 0
errors_counter = 0

for rotation in rotations:
    direction, clicks = rotation
    initial_position = position
    pos = initial_position; increase = 1; zeros_hit_while = 0

    if direction == "L":
        clicks = -clicks
        increase = -1

    for _ in range(abs(clicks)):
        pos += increase
        if pos == 100:
            pos = 0
        if pos == -1:
            pos = 99
        if pos == 0:
            zeros_hit_while += 1

    zeros_hit = abs((position + clicks) // 100)
    position = (position + clicks) % 100 # this is always correct
    
    if direction == "L" and initial_position == 0:
        zeros_hit -= 1
    if direction == "L" and position == 0:
        zeros_hit += 1

    # if position == 0: # 1005 total cases, 1100 fail
    if (zeros_hit_while != zeros_hit) and (direction == "L") and (position != 0):
        # either happens to be greater than the other, but difference is max 1
        # always direction == "L" -> also position == 0
        # fails basically in 2 cases
        #  - x -> L -> 0: counts 0
        #  - 0 -> L -> x, counts 1 
        print(initial_position, rotation, position, zeros_hit, zeros_hit_while)
        errors_counter += 1

    counter += zeros_hit
    counter_while += zeros_hit_while

print(counter_while, counter, errors_counter)