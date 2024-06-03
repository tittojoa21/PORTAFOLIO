# procede una lista de tuplas (actividad, edad), donde se pide se muestren los siguientes mensajes debido a las siguientes condiciones:
# si la edad es 65 o más y la actividad es "trabajar", mostrar "jubilado que trabaja"
# si la edad es 65 o mas y la actividad es "descansar", mostrar "jubilado retirado"
# si la edad es 18 o mas mostrar "mayor de edad"
# si la actividad no es ninguna de las mencionadas detenga el programa mostrando un mensaje de error
# si la edad es menor que 5, no muestres nada 
# en cualquier otro caso, muestre "nada interesante"
# utilice continue para evitar anidar condicionales, asegurece de ordenar las condiciones de manera conveniente

persons = [
    ("trabajar", 70),
    ("descansar", 70),
    ("estudiar", 20),
    ("trabajar", 20),
    ("cocinar", 20),
    ("jugar", 3),
]

for actividad, edad in persons:
    if actividad not in ["trabajar", "descansar", "estudiar", "cocinar", "jugar"]:
        print("error, actividad desconocida")
        break
    if edad < 5:
        continue
    
    if edad >= 65 and actividad == "trabajar":
        print("jubilado que trabaja")
        continue
    if edad >= 65 and actividad == "descansar":
        print("jubilado retirado")
        continue
    if edad >= 18:
        print("mayor de edad")
        continue
    else :
        print("nada interesante")