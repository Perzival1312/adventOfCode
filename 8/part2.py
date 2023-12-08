# --- Part Two ---

# The sandstorm is upon you and you aren't any closer to escaping the wasteland.
# You had the camel follow the instructions, but you've barely left your starting position.
# It's going to take significantly more steps to escape!

# What if the map isn't for people - what if the map is for ghosts?
# Are ghosts even bound by the laws of spacetime? Only one way to find out.

# After examining the maps a bit longer, your attention is drawn to a curious fact:
# the number of nodes with names ending in A is equal to the number ending in Z!
#  If you were a ghost, you'd probably just start at every node that ends with A
#  and follow all of the paths at the same time until they all simultaneously end up at nodes that end with Z.

# For example:

# LR

# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)

# Here, there are two starting nodes, 11A and 22A (because they both end with A).
# As you follow each left/right instruction, use that instruction to simultaneously
# navigate away from both nodes you're currently on. Repeat this process until all
# of the nodes you're currently on end with Z. (If only some of the nodes you're on
# end with Z, they act like any other node and you continue as normal.)
#  In this example, you would proceed as follows:

#     Step 0: You are at 11A and 22A.
#     Step 1: You choose all of the left paths, leading you to 11B and 22B.
#     Step 2: You choose all of the right paths, leading you to 11Z and 22C.
#     Step 3: You choose all of the left paths, leading you to 11B and 22Z.
#     Step 4: You choose all of the right paths, leading you to 11Z and 22B.
#     Step 5: You choose all of the left paths, leading you to 11B and 22C.
#     Step 6: You choose all of the right paths, leading you to 11Z and 22Z.

# So, in this example, you end up entirely on nodes that end in Z after 6 steps.

# Simultaneously start on every node that ends with A.
# How many steps does it take before you're only on nodes that end with Z?

RL_map = {'R':1, 'L':0}
direction_arr = []
location_map = {}

with open('real.txt', 'r') as p:
    for direction in p.readline().strip():
        direction_arr.append(RL_map[direction])
    # skip empty line
    p.readline()

    for locations in p.readlines():
        origin = locations.strip().split(' = ')[0]
        destination0 = locations.strip().split(' = ')[1].split(', ')[0][1:]
        destination1 = locations.strip().split(' = ')[1].split(', ')[1][:-1]
        location_map[origin] = (destination0, destination1)

starting_points = {}
ending_points = {}

for locations in location_map.keys():
    if list(locations)[2] == 'A':
        starting_points[locations] = []
    elif list(locations)[2] == 'Z':
        ending_points[locations] = False

for l in starting_points.keys():
    location = l
    steps = 0
    found = False
    while not found and steps <= 1_000_000:
        for direction in direction_arr:
            steps += 1
            location = location_map[location][direction]
            if location in ending_points and not ending_points[location]:
                ending_points[location] = True
                starting_points[l].append(steps)
                for ends in ending_points.values():
                    if not ends:
                        break
                    found = True
                break
    else:
        for k in ending_points.keys():
            ending_points[k] = False


def is_prime(a):
    if a <= 2:
        return True
    elif a != 2 and a % 2 == 0:
        return False
    else:
        return all(a % i for i in range(3, int(a**0.5)+1))

PRIMES = [i for i in range(2, 100_000) if is_prime(i)]

def prime_factors(n):
    num = n
    factors = []
    i = 0
    while i < len(PRIMES):
        if is_prime(num):
            factors.append(int(num))
            return factors
        prime = PRIMES[i]
        if num % prime == 0:
            factors.append(prime)
            num = num/prime
            i = -1
        i += 1
    else:
        return []

factors = set()
lcm = 1

for num in starting_points.values():
    for i in prime_factors(num[0]):
        factors.add(i)

for factor in factors:
    lcm *= factor

print(lcm)
