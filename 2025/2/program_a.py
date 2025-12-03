with open("input.txt") as f:
    text = f.read()

ranges = text.split(",")
invalid_IDs = set()

for rng in ranges:
    start, end = rng.split("-")
    start, end = int(start), int(end)
    for number in range(start, end+1):
        number = str(number)
        length = len(number)
        assert number[0] != "0"
        if length % 2 != 0: # skip numbers that don't even divide by 2
            continue
        if number[:length//2] == number[length//2:]:
            invalid_IDs.add(int(number))

print(sum(invalid_IDs))