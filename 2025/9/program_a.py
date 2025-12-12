def find_area(tile_a, tile_b):
    x1, y1 = tile_a
    x2, y2 = tile_b
    return (abs(x2-x1)+1) * (abs(y2-y1)+1)

def solve():
    with open("input.txt") as f:
        text = f.readlines()

    red_tiles = []
    for line in text:
        line = line[:-1]
        x, y = line.split(",")
        x, y = int(x), int(y)
        red_tiles.append((x, y))

    squares = [(i, j, find_area(i, j)) for i in red_tiles for j in red_tiles]
    squares.sort(key=lambda x: -x[2])
    print(squares[0])

solve()