# dada una lista de numeros y ubn numero, determine en que posicion se encuentra el numero en la lista
# si no se encuentra, mostrar un -1
# utilice break para encontrar el numero
numbers = [11, 25, -4, 95]
n = 3

# Inicializar la variable 'posicion'
posicion = -1

# Inicializar el índice
index = 0

# Usar un bucle while para buscar el número en la lista
while index < len(numbers):
    if numbers[index] == n:
        posicion = index
        break  # Detener el bucle una vez que se encuentra el número
    index += 1  # Incrementar el índice

print(posicion)