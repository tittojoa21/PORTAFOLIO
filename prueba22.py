# mostrar por pantalla la suma y el producto de los numeros ingresados por el usuario
def obtener_entrada(entrada):
    valido = True
    while valido:
        try:
            return float(input(entrada))
        except ValueError:
            print("Por favor ingresa un número válido.")

def realizar_operacion(operacion, num1, num2):
    if operacion == "suma":
        return num1 + num2
    elif operacion == "producto":
        return num1 * num2
    else:
        return None

num1 = None
num2 = None
suma_num = 0
producto_num = 1

bandera = True
while bandera:
    try:
        num1 = obtener_entrada("Ingresa el primer número: ")
        num2 = obtener_entrada("Ingresa el segundo número: ")

        print("Selecciona la operación a realizar:")
        print("1. Suma")
        print("2. Producto")
        print("3. Salir")
        eleccion = int(input("Ingresa la opción deseada: "))

        if eleccion == 1:
            suma_num = realizar_operacion("suma", num1, num2)
            print("La suma de los números es: ", suma_num)

        elif eleccion == 2:
            producto_num = realizar_operacion("producto", num1, num2)
            print("El producto de los números es: ", producto_num)

        elif eleccion == 3:
            print("Fin del programa")
            bandera = False

        else:
            print("Opción inválida. Por favor ingresa una opción válida.")

    except ValueError:
        print("Por favor ingresa una opción numérica válida.")
    except Exception as e:
        print(f"Algo salio mal: {e}")
        break 