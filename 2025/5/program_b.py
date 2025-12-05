def included(new: tuple[int, int], old: tuple[int, int]):
    new_start, new_end, old_start, old_end = new, old
    if new_end < old_start or new_start > old_end: # range completely outside
        return "to add entirely"
    if new_start < old_start and new_end > old_end: # starts before, ends inside 
    if new_start > old_start and new_end < old_end: # completely included
    if new_start > old_start and new_end > old_end: 

def solve():
    # i think it's better to only work with start and end indexes

    with open("input.txt") as f:
        text = f.readlines()
    fresh: list[tuple[int, int]] = []

    for line in text:
        line = line[:-1]
        if "-" not in line:
            break
        new_start, new_end = line.split("-")
        new_start, new_end = int(new_start), int(new_end)

        to_count = "yes"
        for start, end in fresh:
            if start <= new_start and new_end <= end:
                to_count = "no"
            elif new_start <= start and :



solve()