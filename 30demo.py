import math
# STRINGS
s = 'hello world'			#string is synonymous with text
print(s)

s1 = 'hey "dude"'
s2 = "don't tell me what to do"
print(s1, s2)					

		# backslashes are used to signify special characters
print('hey "dude" don\'t tell me what to do')

## string methods
print(s.upper())
print(s)

print(s.replace('o', ''))
print(s.replace('o', '').replace('r', 'i'))

## string formatting

### f-string --> should use, for completeness use other form
print(f'{math.pi}')				# does nothing special
print(f'{math.pi:.3f}')			# 3 fixed digits after decimal
print(f'{1e6 * math.pi:e}')		# exponent notation
print(f'{"hello world":>20}')	# right justify with space filler
print(f'{"hello world":.>20}')	# right justify with dot filler
print(f'{20:<10} {10}')			# left justify

### str.format()
print('{} {:.3f}'.format('str.format', math.pi))

print('%s %.3f' % ('printf', math.pi))

#INDEXES
seq = 'GAATTC'		# computer languages start counting at 0 not 1
print(seq[0], seq[1])

print(seq[-1])			# treats last as the first

for nt in seq:
	print(nt, end='')
print()

for i in range(len(seq)):	# letters by indices
	print(i, seq[i])

#SLICES
s = 'ABCDEFGHIJ'		# slice subset of container
print(s[0:5])			# show positions 0-5
print(s[0:8:2])			# show positions 0-8, every 2 positions
print(s[0:5], s[:5])	# both ABCDE
print(s[5:len(s)], s[5:])	# both FGHIJ
print(s, s[::], s[::1], s[::-1]) # 1st 3 do the same 4th in reverse

##example of use of slicing practically
dna = 'ATGCTGTAA'
for i in range(0, len(dna), 3):
	codon = dna[i:i+3]
	print(i, codon)		# gives 3 positions per line, labels number

#TUPLES
tax = ('Homo', 'sapiens', 9606)	# construct tuple
print(tax)						# note the parenthesis in the output

# tuples and strings are immutable 

print(tax[0])		# index
print(tax[::-1])	# slice

# ENUMERATE() and ZIP()

## enumerate()
nts = 'ACGT'
for i in range(len(nts)):
	print(i, nts[i])

for i, nt in enumerate(nts):
	print(i, nt)

## zip()
### index sep. containers
names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):		
	print(nts[i], names[i])
### tidier solutions
for nt, name in zip(nts, names):
	print(nt, name)
### enumerate zip
for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)
	
#LISTS
nts = ['A', 'T', 'C']
print(nts)

nts[2] = 'G'
print(nts)

nts.append('C')
print(nts)

last = nts.pop()
print(last)

nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)

nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

# list.copy()		# to make a copy

alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(alph)
aas = list(alph)
print(aas)

# split() and join()
text = 'good day       to you ' #number spaces didnt matter
words = text.split()
print(words)

line = '1.41,2.72,3.14'
print(line.split(','))

# lists turned into strings
s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)

# SEARCHING
if 'A' in alph: print('yay')
if 'a' in alph: print('no')

print('index G?', alph.index('G'))
print('index Z?', alph.index('Z'))
print('index A?', alph.index('A'))

print('find G?', alph.find('G'))
print('find Z?', alph.find('Z'))

# PRACTICE PROBLEMS
s = 16, 6, 9, 10, 1
def minimum(vals):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
	return mini
	
print(minimum(s))

def minmax(vals):
	mini = vals[0]
	maxi = vals[0]
	for val in vals:
		if val < mini: mini = val
		if val > maxi: maxi = val
	return mini, maxi

print(minmax(s))

def mean(vals):
	total = 0
	for val in vals: total += val
	return total / len(vals)
	
print(mean(s))

def entropy(probs):
	h=0
	for p in probs:
		h -= p * math.log2(p)
	return h
print(entropy([0.2, 0.3, 0.5]))

def dkl(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += p * math.log2(p/q)
	return d
p1 = [0.4, 0.3, 0.2, 0.1]
p2 = (0.1, 0.3, 0.4, 0.2)
print(dkl(p1, p2))

#COMMAND LINE DATA
import sys 
print(sys.argv)

i = int('42')
x = float('hello')
print(i * x)	

	