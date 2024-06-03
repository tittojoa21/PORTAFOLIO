# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

barras = float(input("¿Cuantas barras de pan no son del dia? "))
descuento = barras * 0.60
print("El descuento es: ", descuento)
barra_dia = 3.49
coste = barras * barra_dia
print("El coste total es: ", coste)