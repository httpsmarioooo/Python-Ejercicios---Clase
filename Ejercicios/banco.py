print("----Bienvenido al Banco del pueblo----")
saldo = 0

while True:
    print("1. Depositar")
    print("2. Retirar")
    print("3. Consultar saldo")
    print("4. Salir")

    try:
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            saldo += cantidad
            print(f"Depósito exitoso. Saldo actual: {saldo}")

        elif opcion == 2:
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            if cantidad <= saldo:
                saldo -= cantidad
                print(f"Retiro exitoso. Saldo actual: {saldo}")
            else:
                print("Fondos insuficientes.")

        elif opcion == 3:
            print(f"Este es tu saldo: {saldo}")

        elif opcion == 4:
            break
        else:
            print ("Opción inválida")
        
    except ValueError:
        print("Error: Ingrese un número válido.")
