# Escribir un programa que pregunte al usuario por las ventas de un rango de años y muestre por pantalla un diagrama de líneas con la evolución de las ventas.
# Pedimos al usuario la cantidad de años
import matplotlib.pyplot as plt
años = int(input("¿Cuantos años hay de datos? "))

# Creamos una lista vacia para almacenar las ventas
ventas_anuales = []

# Pedimos al usuario las ventas de cada año
for i in range(años):
    ventas = float(input(f"¿Cuantas ventas hubo en {i+1}? "))
    ventas_anuales.append(ventas)

# Graficamos la evolución de las ventas

plt.plot(range(1, años+1), ventas_anuales)

plt.xlabel("Año")
plt.ylabel("Ventas")
plt.title("Evolución de ventas")

plt.show()

