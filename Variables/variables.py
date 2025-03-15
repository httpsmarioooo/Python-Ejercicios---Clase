#& VARIABLES:
#& El valor puede cambiar durante la ejecución 

nombre = "Ana"
edad = 50 
es_estudiante = True
print(nombre, edad, es_estudiante)

edad = 50
print(edad)
edad = 30
print(edad)

#* Tipos de datos 

#! Entero 
numero_entero = -10 
numero_entero2 = 10
print("Entero: " , numero_entero)
print("Entero: " , numero_entero2)

#! Flotante 
numero_flotante = 10.2
numero_flotante2 = 0.2
print("Flotante: ", numero_flotante)

#! Cadena 
cadena = "Hola a todxs"
cadena2 = "¿Cómo están?"
print("Cadena: ", cadena)

#! Booleano
num_booleano = True
print("Booleano: ", num_booleano)


#& OPERACIONEES CON ENTEROS Y FLOTANTES 

#? Suma de enteros 
print("Suma de enteros: ", numero_entero + numero_entero2)

#? Suma de flotantes 
print("Suma de flotantes: ", numero_flotante + numero_flotante2)

#? Suma Booleanos 
booleano1 = False 
booleano2 = False
print(booleano1 + booleano2)

#? Operaciones entre cadenas
resultado =  cadena + " " + cadena2
print("Concatenación: ", resultado )


#& Determinar el tipo de dato 

print("Tipo de dato de 10: ", type(10))
print("Tipo de dato de 10.5: ", type(10.4))
print("Tipo de dato de Hola: ", type("Hola"))
print("Tipo de dato de True: ", type(True))


