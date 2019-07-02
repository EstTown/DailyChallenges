# Given an array of integers, find the first missing positive integer in linear time and constant space. 
# In other words, find the lowest positive integer that does not exist in the array. 
# The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.

def findMissing(array):
    lowest = 1
    for x in array:
        if x >= 0 and x == lowest: 
            lowest += 1
    return lowest

lst1 = [3, 4, -1, 1]
lst2 = [1, 2, 0]
lst3 = [1, 2, 3, 4, 6, 7]

print(findMissing(lst1))

assert(findMissing(lst1) == 2)
assert(findMissing(lst2) == 3)
assert(findMissing(lst3) == 5)