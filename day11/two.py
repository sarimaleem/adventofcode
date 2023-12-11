import numpy as np
import copy

f = open("./in.txt")

matrix = np.array([[1 if x == "#" else 0 for x in l] for l in f.read().splitlines()])
m, n = matrix.shape

i = 0
r, c = np.where(matrix == 1)
positions = list(zip(r, c))
transformed = copy.deepcopy(positions)
factor = 1000000

# expand rows
for i in range(m):
    if np.sum(matrix[i]) == 0:
        for j in range(len(transformed)):
            if positions[j][0] > i:
                transformed[j] = (transformed[j][0] + factor - 1, transformed[j][1])

# expand columns
for i in range(n):
    if np.sum(matrix[:, i]) == 0:
        for j in range(len(transformed)):
            if positions[j][1] > i:
                transformed[j] = (transformed[j][0], transformed[j][1] + factor - 1)

total = 0
for i in range(len(transformed)):
    for j in range(i + 1, len(transformed)):
        r1, c1 = transformed[i]
        r2, c2 = transformed[j]
        total += abs(r1 - r2) + abs(c1 - c2)

print(total)
