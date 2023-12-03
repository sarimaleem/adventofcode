from functools import reduce

f = open("./in.txt")

total = 0
for line in f:
    i = line.index(":")
    line = line[i + 2:].strip()
    games = line.split(";")
    draws = [draw.strip() for game in line.split(";") for draw in game.split(",")]
    max_colors = {}
    for draw in draws:
        amt, color = draw.split(" ")
        if color not in max_colors or max_colors[color] < int(amt):
            max_colors[color] = int(amt)
    power = reduce(lambda x, y: x * y, max_colors.values(), 1)
    total += power

print(total)
