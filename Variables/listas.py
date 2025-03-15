#& Estructuras de datos: Listas 

#* Lista: 
lista_1 = ["manzana", "bananos", "sandia"]
print("Lista inicial", lista_1)

#? Acceder a la información:
print("Primer elemnto de lista: ", lista_1[0])
print("Primer elemnto de lista: ", lista_1[1])

#? Añadir elementos 
lista_1.append("naranja")
print("Lista modificada", lista_1)

#? Eliminar elementos
lista_1.pop(2)
print("Lista modificada2", lista_1)


#& Diccionarios:
dic_1 = {"nombre": "Juan", "edad": 60, "ciudad": "Bogotá"}
print("Diccionario1: ", dic_1)

#? Acceder a un valor 
print("Ciudad: ", dic_1["ciudad"])

#? Añadimos otra clave-valor 
dic_1["profesión"] = "Desarollador"
print("Dic actual:", dic_1)


#& Operaciones con estrructuras de datos:
#!Suma de listas

list1 = ["pera", "sandia"]
list2 = ["mandarina"]
list3 = list1 + list2
print(list3)

#!Modificar el dic 
dic2 = {"piloto": "Carlos", "pasajeros": 4}
print(dic2)

dic2["pasajeros"] = 20
print(dic2)



#!Suma de lista de elementos
list1 = ["perro", "gato", "pato"]
list2 = [1, 2, 3, 4, 5]
list3 = [True, False, True, True]
list4 = ["perro", 1, True]
sumaList = list1 + list2 + list3 + list4
print(sumaList)

#!Modificar el diccionario
dic2 = {"nombre": "Ana", "edad": 50, "es_estudiante": True}
print(dic2)
