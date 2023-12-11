import numpy as np

f = open("./in.txt")

matrix = np.array([[1 if x == "#" else 0 for x in l] for l in f.read().splitlines()])

# first let's do some expansion

# expand rows first
i = 0
while i < matrix.shape[0]:
    if np.sum(matrix[i]) == 0:
        matrix = np.insert(matrix, i, 0, axis = 0)
        i += 1
    i += 1

# expand columns
i = 0
while i < matrix.shape[1]:
    if np.sum(matrix[:, i]) == 0:
        matrix = np.insert(matrix, i, 0, axis = 1)
        i += 1
    i += 1

# find shortest paths: I think we can use BFS here

galaxy_pos = np.where(matrix == 1)
total = 0
pos = list(zip(list(galaxy_pos[0]), list(galaxy_pos[1])))
for i in range(len(pos)):
    for j in range(i + 1, len(pos)):
        r1, c1 = pos[i]
        r2, c2 = pos[j]
        total += abs(r1 - r2) + abs(c1 - c2)

print(total)
