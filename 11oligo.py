def tm(a, c, g, t):
	length = a + c + g + t
	if length <= 13:
		return(a + t) * 2 + (g + c) *4
	return 64.9 + 41 *(g + c - 16.4)/(a+t+g+c)
print('oligo1:', tm(0, 2, 3 ,4))
print('oligo2:', tm(5, 7, 3, 4))
