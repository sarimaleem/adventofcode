import math
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

def find_first_z(start):
    steps = 0
    found = False
    while not found:
        for dir in rl:
            p = 0 if dir == "L" else 1
            start = adj[start][p]
            steps += 1
            if start.endswith("Z"):
                found = True
                break
    return steps

starts = [x for x in adj.keys() if x.endswith("A")]
firsts = list(map(lambda x: find_first_z(x), starts))
print(math.lcm(*firsts))
