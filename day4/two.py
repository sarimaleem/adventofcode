lines = [line for line in open("./in.txt")]

winnings = []
mys = []
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

    winnings.append(winning)
    mys.append(my)

scratch_cards = [1 for _ in range(len(winnings))]
for i in range(len(winnings)):
    num_scratches = scratch_cards[i]

    matches = 0
    for n in mys[i]:
        if n in winnings[i]:
            matches += 1

    j = i + 1
    while j < len(winnings) and j <= i + matches:
        scratch_cards[j] += num_scratches
        j += 1

print(sum(scratch_cards))
