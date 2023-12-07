from collections import defaultdict
from functools import cmp_to_key

f = open("./in.txt")

pairs = [line.strip().split(" ") for line in f]
order = "AKQT98765432J"

def ranking(a):
    count_non_jokers = defaultdict(int)
    for c in a:
        if c != 'J':
            count_non_jokers[c] += 1

    jokers = sum([x == 'J' for x in a])
    if jokers == 5:
        return 7

    v = list(count_non_jokers.values())

    # five of a kind
    max_non_jokers = max(v)

    if max_non_jokers + jokers == 5:
        return 7

    # four of a kind
    if max_non_jokers + jokers == 4: 
        return 6

    # full house
    if (3 in v and 2 in v) or (sum([x == 2 for x in v]) == 2 and jokers == 1):
        return 5

    # three of a kind
    if max_non_jokers + jokers == 3:
        return 4

    # i think this is correct? 
    if sum([x == 2 for x in v]) == 2:
        return 3

    # pair
    if 2 in v or jokers == 1:
        return 2

    # high card
    return 1


def break_tie(a, b):
    for i in range(len(a)):
        a_rank = order.index(a[i])
        b_rank = order.index(b[i])
        if a_rank < b_rank:
            return 1
        elif a_rank > b_rank:
            return -1
    return 0

# def break_tie(a, b):
#     for i in range(len(a)):
#         ac = order.index(a[i])
#         bc = order.index(b[i])
#         if ac != bc:
#             if ac < bc:
#                 return 1
#             else:
#                 return -1

#     print("Cannot Reach")
#     return 0

def compare(a, b):
    hand_1 = a[0]
    hand_2 = b[0]
    ra = ranking(hand_1)
    rb = ranking(hand_2)
    if ra != rb:
        return ra - rb
    else:
        return break_tie(hand_1, hand_2)

s = sorted(pairs, key=cmp_to_key(compare))

total = 0
for i in range(len(s)):
    total += (i + 1) * int(s[i][1])

print(total)
# pairs.sort(key=compare)