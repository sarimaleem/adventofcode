f = open("./in.txt")

l = f.readline()
_, numbers = l.split(":")
seeds_ranges = [int(n) for n in numbers.split()]
seed_ranges = [range(a, a + b) for a, b in zip(seeds_ranges[0::2], seeds_ranges[1::2])]
maps = f.read().split("\n")


def find_overlap(range1, range2):
    if range1.stop <= range2.start or range2.stop <= range1.start:
        return None
    return range(max(range1.start, range2.start), min(range1.stop, range2.stop))

# subtract range 1 from range 2
def subtract_range(range1, range2):
    overlap = find_overlap(range1, range2)
    if overlap == None:
        return [range1]

    cuts = []
    if range1.start < overlap.start:
        cuts.append(range(range1.start, overlap.start))

    if range1.stop > overlap.stop:
        cuts.append(range(overlap.stop, range1.stop))

    return cuts



def find_ranges(seed_range, maps):
    new_ranges = []
    original_seeds = [seed_range]
    for map in maps:
        dest, source, length = map
        src_range = range(source, source + length)
        new_seeds = []
        for cur_seed_range in original_seeds:
            overlap = find_overlap(cur_seed_range, src_range)
            if overlap is not None:
                new_dest_range = range(overlap.start - source + dest, overlap.stop - source + dest)
                new_ranges.append(new_dest_range)
            new_seeds.extend(subtract_range(cur_seed_range, src_range))
        original_seeds = new_seeds
    new_ranges.extend(original_seeds)
    return new_ranges

i = 0
while i < len(maps):
    i += 2 # eliminate space and and text
    current_maps = []
    while i < len(maps) and maps[i] != "":
        current_maps.append([int(x) for x in maps[i].split()])
        i += 1


    new_ranges = []
    for seed_range in seed_ranges:
        new_ranges.extend(find_ranges(seed_range, current_maps))
    seed_ranges = new_ranges

smallest = min((map(lambda r: r.start, seed_ranges)))
print(smallest)
