# --- Day 3: Gear Ratios ---

# You and the Elf eventually reach a gondola lift station; he says the gondola lift
# will take you up to the water source, but this is as far as he can bring you. You go inside.

# It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

# "Aaah!"

# You turn around to see a slightly-greasy Elf with a wrench and a look of surprise.
# "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now;
# it'll still be a while before I can fix it." You offer to help.

# The engineer explains that an engine part seems to be missing from the engine,
# but nobody can figure out which one. If you can add up all the part numbers in
# the engine schematic, it should be easy to work out which part is missing.

# The engine schematic (your puzzle input) consists of a visual representation of the engine.
# There are lots of numbers and symbols you don't really understand, but apparently any number
# adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum.
# (Periods (.) do not count as a symbol.)

# Here is an example engine schematic:

# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..

# In this schematic, two numbers are not part numbers because they are not adjacent to a symbol:
# 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number;
# their sum is 4361.

# Of course, the actual engine schematic is much larger.
# What is the sum of all of the part numbers in the engine schematic?


NUMBERS = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
# char_set = {'-', '=', '$', '&', '%', '/', '@', '+', '*', '#'}
matrix = []
part_nums = []
total = 0
chars = set()

with open('real.txt', 'r') as p:
    for line in p.readlines():
        for char in line.strip():
            chars.add(char)
        matrix.append(list('.'+line.strip()+'.'))
    chars.remove('.')
    char_set = chars.difference(NUMBERS)
    # print(char_set)

for r, row in enumerate(matrix):
    for c, char in enumerate(row):
        if char in char_set:
            # search in circle around spotted symbol
            for i in range(-1, 2):
                for j in range(-1, 2):
                    # print(i, j, r+i, c+j)
                    if matrix[r+i][c+j] in NUMBERS:
                        # found digit near symbol
                        end_of_num = c+j
                        begin_of_num = c+j
                        num = ''
                        # print(char)
                        # look to right for rest of number
                        for k in range(1, 4):
                            if matrix[r+i][c+j+k] in NUMBERS:
                                end_of_num = c+j+k
                            else:
                                break
                        # look to left for rest of number
                        for k in range(1, 4):
                            if matrix[r+i][c+j-k] in NUMBERS:
                                begin_of_num = c+j-k
                            else:
                                break
                        for l in range(begin_of_num, end_of_num+1):
                            num += matrix[r+i][l]
                            matrix[r+i][l] = '.'
                        num = int(num)
                        total += num
                        # print(num)
                        # break
print(total)
