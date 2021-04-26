import math

def serie1(n):
	return math.ceil(n / 2)

def serie2(n):
	m = (n // 2) + 1
	if n % 2 == 0:
		return (m - 1) * (m - 1) + 1
	return m * m

def serie3(n):
	m = (n // 2) + 1
	if n % 2 == 0:
		return (m - 1) * (m - 1) * (m - 1) + 1
	return m * m * m

n = int(input())
for i in range(2 * n):
	print(serie1(i + 1), serie2(i + 1), serie3(i + 1))