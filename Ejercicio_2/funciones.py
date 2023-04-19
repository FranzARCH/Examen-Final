import random
import math

# Crear el archivo "notas.txt" si no existe
with open("notas.txt", "a+") as f:
    f.seek(0)
    if not f.read(1):
        f.write("Archivo de notas\n\n")

# Crear el archivo "funciones.py" si no existe
with open("funciones.py", "a+") as f:
    f.seek(0)
    if not f.read(1):
        f.write("# Funciones para el archivo de notas\n\n")

# Función para llenar la lista con números aleatorios
def llenar_lista():
    n = int(input("Ingrese el tamaño de la lista: "))
    lista = [random.randint(1, 100) for _ in range(n)]
    with open("notas.txt", "a") as f:
        f.write("Lista de números aleatorios:\n")
        for num in lista:
            f.write(str(num) + "\n")

# Función para calcular la raíz cuadrada de cada número en la lista
def raiz_cuadrada():
    lista = []
    with open("notas.txt", "r") as f:
        for line in f:
            try:
                lista.append(int(line))
            except ValueError:
                pass
    with open("notas.txt", "a") as f:
        f.write("\nRaíz cuadrada de los números:\n")
        for num in lista:
            f.write(str(math.sqrt(num)) + "\n")

# Agregar las funciones al archivo "funciones.py"
with open("funciones.py", "a") as f:
    f.write(llenar_lista.__name__ + "()\n")
    f.write(raiz_cuadrada.__name__ + "()\n")

# Ejecutar las funciones
llenar_lista()
raiz_cuadrada()