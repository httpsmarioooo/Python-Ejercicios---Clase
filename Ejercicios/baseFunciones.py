def calcular_area(base, altura):
    area = base * altura
    return area

def main():
    print("Calculadora de áreas")
    
    while True:
        print("\nOpciones:")
        print("1. Calcular área de un rectángulo")
        print("2. Calcular área de un triángulo")
        print("3. Salir")
        
        opcion = input("Ingrese su opción: ")
        
        if opcion == "1":
            # Pedir al usuario que ingrese la base y la altura para un rectángulo
            try:
                base = float(input("Ingrese la base del rectángulo: "))
                altura = float(input("Ingrese la altura del rectángulo: "))
                
                # Calcular y mostrar el área del rectángulo
                area_rectangulo = calcular_area(base, altura)
                print(f"El área del rectángulo es: {area_rectangulo}")
            except ValueError:
                print("Error: Ingrese números válidos.")
                
        elif opcion == "2":
            # Pedir al usuario que ingrese la base y la altura para un triángulo
            try:
                base = float(input("Ingrese la base del triángulo: "))
                altura = float(input("Ingrese la altura del triángulo: "))
                
                # Calcular y mostrar el área del triángulo
                area_triángulo = calcular_area(base, altura) / 2
                print(f"El área del triángulo es: {area_triángulo}")
            except ValueError:
                print("Error: Ingrese números válidos.")
                
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    main()
