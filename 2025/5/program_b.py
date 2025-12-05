# this is so messy

def compare(new_range: tuple[int, int], old_range: tuple[int, int]):
    new_start, new_end = new_range
    old_start, old_end = old_range
    overlap = False
    result = new_range
    # what if old range has only one element?

    if new_end < old_start or new_start > old_end: # range completely outside
        return overlap, result
    else:
        overlap = True
        result = min(new_start, old_start), max(new_end, old_end) # overlap
        # print(f"{new_range} overlaps with {old_range} so i will consider only {result}")
        return overlap, result

def solve():
    # i think it's better to only work with start and end indexes

    with open("input.txt") as f:
        text = f.readlines()
    ranges: set[tuple[int, int]] = set()
    fresh: set[tuple[int, int]] = set()


    for line in text:
        line = line[:-1] # remove ending \n
        if "-" not in line: # consider only lines with ranges
            break # and this works ok
        new_range = tuple(int(i) for i in line.split("-")) # convert str -> tuple[int, int]
        ranges.add(new_range) # add to all the ranges
    # ranges set created: only 185 unique ranges

    for new_range in ranges:
        to_remove = set()
        for old_range in fresh: # loop for the ranges already in the set
            overlap, current_range = compare(new_range, old_range) # get a temporary result of the comparison
            if overlap:
                to_remove.add(old_range) # remove the previous one
                new_range = current_range # update the range to be compared with the next ones
        
        fresh.difference_update(to_remove) # remove all conflicting ranges
        fresh.add(new_range)

    result = sum(e-s+1 for s,e in fresh)
    print(result)





solve()