#  escriba un script en python que pida al ussuario que pida al usuario que igrese una palabra, y luego otra, y otra, y otra...
# hasta que el usuario ingrese la palabra 'exit'.
# muestre todas las palabras ingresadas como si fueran un parrafo, ademas muestre el total ingresadas 

palabras = []

while True:
    palabra = input("Ingresa una palabra: ")
    if palabra.lower() == "exit":
        break   
    palabras.append(palabra)
    
parrafo = " ".join(palabras)
print("\nParrafo:\n", parrafo)

print("\nTotal de palabras:", len(palabras))        