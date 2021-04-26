import math

def den(m, n):
	if(m % n == 0):
		return n
	return (m % n)

def num(m, n):
	return math.ceil(m / n)

def procedimientoSerie(n):
	for i in range(n*n):
		print(str(num(i + 1, n))+"/"+str(den(i + 1, n)))

n = int(input())
show(n)
