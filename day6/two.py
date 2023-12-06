f = open("./in.txt")
time = int(''.join(f.readline().split(":")[1].split()))
distance = int(''.join(f.readline().split(":")[1].split()))


total = 0
for j in range(time):
    if j * (time - j) > distance:
        total += 1
print(total)
