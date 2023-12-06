f = open("./in.txt")
times = [int(x) for x in f.readline().split(":")[1].split()]
distances = [int(x) for x in f.readline().split(":")[1].split()]

n = len(times)
result = 1
for i in range(n):
    time = times[i]
    distance = distances[i]
    total = 0
    for j in range(time):
        if j * (time - j) > distance:
            total += 1
    result *= total

print(result)
