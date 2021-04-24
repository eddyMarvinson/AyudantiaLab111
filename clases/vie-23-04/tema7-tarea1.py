# esta funcion nos calcula el promedio de cuatro datos
def funcion1(dato1, dato2, dato3, dato4):
    return (dato1 + dato2 + dato3 + dato4) // 4
# esta funcion califica segun promedio
def funcion2(promedio):
    #a si promedio es mayor a 20
    #b si promedio esta entre 15 y 20 inclusive
    #c si promedio esta entre 10 y 14
    #d si es menor a 10
    if promedio > 20:
        return 'a'
    if promedio >= 15 and promedio <= 20:
        return 'b'
    if promedio >= 10 and promedio <=14:
        return 'c'
    return 'd'