import sys

def funcion300(n):
	s = ''.join(sorted(n, reverse=True))
	r = int(s)
	if r % 300 == 0:
		return r
	return -1
	
for x in sys.stdin:
	y = str(x).replace('\n','')
	print(funcion300(y))
