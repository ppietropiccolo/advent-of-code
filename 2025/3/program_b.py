# it works but i don't really know why
# and it is O(n) ez

import numpy as np

def find_max_joltage(bank): # dynamic programming ?
    assert len(bank) == 100

    bank = [int(i) for i in bank] # convert to list[int]
    digits = np.zeros(12, dtype=np.int32)

    # for i, current_digit in enumerate(bank[:-11]): # exclude the last eleven
    for i in range(len(bank) - 11): # last index for 40 elements: 39 - 11 = 28 -> range = (28 - 39) -> [27+7 : 27+13=40] = [34:40] -> []
        for j in range(12):
            if digits[j] < bank[i+j]: # ex: digits[7] < bank[26]
                digits[j:] = bank[i+j : i+12] # if last element -> i = len - 11 -> bank[len-11+j : len-11+13]
                break
    return int("".join([str(digit) for digit in digits]))


def solve():

    with open("input.txt") as f:
        banks = f.readlines()

    result = []
    for bank in banks:
        joltage = find_max_joltage(bank[:-1])
        result.append(joltage)
    
    # print(result)
    print(sum(result))

solve()