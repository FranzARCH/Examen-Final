"""
3. (3 ptos) Crear un programa usando decoradores para medir el tiempo de
ejecución.
Reglas:
- Crear la función decorador adecuadamente que sumará los elementos de la
función que pasará como parámetro de la función decoradora
- Crear una función, por ejemplo, multiplicación de 4 números para decorarla
con la función anterior.
- Usar la propiedad de N parámetros para la función a decorar (*, **) y
visualizar los resultados con un mínimo tres ejemplos.
"""

import time

def tiempo_ejecucion(funcion):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        tiempo_total = fin - inicio
        print("La función {} tardó {} segundos en ejecutarse".format(funcion.__name__, tiempo_total))
        return resultado
    return wrapper

@tiempo_ejecucion
def multiplicacion(a, b, c, d):
    resultado = a * b * c * d
    return resultado

multiplicacion(5, 20, 2, 5)

