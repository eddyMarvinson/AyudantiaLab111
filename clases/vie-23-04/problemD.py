# un procedimiento que nos muestra la serie hasta n
def procedimiento(n):
	# x es el enesimo numero de la seria, x se imprimira
	x = 0
	# cnt es el contador de las veces que se imprimio x
	cnt = 0
	for j in range(n):
		# cuando x se haya imprimido 2
		if cnt == 2:
			# reiniciamos cnt
			cnt = 0
			# incrementamos x
			x = x + 1	
		# se imprime x e incrementamos las veces que se imprimio
		cnt = cnt + 1
		# esta instruccion convertimos x en cadena y evitamos le salto de linea
		print(str(x) + " ", end="")
	# salto de linea
	print()
# leemos los t casos de entrada
t = int(input())
for i in range(t):
	# para cada entrada leemos n
	n = int(input())
	# llamamos al procedimiento que muestra la serie
	procedimiento(n)