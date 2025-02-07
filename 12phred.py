"""
import math 

def symbol_to_prob(c):	
	return 0.001
	

print(symbol_to_prob('9'))
print(prob_to_symbol(0.003))

def prob_to_symbol(p):
	pqv = -int(math.log10(p)*10)
	symbol = chr(pqv+33)
	print(symbol)
	p= 0.0005
	print(p)

import math 
print(ord('A'))
print(chr(65))
"""
import math
def char_to_prob(x):
	phred = ord(x) - 33
	p = 10**(-phred/10)
	return p

print(char_to_prob('A'))

def prob_to_char(y):
	q = -10 *math.log10(y)
	return chr(int(q+33))
	
print(prob_to_char(0.001))	

	
	
	
	
	
	
	
	
	
	