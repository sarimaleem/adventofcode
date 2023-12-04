f = open("in.txt")

matrix = [line.strip() for line in f]
rows, cols = len(matrix), len(matrix[0])
numbers = [[False for _ in range(cols)] for _ in range(rows)]

def is_symbol(c: str):
    if c.isdigit() or c == ".":
        return False
    return True

def annotate(bool_matrix, i, j):
    global rows
    global cols
    r, c = i, j
    if i == -1:
        print("hi")
    while c >= 0 and matrix[r][c].isdigit():
        bool_matrix[r][c] = True
        c -= 1

    c = j
    while c < cols and matrix[r][c].isdigit():
        bool_matrix[r][c] = True
        c += 1

for i in range(rows):
    for j in range(cols):
        if is_symbol(matrix[i][j]):
            for delta_x in range(-1, 2):
                for delta_y in range(-1, 2):
                    annotate(numbers, i + delta_x, j + delta_y)

total = 0

i = 0
while i < rows:
    j = 0
    while j < cols:
        if numbers[i][j]:
            temp = 0
            while j < cols and numbers[i][j]:
                temp *= 10
                temp += int(matrix[i][j])
                j += 1
            total += temp
        j += 1
    i += 1

print(total)


