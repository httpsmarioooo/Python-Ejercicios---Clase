# Exactamente. Cuando usas _ en un bucle for, no tienes acceso al valor de la iteración (como 0, 1 o 2),
# porque _ es una forma de decirle a Python que no vas a usar ese valor.

# Por otro lado, cuando usas un nombre de variable como indice, puedes acceder al valor
# de la iteración y saber exactamente a qué iteración pertenece cada dato.

#! Diccionario vacio
personas = {}

#! Utilizando _ 
for _ in range(3):
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    personas[nombre] = edad

# print(personas)

#! Usando un nombre de variable
for indice in range(3):
    nombre = input(f"Ingrese el nombre para la iteración {indice}: ")
    edad = int(input(f"Ingrese la edad para la iteración {indice}: "))
    print(f"Iteración {indice}: Nombre: {nombre}, Edad: {edad}")