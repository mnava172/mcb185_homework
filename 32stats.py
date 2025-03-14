import sys 
import math 

vals = []
total = 0

# Number of values
for arg in sys.argv[1:]:
	arg = int(arg)
	vals.append(arg)
	total += arg
print("sum:", total)

#Mean
mean = total/len(vals)
print("mean:", mean)

#Standard Deviation
vari = 0
for val in vals:
	vari += (mean - val)**2
vari /= (len(vals)-1)
sd = vari**0.5
print("standard deviation:", sd)

# Minimum and Maximum values 
def minmax(vals):
	mini = vals[0]
	maxi = vals[0]
	for val in vals:
		if val < mini: mini = val
		if val > maxi: maxi = val
	return mini, maxi 
lowest, highest = minmax(vals)
print("mini:",lowest)
print("maxi:", highest)

vals.sort()

# Median
if len(vals)%2 == 0 : # even
	i1 = len(vals)//2
	i2 = i1 - 1
	median = (vals[i1] + vals[i2])/2
else :
	median = vals[len(vals)//2]

print('median:', median)

#N50
vals.sort()
def N50(vals):
	length = 0
	for val in vals:
		length += val
		if length >= total/2: 
			return val
print('N50:', N50(vals))


