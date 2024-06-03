# dada una lista de numeros al azar, encuentre la primer aparicion del numero 0
# imprimir su posicion en la lista
# asegurese de detener el ciclo una vez que se encuentra el numero.
# oues no hacerlo hara que el programa tarde mucho en ejecutarse
import random

# Crear una lista de números al azar
numeros = [random.randint(0, 1000) for _ in range(100)]

# Imprimir la lista generada
print("Lista de números generada al azar:")
print(numeros)

# Inicializar la variable 'posicion' para rastrear la posición de 0
posicion = None

# Bucle para encontrar la primera aparición de 0
for i, numero in enumerate(numeros):
    if numero == 0:
        posicion = i
        break  # Detener el ciclo una vez que se encuentra 0

# Verificar si se encontró el número 0 y mostrar su posición
if posicion is not None:
    print(f"La primera aparición del número 0 está en la posición: {posicion}")
else:
    print("No hay un 0 en la lista.")