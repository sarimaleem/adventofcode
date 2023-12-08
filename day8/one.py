from collections import defaultdict

f = open("./in.txt")

rl = f.readline().strip()
f.readline()

adj = defaultdict(list)
for line in f:
    line = line.strip()
    l, r = line.split("=")
    l = l.strip()
    r = r.strip()
    left, right = r[1:-1].split(", ")
    adj[l].append(left)
    adj[l].append(right)

steps = 0
current = "AAA"
found = False
starts = [x for x in adj.keys() if x.endswith("A")]
while not found:
    for dir in rl:
        if dir == "L":
            current = adj[current][0]
        elif dir == "R":
            current = adj[current][1]
        steps += 1
        if current == "ZZZ":
            found = True
            print(current, steps)
