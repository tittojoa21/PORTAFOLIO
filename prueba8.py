# calcule el promedio de las calificaciones de los estudiantes
# los estudiantes seran cargados por el usuario en un diccionario
# nombre: calificacion
# para ello pidale que primero ingrese la cantidad de estudiantes que se ingresan
# luego ingrese el nombre y la calificacion correspondiente
# una vez terminado este proceso, que se calcule el promedio y lo muestre por pantalla

students = {}

numero_estudiantes = int(input("¿Cuantos estudiantes va a registrar? "))

for i in range(numero_estudiantes):
    nombre = input("¿Cual es el nombre del estudiante? ")
    calificacion = float(input("¿Cual es la calificación? "))
    students[nombre] = calificacion

suma_calificaciones = sum(students.values())
promedio = suma_calificaciones / numero_estudiantes

print(f"El promedio es: {promedio:.2f}")