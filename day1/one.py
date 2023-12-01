file = open("./in.txt")

sum = 0
for line in file: 
    line = [c for c in line if c.isdigit()]
    sum += 10 * int(line[0]) + int(line[-1])
print(sum)

