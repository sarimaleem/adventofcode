f = open("./in.txt")

maze = f.read().splitlines()

rs, cs = 0, 0

for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == "S":
            rs, cs = i, j

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

print(len(visited) // 2)
print(len(visited))
