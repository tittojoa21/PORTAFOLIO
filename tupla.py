# Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.

def decimal_binario(num_decimal):
    return bin(num_decimal)[2:]

def binario_decimal(num_binario):
    return int(num_binario, 2)

numero_decimal = int(input("Ingresa un número decimal: "))
binario = decimal_binario(numero_decimal)
print("El número binario es:", binario)

numero_binario = input("Ingresa un número binario: ")
decimal = binario_decimal(numero_binario)

print("El número decimal es:", decimal)



