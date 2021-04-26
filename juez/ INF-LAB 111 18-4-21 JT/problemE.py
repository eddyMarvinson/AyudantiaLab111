def sum(x, k, m):
	s = ((k + k * x) // 2) * x
	return s % m

def sum2(x, k, m):
	s = 0
	for i in range(x):
		s = s + k * (i + 1)
	return s % m
	
x, k, m = map(int, input().split());
print(sum2(x, k, m))