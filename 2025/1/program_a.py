with open("input.txt") as f:
    text = f.readlines()

rotations = [(line[0], int(line[1:-1])) for line in text]

position = 50
counter = 0

for rotation in rotations:
    direction, clicks = rotation
    if direction == "L":
        clicks = -clicks
    position = (position + clicks) % 100
    if position == 0:
        counter += 1

print(counter)