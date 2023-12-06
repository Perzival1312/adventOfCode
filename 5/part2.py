# --- Part Two ---

# Everyone will starve if you only plant such a small number of seeds.
# Re-reading the almanac, it looks like the seeds: line actually describes ranges of seed numbers.

# The values on the initial seeds: line come in pairs. Within each pair,
# the first value is the start of the range and the second value is the length of the range.
# So, in the first line of the example above:

# seeds: 79 14 55 13

# This line describes two ranges of seed numbers to be planted in the garden.
# The first range starts with seed number 79 and contains 14 values: 79, 80, ..., 91, 92.
# The second range starts with seed number 55 and contains 13 values: 55, 56, ..., 66, 67.

# Now, rather than considering four seed numbers, you need to consider a total of 27 seed numbers.

# In the above example, the lowest location number can be obtained from seed number 82,
# which corresponds to soil 84, fertilizer 84, water 84, light 77, temperature 45,
# humidity 46, and location 46. So, the lowest location number is 46.

# Consider all of the initial seed numbers listed in the ranges on the first
# line of the almanac. What is the lowest location number that corresponds to any of the initial seed numbers?

# 1 seed-to-soil map:
# 2 soil-to-fertilizer map:
# 3 fertilizer-to-water map:
# 4 water-to-light map:
# 5 light-to-temperature map:
# 6 temperature-to-humidity map:
# 7 humidity-to-location map:

seed_map = {}

almanac = []

with open('real.txt') as p:
    for line in p.readlines():
        almanac.append(line.strip())

seeds_to_find = almanac[0].strip().split(': ')[1].split(' ')
seed_ranges = []

for g, spot in enumerate(seeds_to_find):
    if g%2 == 0:
        seed_ranges.append(int(spot))
    else:
        seed_ranges.append(int(seeds_to_find[g-1])+int(spot)-1)

print(seed_ranges)
# seed_ranges = [858905075, 858905075+56936593]
# seed_ranges = [947763189, 947763189+267019426]
# seed_ranges = [206349064, 206349064+252409474]
# seed_ranges = [660226451, 660226451+92561087]
# seed_ranges = [752930744, 752930744+24162055]   #2002394171
# seed_ranges = [75704321, 75704321+63600948]     #245225896
# seed_ranges = [3866217991, 3866217991+323477533]
# seed_ranges = [3356941271, 3356941271+54368890] #213026178
# seed_ranges = [1755537789, 1755537789+475537300]
seed_ranges = [1327269841, 1327269841+427659734]
ranges = []

for i, line in enumerate(almanac):
    if not line:
        ranges.append(i)

for ind, r in enumerate(ranges):
    seed_map[ind+1] = []
    if len(ranges) == ind+1:
        break
    for i in range(r+1, ranges[ind+1]):
        if almanac[i+1]:
            seed_map[ind+1].append(almanac[i+1])

t_map = {}
seed_map.pop(8)

for k, l in seed_map.items():
    t_map[k] = []
    for num in l:
        i = num.split(' ')
        t_map[k].append(i)

print(t_map)

prod = {}
prod[0] = set()

# for seed in seed_ranges:
for j in range(0, len(seed_ranges), 2):
    sr0 = seed_ranges[j]
    sr1 = seed_ranges[j+1]
    prod[0].add((sr0, sr1))


for i in range(1, 8):
    prod[i] = set()
    for pair in prod[i-1]:
        found = False
        sr0 = pair[0]
        sr1 = pair[1]
        for l in t_map[i]:
            l0 = int(l[0])
            l1 = int(l[1])
            l2 = int(l[2])-1
            diff = l0-l1
            # source starts before dest and end insdide dest range
            if sr0<=l1 and sr1>=l1 and sr1<l1+l2:
                print(sr0, sr1, l, [sr0, l1-1], [l1+diff, sr1+diff], i, 'a')
                prod[i].add((sr0, l1-1))
                prod[i].add((l1+diff, sr1+diff))
                found = True
                continue
            # source starts inside dest range and continues past
            elif sr0>=l1 and sr1>l1+l2 and sr0 < l1+l2:
                print(sr0, sr1, l, [sr0+diff, l1+l2+diff], [l1+l2+1, sr1], i, 'b')
                prod[i].add((sr0+diff, l1+l2+diff))
                prod[i].add((l1+l2+1, sr1))
                found = True
                continue
            # dest range contained within source range
            elif sr0<l1 and sr1>l1+l2:
                print(sr0, sr1, l, [sr0, l1-1], [l1+diff, l1+l2+diff], [l1+l2+1, sr1], i, 'c')
                prod[i].add((sr0, l1-1))
                prod[i].add((l1+diff, l1+l2+diff))
                prod[i].add((l1+l2+1, sr1))
                found = True
                continue
            # source range is contained within the dest range
            elif sr0>=l1 and sr1<=l1+l2:
                print(sr0, sr1, l, [sr0+diff, sr1+diff], i, 'd')
                prod[i].add((sr0+diff, sr1+diff))
                found = True
                continue

        if not found:
            prod[i].add(pair)

# for item in prod[7]:
#     print(item)
print(prod)

lowest = 999999999999999999999999999999999999999999999999999999

for pair in prod[7]:
    if pair[0] < lowest:
        lowest = pair[0]

print(lowest)


#2002394171
#245225896
#213026178
