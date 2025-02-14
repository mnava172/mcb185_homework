
num1 = 0
num2 = 1
print(num1, num2, end="")
for i in range(8):
	placeholder = num1 + num2
	num1 = num2
	num2 = placeholder
	print(" ",placeholder, end="")
print()