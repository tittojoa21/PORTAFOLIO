# dado un texto cualquiera, determine cuantas veces aparece cada vocal en el texto. no distinga entre mayúsculas y minúsculas.
# recuerde que puede iterar por sobre las letras de un texto utilizando el for solamente. recuerde el metodo lower() para convertir las letras a minúsculas.
# comience con el siguiente diccionario
# vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
# opcional: comience con un diccionario vacio y cuente cualquier letra. a medida que aparezcan nuevas, agregue una entrada al diccionario. la entrada debe ser la letra, y el valor debe ser el número de veces que aparece. una vez que se cuente todas las letras, muestre el diccionario.

vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
letras = {}
frase_usuario = input("Ingrese una frase: ")

for letra in frase_usuario:
    if letra.lower() in vocales:
        vocales[letra.lower()] += 1

print(vocales)

for letra in frase_usuario:
    if letra.lower() not in letras:
        letras[letra.lower()] = 1
    else:
        letras[letra.lower()] += 1
print(letras)
