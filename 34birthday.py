import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

day = 0
shared = 0
for i in range(trials):
	calendar=[]
	for day in range(days):
		calendar.append(0)
	for pep in range(people):
		birthday = random.randint(0,days-1)
		calendar[birthday] += 1
		if calendar[birthday] == 2: 
			shared += 1
			break
			calendar.append(birthday)
print(shared/trials, 'shared/trials')
	
	