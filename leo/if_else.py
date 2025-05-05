# Programas de ejemplo

# Programa 1: Actualizar lista de destinos
destinos = ["Bariloche", "Chilecito", "Rosario", "Salta", "Tilcara", "Pumamarca"]
destinos_nuevo = input("Ingrese un destino: ") 
destinos.append(destinos_nuevo)
print(destinos)

# Programa 2: Lista de productos
productos = ["Esponja", "Shampoo", "Lavandina", "Crema", "Aerosol"]
productos_1 = input("Ingresar el nuevo producto: ")
productos_2 = input("Ingresar el nuevo producto: ")
productos_3 = input("Ingresar el nuevo producto: ")
productos.append(productos_1)
productos.append(productos_2)
productos.append(productos_3)
print(productos)

# Programa 3: Información de empleados
empleados = [["Juan", 28, "Ingeniero"], ["Ana", 32, "Diseñadora"], ["Pedro", 45, "Gerente"], ["Luisa", 29, "Analista de datos"]]
empleado_ana = empleados[1][0]
empleado_pedro = empleados[2][0]
puesto_pedro = empleados[2][2]
print(f"El nombre del segundo empleado: {empleado_ana}, el nombre del tercer empleado es: {empleado_pedro} y el puesto es: {puesto_pedro}")

# Programa 4: Feliz Año Nuevo
dia = "1 de enero"
if dia == "1 de enero":
    print("Feliz año nuevo!!!")

# Programa 5: Comprobación de fecha
dia = "2 de enero"
if dia == "1 de enero":
    print("Feliz año nuevo")
else:
    print("Hoy no es año nuevo!!!...")

# Programa 6: Clasificación por edad
edad = int(input("¿Qué edad tiene la persona? "))
if edad <= 2:
    print("Es un bebé")
elif edad <= 13:
    print("Es un niño/a")
elif edad <= 20:
    print("Es un adolescente")
else:
    print("Es un adulto")

# Programa 7: Clasificación de vehículo por ruedas
ruedas = int(input("Cuantas ruedas tiene tu vehiculo: "))
if ruedas == 1:
    print("Es un monociclo")
elif ruedas == 2:
    print("Es una moto")
elif ruedas == 3: 
    print("Es un triciclo")
elif ruedas == 4:
    print("Es un auto")
elif ruedas >= 5:
    print("Son demasiadas ruedas")
else: 
    print("No me chamuyes")

# Programa 8: Mayor de edad
edad = int(input("¿Qué edad tienes? "))
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("No eres mayor de edad")

# Programa 9: Comprobación de contraseña
key = "contraseña"
valor = input("¿Cuál es la contraseña? ")
if valor.lower() == key:
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")

# Programa 10: División de números
try:
    numero1 = int(input("Ingrese el número 1: "))
    numero2 = int(input("Ingrese el número 2: "))
    if numero2 == 0:
        print("No se puede dividir por cero")
    else:
        print(numero1 / numero2)
except ValueError:
    print("Error: Debe ingresar números enteros.")

# Programa 11: Par o impar
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

# Programa 12: Tributar impuestos
edad = int(input("Ingrese su edad: "))
ingresos = float(input("Ingrese sus ingresos mensuales: "))
if edad >= 16 and ingresos >= 1000:
    print("Tienes que tributar")
else:
    print("Afortunado, no tienes que tributar")

# Programa 13: Clasificación por grupo A o B
nombre = input("Ingrese su nombre: ")
sexo = input("¿Tu sexo es Masculino o Femenino? ").lower()
if sexo == "femenino" and nombre[0].upper() < "M":
    print("Tu grupo es el A")
elif sexo == "masculino" and nombre[0].upper() > "N":
    print("Tu grupo es el A")
else:
    print("Tu grupo es el B")

# Programa 14: Tramos impositivos
renta = float(input("Ingrese su renta anual: "))
if renta < 10000:
    tipo = 5
elif renta < 20000:
    tipo = 15
elif renta < 35000:
    tipo = 20
elif renta < 60000:
    tipo = 30
else:
    tipo = 45
print(f"Tienes que pagar el {tipo}%")

# Programa 15: Evaluación de empleados
bonificacion = 2400
puntos = float(input("Ingrese el valor del resultado final: "))
if puntos == 0.0:
    nivel = "Inaceptable"
elif puntos == 0.4:
    nivel = "Aceptable"
elif puntos >= 0.6:
    nivel = "Meritorio"
else:
    nivel = ""
if nivel:
    print(f"Tu rendimiento es {nivel}")
    print(f"Te corresponde cobrar {bonificacion * puntos}")
else:
    print("Puntuación no válida")

# Programa 16: Precio de entrada a sala de juegos
edad = int(input("Ingrese su edad: "))
if edad < 4:
    print("Entras gratis")
elif edad <= 18:
    print("Debes pagar 5 euros")
else:
    print("Tienes que pagar 10 euros")

# Programa 17: Pizzería
print("Pizzería Bella Napoli. \nTipos de pizza\n\t1- Vegetariana\n\t2- No Vegetariana\n")
tipo = input("Ingrese el tipo de pizza que desea: ")
if tipo == "1":
    print("Ingredientes de pizza Vegetariana\n\t1-Pimiento\n\t2-Tofu\n")
    ingrediente = input("Indique el ingrediente que desea: ")
    if ingrediente == "1":
        print("Pizza Vegetariana con Tomate, Mozzarella y Pimiento")
    else:
        print("Pizza Vegetariana con Tomate, Mozzarella y Tofu")
else:
    print("Ingredientes de pizza No Vegetariana\n\t1-Peperoni\n\t2-Jamón\n\t3-Salmón")
    ingrediente = input("Indique el ingrediente que desea: ")
    if ingrediente == "1":
        print("Pizza No Vegetariana con Tomate, Mozzarella y Peperoni")
    elif ingrediente == "2":
        print("Pizza No Vegetariana con Tomate, Mozzarella y Jamón")
    else:
        print("Pizza No Vegetariana con Tomate, Mozzarella y Salmón")
