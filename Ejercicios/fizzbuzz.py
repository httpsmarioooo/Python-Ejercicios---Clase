

# Números esperados (múltiplos de 3 o 5)

while True:
    print("Introduce un número para comprobar si es múltiplo de 3 o 5: ")
    try:
        numero = int(input())
        if numero % 3 == 0 or numero % 5 == 0:
            # Si es múltiplo de 3 o 5, mostrar el resultado
            if numero % 3 == 0 and numero % 5 == 0:
                print("FizzBuzz")
            elif numero % 3 == 0:
                print("Fizz")
            elif numero % 5 == 0:
                print("Buzz")
            break
        else:
            print("Número incorrecto. Por favor, ingresa un múltiplo de 3 o 5.")
    except ValueError:
        print("No has ingresado un número. Por favor, inténtalo de nuevo.")


# Generar una secuencia de números del 1 al 100
# for numero in range(1, 21):
#     if numero % 3 == 0 and numero % 5 == 0:
#         print("FizzBuzz")
#     elif numero % 3 == 0:
#         print("Fizz")
#     elif numero % 5 == 0:
#         print("Buzz")
#     else:
#         print(numero)



