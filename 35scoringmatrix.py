
import sys

alph = sys.argv[1]
mat = sys.argv[2]
mismat = sys.argv[3]

print(sys.argv)

for letters in sys.argv[1]:
	print(' ',letters, end=' ')
print()
	
for l1 in range(len(alph)):
	print(alph[l1], end=' ')
	for l2 in range(len(alph)):
		if l1 == l2: print(mat, end='  ')
		else: print(mismat, end='  ')
	print()

'''
for l in range(0, len(alph)):
	if l == l: print(alph[l], mat)
	else: print(mismat)
	

for l in sys.argv[1]:
	if l == l: print(l, mat)
	else: print(mismat)
'''