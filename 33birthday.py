import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

shared = 0
for i in range(trials):
	list_23_birthday = []
	
	for pep in range(people):
		bday = random.randint(0,days)
		if bday in list_23_birthday:
			shared += 1
			break
		list_23_birthday.append(bday)
	
print(shared/trials, 'for shared/trials')