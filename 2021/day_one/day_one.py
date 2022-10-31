# Read the txt file with the puzzle input for Advent 2021 day 1
# https://adventofcode.com/2021/day/1
my_sub = open("one.txt", "r")
#print(my_sub.read())
k = 122
increase = 0
# Loop through the list. Assign the txt file to X
for x in my_sub:
    # is x greater than k
    if int(x) == k:
        # assign old x value to k
        k = int(x)
        print("no change")
    elif int(x) > k:
        # assign old x value to k
        k = int(x)
        print("increase")
        increase += 1
    else:
        # assign old x value to k
        k = int(x)
        print("decrease")

print("increase", increase)
