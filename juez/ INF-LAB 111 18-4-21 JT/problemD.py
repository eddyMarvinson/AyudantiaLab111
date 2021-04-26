import math

def procedimientoSerie(n):
	for j in range(n):
		number = math.ceil(((j + 1) / 2) - 1)
		print(str(number) + " ", end="")
	print()

t = int(input())
for i in range(t):
	n = int(input())
	procedimientoSerie(n)
	