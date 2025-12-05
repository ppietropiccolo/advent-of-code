def solve():
    # set approash unfeasible, the ranges are too large

    with open("input.txt") as f:
        text = f.readlines()
    fresh = set()
    available = set()
    available_fresh = set()

    for line in text:
        line = line[:-1]
        if "-" in line:
            start, end = line.split("-")
            start, end = int(start), int(end)
            fresh.add((start, end))
        elif len(line) > 0:
            ingredient = int(line)
            available.add(ingredient)
    # [print(i) for i in available]

    for ingredient in available:
        for start, end in fresh:
            if start <= ingredient <= end:
                available_fresh.add(ingredient)
                break
    
    print(len(available_fresh))

solve()