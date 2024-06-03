# Un vendedor de juguetes ofrece tres tipos de juguetes: 
# juguetes a baterías, juguetes a cuerda y juguetes de carga eléctrica. 
# El vendedor ofrece un descuento del 10 % en los pedidos de juguetes a base de baterías si el pedido supera los 1000 productos. 
# En pedidos de más de 100 para juguetes a cuerda, se otorga un descuento del 5 %, y se otorga un descuento del 10 % en pedidos de juguetes de carga eléctrica 
# superior a 500. Suponga que los códigos numéricos 1, 2 y 3 se usan para
# juguetes con batería, juguetes a cuerda y juguetes de carga eléctrica, respectivamente. 
# Escriba un programa que lea el código del producto y la cantidad del pedido e 
# imprima la cantidad neta por la que el cliente debe pagar después del descuento.
# Precios unitarios de los juguetes

precio_bateria = 20  # Precio de un juguete a batería
precio_cuerda = 15   # Precio de un juguete a cuerda
precio_electrico = 30  # Precio de un juguete de carga eléctrica

juguetes = input("Ingrese el tipo de juguetes: \n 1. Baterias \n 2. Cuerda \n 3. Carga Electrica \n")
total = 0
descuento_aplicado = False  # Para verificar si se aplicó algún descuento

if juguetes == "1":
    print("Al comprar más de 1000 juguetes a baterías, se aplicará un descuento del 10%.")
    cantidad_bateria = int(input("Ingrese la cantidad de juguetes a baterias: "))
    if cantidad_bateria > 1000:
        descuento_aplicado = True
        total = cantidad_bateria * precio_bateria * 0.9
        print("Descuento aplicado correctamente.")
    else:
        total = cantidad_bateria * precio_bateria
    tipo_juguete = "baterías"
elif juguetes == "2":
    print("Al comprar más de 100 juguetes a cuerda, se aplicará un descuento del 5%.")
    cantidad_cuerda = int(input("Ingrese la cantidad de juguetes a cuerda: "))
    if cantidad_cuerda > 100:
        descuento_aplicado = True
        total = cantidad_cuerda * precio_cuerda * 0.95
        print("Descuento aplicado correctamente.")
    else:
        total = cantidad_cuerda * precio_cuerda
    tipo_juguete = "cuerda"
elif juguetes == "3":
    print("Al comprar más de 500 juguetes de carga eléctrica, se aplicará un descuento del 10%.")
    cantidad_carga = int(input("Ingrese la cantidad de juguetes de carga electrica: "))
    if cantidad_carga > 500:
        descuento_aplicado = True
        total = cantidad_carga * precio_electrico * 0.9
        print("Descuento aplicado correctamente.")
    else:
        total = cantidad_carga * precio_electrico
    tipo_juguete = "carga eléctrica"
else:
    print("Tipo de juguete no válido.")

if total > 0:
    print("El total a pagar es: ${:.2f}".format(total))

