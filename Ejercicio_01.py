"""
1. Escribir un programa para el manejo de listas el cuál cumplirá los siguientes
requerimientos (4 ptos):
Reglas:
- Crear una función que le permitirá almacenar 10 número aleatorios en una
lista y finalmente los imprimirá por consola al llamar la función.
- Crear una función que le permita almacenar los números no repetidos de la
lista anterior, retornar este valor e imprimirlo por consola.
- Crear una función donde se creará una lista para ordenar de mayor a menor
la lista que se creó en el ítem anterior (número no repetidos) y otra lista
para ordenarlas de menor a mayor, retornar este valor e imprimirlos por
consola.
- Crear una función para indicar cuál es mayor número de la lista (lista del
ítem 2), retornar este valor e imprimirlo por consola.
"""

def almacenar_lista():
    lista=[[]]*10

    for i in range(len(lista)):
        elemento = int(input("Ingrese un elemento para la lista: "))
        lista[i] = elemento

    print("La lista creada es: ")
    print(lista)

    return lista

def elementos_no_repetidos(lista):

    lista_no_repetidos = []

    for elemento_1 in lista:
        if elemento_1 not in lista_no_repetidos:
            lista_no_repetidos.append(elemento_1)

    print("Lista de números no repetidos: {}".format(lista_no_repetidos))

    return lista_no_repetidos

def ordenar_lista(lista):

    lista_menor_mayor = sorted(lista)
    lista_mayor_menor = sorted(lista, reverse=True)
    print("La lista ascendente es: {}".format(lista_menor_mayor))
    print("La lista descendente es: {}".format(lista_mayor_menor))

    return lista_menor_mayor,lista_mayor_menor

def mayor_numero(lista):
    mayor = max(lista)
    print("El mayor número de la lista es: {}".format(mayor))
    return mayor

lista = almacenar_lista()
lista_no_repetidos = elementos_no_repetidos(lista)
lista_ascendente,lista_descendente = ordenar_lista(lista_no_repetidos)
mayor = mayor_numero(lista_no_repetidos)
















