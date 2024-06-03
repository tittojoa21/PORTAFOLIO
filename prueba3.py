# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

deposito = float(input("¿Cuanto ha depositado? "))
ahorros = deposito * 0.04
print("El primer ahorro es: ", round(ahorros, 2))
ahorros = ahorros + deposito
print("El segundo ahorro es: ", round(ahorros, 2))
ahorros = ahorros + deposito
print("El tercer ahorro es: ", round(ahorros, 2))

