# 10demo.py by Mikaela
"""
#MATH
import math 
print('hello, again') # greeting
print(1.5e-2)
print(1+1)
print(1-1)
print(2*2)
print(1/2)
print (2**3)
print (5 // 2)
print (5 % 2)
print (5 * (2+1))

print(math.log2(10))
print(math.pow(2,3))
print(2**3)

print(0.1 * 1)
print(0.1 * 3)

#VARIABLES
a = 3						#side of triangle
b = 4						#side of triangle
c = math.sqrt(a**2 + b**2)	#hypotenuse
print(c)

print(type(a), type(b), type(c))
print(type(a), type(b), type(c), sep=',', end='!\n')

#FUNCTIONS
def pythagoras(a, b):
	c = math.sqrt(a**2 + b**2)
	return c
hyp = pythagoras(3, 4)
print(hyp)

def pythagoras(a, b):
	return math.sqrt(a**2 + b**2)
print(pythagoras(3, 4))

def pythagoras(a, b): return math.sqrt(a**2 + b**2)
print(pythagoras(3,4))


#PRACTICE
def circle_area(r):return math.pi * r**2
def rectangle_area(w, h): return w * h
def triangle_area(w, h):return rectangle_area(w, h) / 2

#CONDITIONALS
a = 2
b = 2
if a == b:
	print('a equals b')
print(a, b)

#practice
def is_even(x):
	if x % 2 == 0: return True
	return False 
	
print(is_even(2))
print(is_even(3))

#boolean
c = a == b
print(c)
print(type(c))

#if-elif-else
if a < b:	print('a < b')
elif a > b:	print('a > b')
else: 		print('a == b')	

if		a < b: 	print('a < b')
elif	a <= b: print('a <= b')
elif 	a == b:	print('this wil never print')

#chaining
if a < b or a > b:	print('all things being equal, a and b are not')
if a < b and a > b:	print('you are living in a strange world')
if not False: print(True)

#floating point warning
a = 0.3							# a = 0.3
b = 0.1 * 3						# b = 0.3000..04
if 		a < b:	print('a < b')
elif 	a > b: 	print('a > b')
else:			print('a == b')
	# Never test for equality using floating point numbers
import math
print(abs(a - b)) #5.551115123125783e-17
	#if abs(a - b) < 1e-9: print('close enough')
if math.isclose(a, b): print('close enough')

#string comparison (using ASCII)
s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('B < a')

#mismatched type error

a = 1
s = 'G'
if a < s: print('a < s')

#NONE TYPE
def silly(m, x, b):
	y = m * x + b
print(silly(2, 3, 4))
"""
# Practice
"""
Write a function that determines if a number is an integer. 
A good name for such a function would be is_integer() or 
isinteger(). Functions with Boolean return values often 
have is in their prefix. To solve this problem, 
try using // or %.
"""
import math
def is_integer(x):
	if x % 1 == 0: return True
	return False 

print(is_integer(3.2))
print(is_integer(4))

"""
write a function that determines if a number is a valid
probability.
"""
import math 
def is_valid_probability(x):
	if x >= 0 and x <= 1: 		return('True probability')
	return('False probability')
print(is_valid_probability(50))
print(is_valid_probability(0.5))\

"""
Write a function that return the molecular weight of
a DNA letter . If the letter doesn't match any nucleotide,
return none
"""
def letter_to_mw(x):
	if x == 'A': 		return('491.2')
	elif x == 'C': 	return('467.2')
	elif x == 'G':	return('507.2')
	elif x == 'T': 	return('482.2')
	else: 				return(None)
print(letter_to_mw('A'))
print(letter_to_mw('C'))
print(letter_to_mw('G'))
print(letter_to_mw('T'))
print(letter_to_mw('Z'))
"""
write a function that returns the complement of a DNA 
letter returning none if the letter isnt DNA
"""
def complementary_DNA(x):
	if x == 'A':	return('T')
	elif x == 'T':	return('A')
	elif x == 'G':	return('C')
	elif x == 'C':	return('G')
	else:			return(None)
print(complementary_DNA('A'))
print(complementary_DNA('C'))
print(complementary_DNA('Z'))
	
"""
Write a function that returns the maximum of 3 numbers. 
To be clear, the function takes 3 input parameters and 
returns the single largest one.
"""
	
"""
Given values for true positives, false positives, 
true negatives, and false negatives, write functions that 
return sensitivity, specificity, and F1 score.
"""
def sensitivity(tp,fn):
	return ( tp/(tp + fn))
def specificity(tn,fp):
	return( tn /(tn + fp))
def f1(tp,fp,fn):
	return( 2 / ((tp / (tp + fp)) + (tp / (tp+fn))))

print(sensitivity(2,3))
print(specificity(3,2))
print(f1(2,2,1))

"""
Write a function that returns the Shannon entropy for 
nucleotide counts A, C, G, T. It should work even in the 
case where there are zero counts for one or more letters.

import math
def shannongene(a, t, g, c): return -sum((x/4)(math.log2(x/4))
print(shannongene(3, 5, 6, 2))

"""

