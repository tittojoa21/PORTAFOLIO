# escriba un programa que solicite un numero entero positivo al usuario y compute la suma de todos los numeros naturales menores a el.
#  este programa debe ser interactivo . es decir, el programa solicita un numero al usuario, devuelve la suma, y solicita un nuevo numero.
# este continua asi hasta que el usuario ingrasa "exit", determinando que el programa debe terminar.
# ejemplos: ingrese un numero o salir para terminar el programa : 10 la suma es 45
while True:
    numero = input("Ingrese un número o 'salir' para terminar el programa: ")

    if numero.lower() == "salir":
        print("Programa terminado.")
        break

    if numero.isdigit():
        numero = int(numero)
        if numero > 0:
            suma = sum(range(numero))
            print(f"La suma es {suma}")
        else:
            print("Por favor, ingrese un número entero positivo.")
    else:
        print("Entrada inválida. Asegúrese de ingresar un número entero positivo o 'salir'.")