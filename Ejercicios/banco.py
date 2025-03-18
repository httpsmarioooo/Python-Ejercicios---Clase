# print("----Bienvenido al Banco del pueblo----")
# saldo = 0

# while True:
#     print("1. Depositar")
#     print("2. Retirar")
#     print("3. Consultar saldo")
#     print("4. Salir")

#     try:
#         opcion = int(input("Ingrese una opción: "))

#         if opcion == 1:
#             cantidad = float(input("Ingrese la cantidad a depositar: "))
#             saldo += cantidad
#             print(f"Depósito exitoso. Saldo actual: {saldo}")

#         elif opcion == 2:
#             cantidad = float(input("Ingrese la cantidad a retirar: "))
#             if cantidad <= saldo:
#                 saldo -= cantidad
#                 print(f"Retiro exitoso. Saldo actual: {saldo}")
#             else:
#                 print("Fondos insuficientes.")

#         elif opcion == 3:
#             print(f"Este es tu saldo: {saldo}")

#         elif opcion == 4:
#             break
#         else:
#             print ("Opción inválida")
        
#     except ValueError:
#         print("Error: Ingrese un número válido.")

def mostrar_menu():
    """Muestra el menú principal."""
    print("----Bienvenido al Banco del pueblo----")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Consultar saldo")
    print("4. Salir")

def depositar(saldo):
    """Permite depositar dinero."""
    cantidad = float(input("Ingrese la cantidad a depositar: "))
    saldo += cantidad
    print(f"Depósito exitoso. Saldo actual: {saldo}")
    return saldo

def retirar(saldo):
    """Permite retirar dinero si hay fondos suficientes."""
    cantidad = float(input("Ingrese la cantidad a retirar: "))
    if cantidad <= saldo:
        saldo -= cantidad
        print(f"Retiro exitoso. Saldo actual: {saldo}")
    else:
        print("Fondos insuficientes.")
    return saldo

def consultar_saldo(saldo):
    """Muestra el saldo actual."""
    print(f"Este es tu saldo: {saldo}")

def main():
    saldo = 0
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Ingrese una opción: "))

            if opcion == 1:
                saldo = depositar(saldo)
            elif opcion == 2:
                saldo = retirar(saldo)
            elif opcion == 3:
                consultar_saldo(saldo)
            elif opcion == 4:
                break
            else:
                print("Opción inválida")
        except ValueError:
            print("Error: Ingrese un número válido.")

if __name__ == "__main__":
    main()


