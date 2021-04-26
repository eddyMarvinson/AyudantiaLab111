import sys

def fibonacci(n):
	a = 1
	b = 0
	c = 0
	for i in range(n):
		c = a + b
		a = b
		b = c
	return c

def prime(n):
	i = 0
	p = 2
	number = 2
	while i < n:
		cnt = 0
		div = number - 1
		while div > 1:
			if number % div == 0:
				cnt = cnt + 1
			div = div - 1
		if cnt == 0:
			p = number
			i = i + 1
		number = number + 1
	return p

def sum(n, x):
	s = 0.00
	for i in range(n):
		s = s + (fibonacci(i + 1) / (prime(i + 1) * x))
	return s

for x in sys.stdin:
	n, x = map(int, x.split())
	print("{:.2f}".format(sum(n,x)))