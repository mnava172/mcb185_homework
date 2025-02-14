import random
trial = 5
die = 0
stable = 0

for i in range(trial):
	print('trial', i)
	faliure = 0
	success = 0
	for i in range (5):
		r = random.randint(1,20)
		if r == 1: faliure += 2
		elif r <= 9: faliure += 1
		elif r <=19: success += 1
		else: 
			revive += 1
			break 
		if success == 3:
			stable += 1
			break
		if faliure == 3:
			die += 1
			break