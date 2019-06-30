# Given an array of integers, return a new array such that each element at index i of the new array 
# is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?

from functools import reduce

def func(array):
	# Empty result list, with same length as input
	res = [None] * len(array)
	for i in range(len(array)):
		# Slice left and right of pivot, not including pivot in either
		left = array[:i]
		right = array[i+1:]
		# Multiply all elements in the combined list
		tmp = reduce((lambda x, y : x * y), left+right)
		# Enter the result into the result list, at the correct index
		res[i] = tmp
	return res

array1 = [1,2,3,4,5]
array2 = [3,2,1]
print(func(array1))
print(func(array2))