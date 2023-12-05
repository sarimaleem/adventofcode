f = open("./in.txt")

l = f.readline()
_, numbers = l.split(":")
seeds = [int(n) for n in numbers.split()]
maps = f.read().split("\n")


def map_numbers(seed, maps):
    for map in maps:
        dest, source, length = map
        if seed in range(source, source + length):
            return dest + seed - source
    return seed

i = 0
while i < len(maps):
    i += 2 # eliminate space and and text
    current_maps = []
    while i < len(maps) and maps[i] != "":
        current_maps.append([int(x) for x in maps[i].split()])
        i += 1

    seeds = list(map(lambda x: map_numbers(x, current_maps), seeds))

print(min(seeds))
