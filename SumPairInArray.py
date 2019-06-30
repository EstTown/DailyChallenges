# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

# Naive approach, O(n^2) time
def sumpair(arr, value):
	for a in arr:
		for b in arr :
			if a + b == value:
				return True
	return False

# More efficient approach (n time)
def sumpair2(arr, value):
	dict = {}
	for i in range(0, len(arr)):
		complement = value - arr[i]
		if complement in dict:
			return True
		dict[arr[i]] = i
	return False

list = [1,2,3,4,5,6]
val = 11

print(sumpair2(list, val))