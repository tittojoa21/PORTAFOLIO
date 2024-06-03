"""ejercicio 18  
escribir un programa equivalente al siguiente, pero sin usar continue:
suma = 0 
i = 1
while i <= 100:
    if i % 2 == 0:
        continue
    suma = suma + i
    
luego del cambio, reemplazar el bucle while por un bucle for que haga lo mismo."""

suma = 0
for i in range(1, 101):
    if i % 2 != 0:
        suma = suma + i
print(suma)