def compare(new_range: tuple[int, int], old_range: tuple[int, int]):
    new_start, new_end = new_range
    old_start, old_end = old_range
    # what if old range has only one element?

    if new_end < old_start or new_start > old_end: # range completely outside
        # print("separated")
        return new_range
    else:
        result = min(new_start, old_start), max(new_end, old_end) # overlap
        print(f"{new_range} overlaps with {old_range} so i will consider only {result}")
        return result

def solve():
    # i think it's better to only work with start and end indexes

    with open("input.txt") as f:
        text = f.readlines()
    fresh: set[tuple[int, int]] = set()

    for line in text:
        line = line[:-1] # remove last \n
        if "-" not in line: # consider only lines with ranges
            break
        new_range = tuple(int(i) for i in line.split("-")) # convert str -> tuple[int, int]
        print(new_range)
        to_remove = set()
        for old_range in fresh: # loop for the ranges already in the set
            current_range = compare(new_range, old_range) # get a temporary result of the comparison
            if current_range != new_range: # if the comparison returned a new interval
                to_remove.add(old_range) # remove the previous one
                new_range = current_range # update the range to be compared with the next ones
        
        fresh.difference_update(to_remove) # remove all conflicting ranges
        fresh.add(new_range) # add the total range, result of the comparisons

    for rng1 in fresh:
        for rng2 in fresh:
            # if rng1 == rng2: continue
            if compare(rng1, rng2) != rng1: # no range should overlap
                print("error!!", rng1, rng2, compare(rng1, rng2))
    # print(fresh)
    result = sum(e-s+1 for s,e in fresh)
    print(result)





solve()