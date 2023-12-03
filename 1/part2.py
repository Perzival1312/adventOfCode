# --- Part Two ---

# Your calculation isn't quite right. It looks like some of the
# igits are actually spelled out with letters: one, two, three,
# our, five, six, seven, eight, and nine also count as valid "digits".

# Equipped with this new information, you now need to find the
# real first and last digit on each line. For example:

# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen

# In this example, the calibration values are 29, 83, 13, 24,
# 2, 14, and 76. Adding these together produces 281.

# What is the sum of all of the calibration values?


NUMBERS = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}

WORDS = {
'one' : 1,
'two' : 2,
'three' : 3,
'four' : 4,
'five' : 5,
'six' : 6,
'seven' : 7,
'eight' : 8,
'nine' : 9,
'zero' : 0
}

total = 0
with open('day1.txt', 'r') as p:
    for word in p.readlines():
        leftmost = len(word)
        rightmost = 0
        left = -1
        right = -1
        for k, v in WORDS.items():
            temp_l = word.find(k)
            if temp_l == -1:
                temp_l = len(word)
            temp_r = word.rfind(k)
            if temp_l < leftmost:
                leftmost = temp_l
                left = v
            if temp_r > rightmost:
                rightmost = temp_r
                right = v
        for char in word[0:leftmost]:
            if char in NUMBERS:
                left = int(char)
                break
        for char in word[rightmost:len(word)]:
            if char in NUMBERS:
                right = int(char)
        num = left*10 + right
        total += num

print(total)
