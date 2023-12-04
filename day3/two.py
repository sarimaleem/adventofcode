import copy
f = open("in.txt")

matrix = [[c for c in line.strip()] for line in f]
rows, cols = len(matrix), len(matrix[0])

def get_number(m, i, j, rows, cols):
    if i < 0 or i >= rows or j < 0 or j >= cols:
        return -1
    if not m[i][j].isdigit():
        return -1

    r, c = i, j
    while c - 1 >= 0 and m[r][c - 1].isdigit():
        c -= 1

    result = 0
    while c < cols and m[r][c].isdigit():
        result *= 10
        result += int(m[r][c])
        m[r][c] = '.'
        c += 1
    return result


total = 0
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == '*':
            mat_copy = copy.deepcopy(matrix)
            numbers = []
            for delta_x in range(-1, 2):
                for delta_y in range(-1, 2):
                    n = get_number(mat_copy, i + delta_x, j + delta_y, rows, cols)
                    if n != -1:
                        numbers.append(n)

            if len(numbers) == 2:
                total += numbers[0] * numbers[1]


print(total)
