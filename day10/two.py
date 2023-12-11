import sys

sys.setrecursionlimit(100000)
f = open("./ex.txt")

maze = f.read().splitlines()

rs, cs = 0, 0

for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == "S":
            rs, cs = i, j

rstart, cstart = rs, cs

m, n = len(maze), len(maze[0])
visited = set()
visited.add((rs, cs))

# . | - F 7 L J
mappings = {
    "|": [(-1, 0), (1, 0)],
    "-": [(0, -1), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
    "L": [(-1, 0), (0, 1)],
    "7": [(0, -1), (1, 0)],
}

# since we're starting we gotta figure out which of the two match up:
# for the right side

if maze[rs + 1][cs] == "|" or maze[rs + 1][cs] == "L" or maze[rs + 1][cs] == "J":
    rs = rs + 1
elif maze[rs - 1][cs] == "|" or maze[rs - 1][cs] == "7" or maze[rs - 1][cs] == "F":
    rs = rs - 1
elif maze[rs][cs - 1] == "-" or maze[rs][cs - 1] == "L" or maze[rs][cs - 1] == "F":
    cs = cs - 1
elif maze[rs][cs + 1] == "-" or maze[rs][cs + 1] == "7" or maze[rs][cs + 1] == "J":
    cs = cs + 1

prev_len = 0
while prev_len != len(visited):
    prev_len = len(visited)
    visited.add((rs, cs))
    if maze[rs][cs] == "S":
        break
    dirs = mappings[maze[rs][cs]]
    diff_i = 0
    if (rs + dirs[diff_i][0], cs + dirs[diff_i][1]) in visited:
        diff_i = 1
    rs, cs = (rs + dirs[diff_i][0], cs + dirs[diff_i][1])

##################################################### Part 2
floodfill = [[False for _ in range(n)] for _ in range(m)]

def is_valid(r, c, m, n):
    if r >= 0 and c >= 0 and r < m and c < n:
        return True
    return False

def dfs(cur, floodfill, visited):
    xdirs = [-1, 1, 0, 0]
    ydirs = [0, 0, -1, 1]
    for i in range(len(xdirs)):
        new_dir = (cur[0] + xdirs[i], cur[1] + ydirs[i])
        if (
            is_valid(new_dir[0], new_dir[1], m, n)
            and not new_dir in visited
            and not floodfill[new_dir[0]][new_dir[1]]
        ):
            floodfill[new_dir[0]][new_dir[1]] = True
            dfs(new_dir, floodfill, visited)

dfs((rstart, cstart), floodfill, visited)
for i in range(m):
    for j in range(n): 
        dfs((i, j), floodfill, visited)

# total = 0
# for i in range(m):
#     for j in range(n):
#         if not floodfill[i][j] and maze[i][j] == ".":
#             total += 1

# total = 0
# for i in range(m):
#     for j in range(n):
#         if floodfill[i][j] and (i, j) not in visited:
#             total += 1

def pretty_print(matrix):
    for row in matrix:
        print("".join(map(lambda x: "Y" if x == True else ".", row)))

pretty_print(floodfill)
print(sum([sum(x) for x in floodfill]))
