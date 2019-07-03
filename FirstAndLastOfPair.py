# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. 
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
# Given this implementation of cons:
'''
def cons(a, b):
	def pair(f):
		return f(a, b)
	return pair
'''
# Implement car and cdr.

def cons(a, b):
	def pair(f):
		return f(a, b)
	return pair

def car(pair):
	def first(a, b):
		return a
	return pair(first)

def cdr(pair):
	def last(a, b):
		return b
	return pair(last)

assert(car(cons(3, 4)) == 3)
assert(cdr(cons(3, 4)) == 4)

print(car(cons(3, 4)))
print(cdr(cons(3, 4)))

# Note: I assume the car/cdr/cons is inspired by Lisp/Scheme,
# however, these languages use these on lists and not just pairs.
# Thus, if going for a Scheme-style implementation, 
# car should return the head of a list, and cdr the tail.
# And obviously, a list can be built by nesting cons's.