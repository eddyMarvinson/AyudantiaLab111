def procedimientoSerie(n, k):
	c = 0
	number = 1 
	for j in range(n):
		if c == k:
			c = 0
			number = number + 2
		print(str(number) + " ", end="")
		c = c + 1
	print()

t = int(input())
for i in range(t):
	n, k = map(int, input().split())
	procedimientoSerie(n, k)