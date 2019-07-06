# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
# Given the root to a binary tree, count the number of unival subtrees.
# For example, the following tree has 5 unival subtrees:
'''
   0
  / \
 1   0
	/ \
   1   0
  / \
 1   1
 '''

class Node():
	def __init__(self, val, left=None, right=None):
		self.value = val
		self.left = left
		self.right = right

# Checker
def isUnival(node):
	return helperFunc(node, node.value)

# Recursive helper function, for checker
def helperFunc(node, value):
	if node is None: return True
	if node.value == value:
		return helperFunc(node.left, value) and helperFunc(node.right, value)
	else: return False

# Main function, to be called
# Recursively applies itself to subtrees, and counts up
def countSubTrees(node):
	if node is None: return 0
	L = countSubTrees(node.left)
	R = countSubTrees(node.right)
	if isUnival(node): return L + R + 1 
	else: return L + R

# Tree from example above
tree = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))

print(countSubTrees(tree))