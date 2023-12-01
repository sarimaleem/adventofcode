file = open("./in.txt")

m = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

sum = 0

for line in file:
    first_digit = -1
    last_digit = -1

    for i in range(len(line)):
        if line[i].isdigit():
            first_digit = int(line[i])

        for (key, val) in m.items():
            if line[i:].startswith(key):
                first_digit = val

        if first_digit != -1:
            break


    for i in range(len(line) -1, -1, -1):
        if line[i].isdigit():
            last_digit = int(line[i])

        for (key, val) in m.items():
            if line[i:].startswith(key):
                last_digit = val

        if last_digit != -1:
            break

    sum += 10 * first_digit + last_digit
print(sum)
