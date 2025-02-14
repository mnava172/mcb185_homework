import random	
t = 1, 2	#this is a tuple
print(t)
print(type(t))

person = 'Steve', 21, 57891.50	#name, age, yearly income 
print(person)

#TUPLES#
def midpoint(x1, y1, x2, y2):
	x = (x1 + x2) / 2
	y = (y1 + y2) / 2
	return x, y
print(midpoint(1, 2, 3, 4))	#output includes parenthesis and comma
m = midpoint(1, 2, 3, 4)	#assigns m to midpoint, contains 2 values
mx, my = midpoint (1, 2, 3, 4)	#unpacks the tuple 
print(mx, my)
print(m[0], m[1]) #numeric index to unpack a tuple into named variables

#ITERATION#
"""
while loop
	while <boolean expression is True>
		do_something
causes an endless loop, DON'T DO IT
"""
i = 0					#create i, each time it goes through the
while True:				#loop i value increases by 1 once i reaches
	i = i + 1			#3, the loop breaks
	print('hey', i)
	if i == 3: break

#better way to brak while loop is some kind of condition
i = 0
while i < 3:
	i = i + 1
	print('hey', i)
	
#loop can start at any number, increase by any increment, and end 
i = 1
while i < 10:
	print(i)
	i = i + 3
print('final value for i is', i)

"""
for i in range
"""
for i in range(1, 10, 3):	# does the same as wile function above
	print(i)

# all 3 do the same thing
for i in range(0, 5, 1): 	print(i)
for i in range(0,5):		print(i)
for i in range(5):			print(i)

"""
for item in container
"""
basket = 'milk', 'eggs', 'bread'
for thing in basket:
	print(thing)
	
for i in range(len(basket)):
	print(basket[i])

# NESTING
for i in range(7):
	if i % 2 == 0:	print(i, 'is even')
	else:			print(i, 'is odd')
	
# PRACTICE
## Triangular number
def triangular(n):
	tri = 0					#in order to sum, must have variable to hold sum
	for i in range(n+1):		
		tri = tri + i		#initialized at 0, each iteration add current value of loop variable
	return tri				#returning value of sum
print(triangular(5))

## Factorial
def factorial(n):
	if n == 0: return 1
	fac = 1
	for i in range(1, n + 1 ):
		fac = fac * i
	return fac
print(factorial(5))

##Poisson Probability 
import math
def Poisson(n,k):
	return (n**k * math.e**-n)/math.factorial(k)
print(Poisson(4,3))

##N Choose K
import math 
def nchoosek(n,k):
	return math.factorial(n) / math.factorial(k) * math.factorial(n-k)
print(nchoosek(6,2))

##Eulers numer
import math
def euler(limit):
	e = 0
	for n in range(limit):
		e = e + 1/ math.factorial(n)
	return e
print(euler(1000))

##Prime number
def is_prime(n):
	for den in range(2, n//2 +1):
		if n % den == 0: return False 
	return True
print(is_prime(31))

## Pi
import math
def nilakantha(limit):
	pi = 3
	for i in range(1, limit + 1):
		n = 2 * i
		d = n * (n+1) * (n*2)
		if i % 2 == 0: 	pi = pi - 4 / d
		else:			pi = pi + 4 / d
	return pi
print(nilakantha(1000))

#RANDOM 
import random 				#will print 5 random numbers 0=<x<1
for i in range(5):
	print(random.random())

for i in range(3):			#will print 3 random number 1-6
	print(random.randint(1,6))
	
## Compound Assignment
"""
x = x + 1
is the same as 
x += 1
"""

#More Practice				
#Monty Pi-thon
import random
import math
total = 0
incount = 0
while True:
	x = random.random()
	y = random.random()
	distance = math.sqrt(x**2 + y**2)
	if distance <= 1 : 
		incount += 1
	total += 1 
	pi = (incount/total)*4
	print(pi)

#D&D Status
#3d6
total = 0
for i in range(3):
	result = random.randint(1,6)
	total += result
print('3D6', total)

#3D6r1
total = 0
for i in range(3):
	result = random.randint(1,6)					
	if result == 1: result = random.randint(1,6)	
	total += result
print('3D6r1', total)
		
#3D6x2
total = 0
for i in range(3):
	result1 = random.randint(1,6)	
	result2 = random.randint(1,6)					
	if result1 > result2: 
		total += result1
	else:
		total += result2
print('3D6x2', total)

#4D6d1
total = 0
lowest = 6
for i in range (4):
	result = random.randint(1,6)
	total += result
	if result < lowest:
		lowest = result
total -= lowest
print('4D6d1', total)
