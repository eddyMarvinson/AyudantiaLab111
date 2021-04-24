# funcion solucion que utiliza:
# solo operaciones matematicas
# para calcular el enesimo elemento de la sumatoria
# s_n = ((t0 + tn) / 2) * n
def sumatoria1(x, k, m):
	s = ((k + k * x) // 2) * x
	return s % m
# funcion solucion que utiliza estructura repetitiva (for)
def sumatoria2(x, k, m):
	s = 0
	for i in range(x):
		s = s + k * (i + 1)
	return s % m

x, k, m = map(int, input().split());
print(sumatoria2(x, k, m))
#print(sumatoria1(x, k, m))