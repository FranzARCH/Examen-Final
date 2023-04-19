import time

def tiempo_ejecucion(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        tiempo_total = fin - inicio
        print("La función {} tardó {} segundos en ejecutarse.".format(func.__name__, tiempo_total))
        return resultado
    return wrapper

@tiempo_ejecucion
def multiplicacion(a, b, c, d):
    resultado = a * b * c * d
    return resultado

# Ejemplos de uso
multiplicacion(2, 3, 4, 5)
multiplicacion(10, 20, 30, 40)
multiplicacion(1, 2, 3, 4)
