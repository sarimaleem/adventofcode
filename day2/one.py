max_colors = {"red": 12, "green": 13, "blue": 14}

f = open("./in.txt")

game_num = 1
total = 0
for line in f:
    i = line.index(":")
    line = line[i + 2:].strip()
    games = line.split(";")
    draws = [draw.strip() for game in line.split(";") for draw in game.split(",")]
    max_found = any([int(amt) > max_colors[color] for draw in draws for amt, color in [draw.split(" ")]])
    total += game_num if not max_found else 0
    game_num += 1

print(total)

