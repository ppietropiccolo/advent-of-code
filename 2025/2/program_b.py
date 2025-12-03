from math import sqrt
from textwrap import wrap

def all_divisors(n):
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            yield i

def dynamically_equal(string) -> bool:
    step = 1
    length = len(string)
    if length == 1:
        return False
    if length == 2:
        return string[0] == string[1]
    for step in range(1, length//2 + 1): # i tried using sqrt as limit, but it is wrong!
        # print(step)
        if length % step != 0:
            continue # ignore case where length is not divisible by step
        magic_set = set(wrap(string, step))
        # print(magic_set)
        if len(magic_set) == 1:
            return True
    return False
    
def stupid_equal(string):
    length = len(string)
    if length == 1:
        return False
    for step in range(1, length//2 + 1):
        if length % step != 0:
            continue
        magic_set = set(wrap(string, step))
        if len(magic_set) == 1:
            # print(magic_set, string)
            return True
    return False

def solve():

    with open("input.txt") as f:
        text = f.read()

    ranges = text.split(",")
    invalid_IDs = set()

    for rng in ranges:
        start, end = rng.split("-")
        start, end = int(start), int(end)
        for number in range(start, end+1):
            number = str(number)
            # length = len(number)
            assert number[0] != "0"
            stupid = stupid_equal(number)
            # dynamic = dynamically_equal(number)
            # if stupid != dynamic:
            #     print(f"stupid: {stupid}, dynamic: {dynamic}, number: {number}")
            if stupid:
                invalid_IDs.add(int(number))

    print(sum(invalid_IDs))

# num = "92569256"
# print(stupid_equal(num))
# print(dynamically_equal(num))
solve() # zio pera 22 secondi