# escribir un programa que permita a un usuario almacenar
# nombres de frutas y su respectiva cantidad en kilogramos.
# el programa debe permitir al usuario ver la lista completa de frutas y su cantidads, o ver una lista de las frutas cuya cantidad sea menor a 10kg.
# usando funciones para cada tarea 
# ejemplo diccionario = {'manzana': 3, 'pera': 5, 'naranja': 7}

frutas= {}

def agregar_fruta(nombre, cantidad):
    frutas[nombre] = cantidad

def mostrar_todas_las_frutas():
    for nombre, cantidad in frutas.items():
        print(f"{nombre}: {cantidad} kg")

def mostrar_frutas_poca_cantidad():
    for nombre, cantidad in frutas.items():
        if cantidad < 10:
            print(f"{nombre}: {cantidad} kg")

while True:
    print("Menu:")
    print("1. Agregar fruta")
    print("2. Mostrar todas las frutas")
    print("3. Mostrar frutas con cantidad menor a 10 kg")
    print("4. Salir")
    opcion = input("Ingrese una opción (1-4): ")

    if opcion == "1":
        nombre = input("Ingrese el nombre de la fruta: ")
        cantidad = float(input("Ingrese la cantidad de kilogramos: "))
        agregar_fruta(nombre, cantidad)
    elif opcion == "2":
        mostrar_todas_las_frutas()
    elif opcion == "3":
        mostrar_frutas_poca_cantidad()
    elif opcion == "4":
        print("fin del programa")
        break
    else:
        print("Opciòn inválida. Intente nuevamente.")

