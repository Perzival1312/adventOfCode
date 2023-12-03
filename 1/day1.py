# --- Day 1: Trebuchet?! ---

# Something is wrong with global snow production, and you've been selected to take a look.
# The Elves have even given you a map; on it,
# hey've used stars to mark the top fifty locations that are likely to be having problems.

# You've been doing this long enough to know that to restore snow operations,
# you need to check all fifty stars by December 25th.

# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar;
# the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

# You try to ask why they can't just use a weather machine ("not powerful enough")
# and where they're even sending you ("the sky") and why your map looks mostly blank
# ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from")
# when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

# As they're making the final adjustments, they discover that their calibration document (your puzzle input)
# has been amended by a very young Elf who was apparently just excited to show off her art skills.
# Consequently, the Elves are having trouble reading the values on the document.

# The newly-improved calibration document consists of lines of text; each line originally contained
# a specific calibration value that the Elves now need to recover. On each line,
# the calibration value can be found by combining the first digit and the last digit
# (in that order) to form a single two-digit number.

# For example:

# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet

# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

# Consider your entire calibration document. What is the sum of all of the calibration values?

NUMBERS = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}

total = 0
with open('day1.txt', 'r') as p:
    for word in p.readlines():
        leftmost = -1
        rightmost = -1
        for char in word:
            if char in NUMBERS:
                if leftmost == -1:
                    leftmost = int(char)
                    rightmost = int(char)
                else:
                    rightmost = int(char)
        num = leftmost*10 + rightmost
        total += num

print(total)


# nums = []
# with open('day1.txt', 'r') as p:
#     for word in p.readlines():
#         number = ''
#         # print(word)
#         for char in word:
#             # print(char)
#             if char in NUMBERS:
#                 number += char
#                 break
#                 # print(number, char)
#         for i in range(len(word)-1, -1, -1):
#             char = word[i]
#             if char in NUMBERS:
#                 number += char
#                 break
#         print(word, number, int(number[0])*10 + int(number[-1]))
#         nums.append(int(number[0])*10 + int(number[-1]))
#         total += int(number[0])*10 + int(number[-1])

# for num in nums:
#     total += num
# print(total)
