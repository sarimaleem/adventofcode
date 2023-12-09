f = open("./in.txt")

def apply_dif(l):
    nl = []
    for i in range(1, len(l)):
        nl.append(l[i] - l[i - 1])
    return nl

total = 0
for line in f:
    numbers = [int(x) for x in line.split()]
    diffs = []

    while not all(x == 0 for x in numbers):
        diffs.append(numbers)
        numbers = apply_dif(numbers)

    while len(diffs) != 1:
        last = diffs.pop()
        diffs[-1].insert(0, diffs[-1][0] - last[0])

    value = diffs.pop()[0]
    total += value

print(total)
