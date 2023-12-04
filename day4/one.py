lines = [line for line in open("./in.txt")]

total = 0
for line in lines:
    i = line.index(":") + 1
    line = line[i:].strip()
    winning_index = line.index("|")
    winning_numbers_string = line[0:winning_index-1].split(" ")
    my_numbers_string = line[winning_index + 1:].split(" ")

    winning = []
    my = []
    for n in winning_numbers_string:
        try: 
            x = int(n)
            winning.append(x)
        except: 
            pass

    for n in my_numbers_string:
        try: 
            x = int(n)
            my.append(x)
        except: 
            pass

    matches = 0
    for n in my:
        if n in winning:
            matches += 1
    if matches >= 1:
        total += 2 ** (matches - 1)

print(total)
