# # print("¿Cual es tu nombre?: ")
# # hombre = input()
# # print("¿Cual es tu apellido?: ")
# # apellido = input()
# # print ("Hola", hombre, apellido)


# print ("El Gran Torneo de las Estrellas\n")
# print ("Era una mañana soleada en la ciudad deportiva, y el entrenador Marcos caminaba de un lado a otro con su libreta en la mano. Faltaban pocos días para el Gran Torneo de las Estrellas, donde los mejores jugadores competirían para demostrar su talento. Pero había un problema: la lista de jugadores aún no estaba completa. Marcos necesitaba encontrar a los últimos dos jugadores para completar el equipo\n")
# print ("Marcos se acercó a ti, su asistente de confianza, y te dijo con urgencia: \n")
# print ("— ¡Necesito que registremos a nuestros jugadores cuanto antes! Para hacerlo bien, necesitamos algunos datos clave.\n")
# print ("Sacó su lista y comenzó a enumerar: \n")
# print ("— Primero, necesitamos el nombre del jugador. \n")
# jugadorA = input("— ¿Cómo se llama el primer jugador? ")
# trabajoA = input("— ¿Qué trabajo tiene el primer jugador? ")
# primerAbj = input("Dime una cualidad de " + jugadorA + ": ")
# segundaAbj = input("Dime otra cualidad de " + jugadorA + ": ")
# primeraComida = input("Dime la comida favorita de " + jugadorA + ": ")
# segundaComida = input("Dime otra comida favorita de " + jugadorA + ": ")
# sentimiento = input("Dime un sentimiento de " + jugadorA + ": ")
# print ("— ¡Perfecto! Ya tenemos toda la información. Ahora solo falta otros detalles. \n")

# print ("— Listo, pero ahora pasó algo, necesito que me ayudes a calculear el area de un rectangulo pra poder inscribirte. \n")
# base =  float(input("— ¿Cuál es la base del rectángulo? "))
# altura = float(input("— ¿Cuál es la altura del rectángulo? "))
# area = base * altura
# print ("— ¡Excelente! El área del rectángulo es: ", area, "\n")

# print("Otra vez pasó un problema, necesito que me ayudes a calcular la edad mia, porque se me olvido")
# anioNacimiento = int(input("— ¿En qué año nací? "))
# anioActual = int(input("— ¿En qué año estamos? "))
# edad = anioActual - anioNacimiento
# print ("— ¡Perfecto! Mi edad es: ", edad, "\n")

# print ("— ¡Excelente! Ya tenemos toda la información que necesitamos. Ahora solo falta un último detalle. \n")
# print ("Este el resumen de los datos que hemos recopilado: \n")
# print ("Nombre del jugador: " + jugadorA)
# print ("Trabajo: " + trabajoA)
# print ("Cualidades: " + primerAbj + " y " + segundaAbj)
# print ("Comida favorita: " + primeraComida + " y " + segundaComida)
# print ("Sentimiento: " + sentimiento)
# print ("Área del rectángulo: " + str(area))
# print ("Mi edad: " + str(edad) + "\n")

# print ("— ¡Ya está! ¡Hemos registrado a todos nuestros jugadores! Ahora solo falta esperar a que llegue el gran día del torneo. Fue un placer trabajar contigo, " + jugadorA + ". ¡Nos vemos en el campo de juego! \n")



print("\u2B50 EL GRAN TORNEO DEPORTIVO \n")
print("En la gran ciudad deportiva, el entrenador Marcos camina de un lado a otro con su libreta en la mano. ")
print("Faltan pocos días para el Gran Torneo y necesita completar la inscripción de su equipo.")

print("\nMarcos se acerca a ti con una mirada decidida y dice:")
print("— ¡Justo la persona que necesito! Ayúdame a inscribir a nuestro último jugador.")

# Registro del jugador
nombre = input("— ¿Cuál es su nombre?: ")
#Se pone una f antes de la cadena de texto porque es un f-string (formatted string), una característica de Python que permite incluir variables dentro de un string de manera sencilla y legible.
apellido = input("— ¿Cuál es su apellido?: ")
trabajo = input(f"— ¿Cuál es su profesión o trabajo {nombre}: ")
primera_cualidad = input(f"— Dime una cualidad de {nombre}: ")
segunda_cualidad = input(f"— Dime otra cualidad de {nombre}: ")
comida_fav1 = input(f"— ¿Cuál es la comida favorita de {nombre}?: ")
comida_fav2 = input(f"— Dime otra comida favorita de {nombre}: ")
sentimiento = input(f"— Dime un sentimiento que describa a {nombre}: ")

print("\n— ¡Genial! Ahora necesito tu ayuda para resolver algo importante. Para completar la inscripción del torneo, debemos calcular el área de una zona de entrenamiento.\n")

# Cálculo del área de un rectángulo
base = float(input("— ¿Cuál es la base del rectángulo?: "))
altura = float(input("— ¿Cuál es la altura del rectángulo?: "))
area = base * altura
print(f"— ¡Perfecto! El área del rectángulo es: {area} unidades cuadradas.\n")

print("Justo cuando todo parecía listo, Marcos se rasca la cabeza y suspira: ")
print("— ¡Ay no! Con tanto que hemos hecho, olvidé mi propia edad. ¿Puedes ayudarme a calcularla?\n")

anio_nacimiento = int(input("— ¿En qué año nací?: "))
anio_actual = int(input("— ¿En qué año estamos?: "))
edad = anio_actual - anio_nacimiento

print(f"— ¡Gracias, {nombre}! Ahora sé que tengo {edad} años. ¡Eres increíble!\n")

print("Marcos revisa sus notas y sonríe satisfecho. ")
print("— Todo está en orden. Aquí está el resumen de nuestro jugador estrella:")
print(f"\nNombre: {nombre} {apellido}\nTrabajo: {trabajo}\nCualidades: {primera_cualidad}, {segunda_cualidad}")
print(f"Comidas favoritas: {comida_fav1}, {comida_fav2}\nSentimiento clave: {sentimiento}")
print(f"Área del rectángulo: {area} unidades cuadradas\nEdad de Marcos: {edad} años\n")
print(f"— ¡Felicidades, {nombre}! Has sido registrado con éxito. Nos vemos en el torneo. ¡Daremos lo mejor de nosotros!\n")
