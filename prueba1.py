# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
horas = float(input("¿Cuántas horas ha trabajado? "))
coste = float(input("¿Cuanto es el coste por hora? "))
paga = horas * coste
print("Tu paga es: ", paga)