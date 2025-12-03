# wohoooo!

def find_max_joltage(bank): # dynamic programming ?

    bank = [int(i) for i in bank] # convert to list[int]
    first_digit = 0
    second_digit = 0

    for i, digit in enumerate(bank[:-1]): # exclude the last one
        next = bank[i+1]
        if first_digit < digit: # find a new greater first digit (max)
            first_digit = digit
            second_digit = next # second digit must be the next one
        elif second_digit < next: # didn't change first digit, so we can check if the second is larger
            second_digit = next

    return 10 * first_digit + second_digit

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