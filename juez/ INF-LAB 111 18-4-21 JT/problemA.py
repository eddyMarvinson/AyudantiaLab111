def factorial(n):
	f = 1
	for i in range(n):
		f = f * (i + 1)
	return f

def fibonacci(n):
	a = 1
	b = 0
	c = 0
	for i in range(n):
		c = a + b
		a = b
		b = c
	return c

def serie(n):
	number = 1
	cnt = 0
	for x in range(n):
		if cnt == number:
			cnt = 0
			number = number + 1
		cnt = cnt + 1
	return number

def sumatoria(n):
	s = 0.00
	for i in range(n):
		s = s + factorial(fibonacci(i + 1)) / serie(i + 1)
	return s

n = int(input())
print("{:.2f}".format(sumatoria(n)))