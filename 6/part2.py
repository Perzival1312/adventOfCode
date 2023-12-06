# --- Part Two ---

# As the race is about to start, you realize the piece of paper with race times
#  and record distances you got earlier actually just has very bad kerning.
#  There's really only one race - ignore the spaces between the numbers on each line.

# So, the example from before:

# Time:      7  15   30
# Distance:  9  40  200

# ...now instead means this:

# Time:      71530
# Distance:  940200

# Now, you have to figure out how many ways there are to win this single race.
# In this example, the race lasts for 71530 milliseconds and the record distance
# you need to beat is 940200 millimeters. You could hold the button anywhere
# from 14 to 71516 milliseconds and beat the record, a total of 71503 ways!

# How many ways can you beat the record in this one much longer race?

with open('real.txt', 'r') as p:
    times = [int(''.join([i.strip() for i in p.readline().strip().split(':')[1].strip().split('   ')]))]
    distances = [int(''.join([i.strip() for i in p.readline().strip().split(':')[1].strip().split('   ')]))]
print(times, distances)

wins = {}

for i, time in enumerate(times):
    count = 0
    for h in range(1, time):
        if h*(time-h) > distances[i]:
            count += 1
    wins[i] = count

margin = 1
for k, v in wins.items():
    margin*=v
print(margin)
