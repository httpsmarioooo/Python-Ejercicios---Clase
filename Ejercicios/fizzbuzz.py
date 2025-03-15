# print ("Introduce un número para comprobar si es multiplo de 3 de 5 o de ambos: ")
# numero = int(input())

# if numero % 3 == 0 and numero % 5 == 0:
#     print("FizzBuzz")
# elif numero % 3 == 0:
#     print("Fizz")
# elif numero % 5 == 0:
#     print("Buzz")
# else:
#     print(numero)


# Generar una secuencia de números del 1 al 100
for numero in range(1, 21):
    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print(numero)



