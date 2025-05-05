# 1. Pedir que se ingrese un número y se imprima el triple
numero = int(input("Ingrese un número: "))  # Usar input para recibir el número
print(numero * 3)  # Imprimir el triple

# 2. Pedir que se ingrese un número, pero que se imprima la mitad, como número entero
numero = float(input("Ingrese un número: "))  # Usar input para recibir el número
division = numero // 2  # División entera con doble // para truncar el decimal
print(int(division))  # Imprimir el resultado como entero

# 3. Pedir que se ingresen 3 notas y se muestre el promedio
nota1 = int(input("Ingrese la primera nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
nota3 = int(input("Ingrese la tercera nota: "))

promedio_variable = (nota1 + nota2 + nota3) / 3  # Promedio con decimales
promedio_entero = (nota1 + nota2 + nota3) // 3  # Promedio entero

print("Promedio con decimales:", promedio_variable)
print("Promedio entero:", promedio_entero)

# 4. Pedir el diámetro de un círculo y calcular su área y perímetro
diametro = float(input("Ingrese el diámetro de un círculo: "))
radio = diametro / 2  # Radio es la mitad del diámetro

pi = 3.14
area = (radio ** 2) * pi  # Fórmula para el área
perimetro = diametro * pi  # Fórmula para el perímetro

print(f"El área es: {area} y el perímetro es: {perimetro}")

# 5. Pedir 2 números y mostrar la división entre ellos y el resto
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

division = numero1 / numero2
resto = numero1 % numero2

print(f"El resultado de la división es: {division}, el resto es: {resto}")

# 6. Pedir alto, ancho y largo de una pileta rectangular en cm. Calcular el volumen
alto = float(input("Indicar el alto en cm: "))
ancho = float(input("Indicar el ancho en cm: "))
largo = float(input("Indicar el largo en cm: "))

volumen = alto * ancho * largo
print(f"El volumen es: {volumen} cm³")

# 7. Pedir ancho y largo de un terreno y mostrar cuántos paneles de pasto hay que comprar (son de 60x60 cm)
ancho = float(input("Indicar el ancho del terreno en metros: "))
largo = float(input("Indicar el largo del terreno en metros: "))

area = ancho * largo
paneles = area / 3.6  # Cada panel de pasto tiene un área de 0.6m x 0.6m = 0.36 m²

print(f"La cantidad de paneles que debes comprar es: {paneles}")

# 8. Pedir datos de 4 productos comprados, con su cantidad y precio unitario y mostrar cuánto se gasta en total
producto1 = input("Ingrese el nombre del primer producto: ")
producto2 = input("Ingrese el nombre del segundo producto: ")
producto3 = input("Ingrese el nombre del tercer producto: ")
producto4 = input("Ingrese el nombre del cuarto producto: ")

cantidad1 = int(input(f"Ingrese la cantidad que compró del {producto1}: "))
cantidad2 = int(input(f"Ingrese la cantidad que compró del {producto2}: "))
cantidad3 = int(input(f"Ingrese la cantidad que compró del {producto3}: "))
cantidad4 = int(input(f"Ingrese la cantidad que compró del {producto4}: "))

precio1 = float(input(f"Ingrese el precio del {producto1}: "))
precio2 = float(input(f"Ingrese el precio del {producto2}: "))
precio3 = float(input(f"Ingrese el precio del {producto3}: "))
precio4 = float(input(f"Ingrese el precio del {producto4}: "))

precio_unitario_1 = precio1 / cantidad1
precio_unitario_2 = precio2 / cantidad2
precio_unitario_3 = precio3 / cantidad3
precio_unitario_4 = precio4 / cantidad4

suma_total = precio1 + precio2 + precio3 + precio4

print(f"Para el {producto1} se gastó ${precio_unitario_1:.2f}")
print(f"Para el {producto2} se gastó ${precio_unitario_2:.2f}")
print(f"Para el {producto3} se gastó ${precio_unitario_3:.2f}")
print(f"Para el {producto4} se gastó ${precio_unitario_4:.2f}")
print(f"La suma total es: ${suma_total:.2f}")

# 9. Escribir un programa que inicialice una tupla con los colores cálidos, luego ingrese un color y diga si es cálido o no
colores_calidos = ("rojo", "naranja", "amarillo")
color = input("Ingrese un color: ")

print(color.lower() in colores_calidos)  # Verifica si el color ingresado está en la tupla

# 10. Escribir un programa para un instituto de enseñanza que inicialice una tupla con 8 cursos
cursos = ("electricidad", "gasista", "tecnico", "cocina", "profesor", "limpieza", "conductor", "psicologo")

nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuántos años tienes? "))
curso_persona = input("¿Qué curso deseas realizar? ")

print(f"Hola, {nombre}. Tu edad es {edad}. El resultado de tu inscripción es: {'puedes' if curso_persona.lower() in cursos else 'no puedes'} realizar el curso.")
