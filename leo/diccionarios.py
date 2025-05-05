#diccionarios // conjuntos 

#Crea un diccionario que contenga la información de una persona: nombre, edad y país.
#Luego, imprime cada clave con su valor.

"""
informacion={"nombre":"juan","edad":"20","pais":"alemania"}

for i in informacion:
    print(i , ":" , informacion[i])
"""
#Tienes una lista de 8 frutas y querés contar cuántas veces aparece cada una usando un diccionario.

"""
frutas = {"manzana","pera","kiwi","kiwi","naranja","mandarina","sandia","uva","banana","banana"}
conteo = {}

for i in frutas:
    if i in conteo:
        conteo[i] += 1
    else:
        conteo[i] = 1

print(conteo)
""" 
###revisar
""" 
frutas = ["manzana", "banana", "pera", "manzana", "banana", "manzana"]

conteo = {}

for fruta in frutas:
    if fruta in conteo:
        conteo[fruta] += 1
    else:
        conteo[fruta] = 1

print(conteo)

""" 
#Crea un programa que guarde nombres de usuarios con sus contraseñas. 
# Luego pedile al usuario que escriba su nombre y, si existe, mostrale su contraseña.
"""
usuarios = {"juan":"hola2020","jose":"kilo2020","matias":"ageparalavida"}

ingreso = input(("Ingrese su nombre: "))

if ingreso in usuarios: 
    print("Tu contraseña es: ", usuarios[ingreso])
else:
    "Usuario no encontrado"

"""
#Crea un diccionario llamado inventario con 10 productos y su cantidad en stock. 
# Luego imprimí los productos que tienen más de 0 unidades.

"""
inventario = {"lavandina":20,"detergente":5,"bolsas":4,"esponja":6,"shampoo":3,"jabon":0}

for productos in inventario:
    if inventario[productos] > 0:
        print("El stock es: ",inventario[productos], "unidades")
    
"""
#Tenés un diccionario con nombres y edades. Sumale 1 año a cada persona (como si fuera su cumpleaños).
"""
edades= {"juan":9,"mirta":49,"pepe":89}

for nombres in edades:
    edades[nombres] += 1
print(edades)

"""

"""
colores= {"rojo":"#FF1458", "verde": "#00FF34", "azul":"F563F"}

valor_buscado= "#FF1458"

for clave in colores:
    if colores[clave]== valor_buscado:
        print ("La clave es", clave)

"""
#Pedirle al usuaurio un palabra y guardar en un diccionario cuantas veces aparece cada letra 
"""
palabra = input("ingrese una palabra: ")

letras = {}

for letra in palabra:
    if letra in letras:
        letras[letra] += 1
    else:
        letras[letra] = 1
print(letras)

"""
#Crear un diccionario que traduzca números del 1 al 7 en palabras. 
# Pedirle al usuario que ingrese un número y mostrar su versión en texto.
"""
numeros = {1:"uno",2:"dos",3:"tres",4:"cuatro",5:"cinco"}

ingreso_numero = int(input("Ingrese un número: "))

if ingreso_numero in numeros:
    print("Tu número es", numeros[ingreso_numero])
else:
    print("Tu número no está en la lista :)")
"""

#Crear un diccionario con nombres de 5 personas y sus números de teléfono. 
# Luego pedile un nombre al usuario y mostrale su número.

"""
agenda = {"juan":"2326429584","pepe":"1125123245","roman":"2326428855","lucha":"1123455455","nahuel":"2325443322"}

nombre = input("Ingrese su nombre de usuario: ")

if nombre in agenda: 
    print("el numero del" , nombre , "es ", agenda[nombre])
else:
    print("No estás en la agenda")

"""

#Tenes un diccionario de 5 alumnos con sus notas y a todos les vas a subir automaticamente un punto por participar en clase
"""
notas = {"juan":4,"pepe":6,"roman":7,"lucha":7,"nahuel":6}

for alumnos in notas:
    notas[alumnos] += 1
print("Notas actualizadas" , notas)

"""
"""
Tenés un diccionario de colores y sus códigos hexadecimales. 
Pedile al usuario un código, y decile si existe y a qué color pertenece.

"rojo": "#FF0000",
"verde": "#00FF00",
"azul": "#0000FF"

colores = {"rojo": "#FF0000","verde": "#00FF00","azul": "#0000FF"}

codigo = input("Ingrese el código: ")
encontrado = False

for color in colores:
    if colores[color] == codigo:
        print("Tu codigo es: ", color)
        encotrado = True
        break
if not encontrado:
    print("El codigo no está en el diccionario")

"""
"""
colores = {
    "rojo": "#FF0000",
    "verde": "#00FF00",
    "azul": "#0000FF"
}

codigo = input("Ingresá un código de color (ej: #FF0000): ")

encontrado = False

for color in colores:
    if colores[color] == codigo:
        print("Ese código corresponde al color", color)
        encontrado = True
        break

if not encontrado:
    print("Ese código no está en el diccionario.")
"""

##Crea una función llamada contar_palabras que reciba una lista de palabras y 
# devuelva un diccionario donde las claves sean las palabras y los valores cuántas veces aparece cada palabra. 
# Usa bucles y diccionarios.
"""
def contar_palabras(lista):
    conteo = {}
    for palabra in lista:
        if palabra in conteo: 
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    return conteo

palabras = ["gato","perro","gato","pez","perro","tortuga"]
print(contar_palabras(palabras))
"""
#Crea una función llamada crear_agenda que le pida al usuario ingresar nombres y teléfonos (usando input) hasta que escriba "salir".
#  Guarda los datos en un diccionario. Luego muestra todos los contactos con un bucle.
"""
def crear_agenda():
    agenda = {}
    while True:
        nombre = "Ingrese su nombre para agendar: . Si desear salir ingrese (salir)"
        if nombre.lower == "salir":
            break
    telefono = input("Ingrese su numero de teléfono: ")
    agenda[nombre] = telefono
    print("/n agenda: ")
    for nombre,telefono in agenda.items():
        print("El nombre", nombre, "el telefono es", telefono)

crear_agenda()
"""
#Crea una función promedios_alumnos que reciba un diccionario con nombres de alumnos como claves y listas de notas como valores. 
# La función debe devolver otro diccionario con los nombres y su promedio.
"""
def promedios_alumnos(diccionario):
    promedios = {}
    for alumnos,notas in diccionario.items():
        promedio = sum(notas) / len(notas)
        promedios[alumnos] = round(promedios,2)
    return promedios

alumnos = {"ana":[7,8,9],"luis":[6,6,7],"pedro":[10,9,8]}
print(promedios_alumnos(alumnos))
"""
"""
def promedios_alumnos(diccionario):
    promedios = {}
    for alumno, notas in diccionario.items():
        promedio = sum(notas) / len(notas)
        promedios[alumno] = round(promedio, 2)
    return promedios

# Prueba
alumnos = {
    "Ana": [7, 8, 9],
    "Luis": [6, 6, 7],
    "Pedro": [10, 9]
}
print(promedios_alumnos(alumnos))
"""
#Crea una función llamada mostrar_frutas que tenga un diccionario con 3 frutas y sus colores. 
# La función debe imprimir cada fruta con su color usando un bucle for.

"""
def mostrar_frutas():
    frutas = {"manzana":"rojo","uva":"morado","pera":"amarilo"}
    for fruta,color in frutas.items():
        print("La fruta es de color",color)

mostrar_frutas()
"""

# Crea un diccionario llamado persona con los siguientes datos:

# nombre: "Ana"

# edad: 10

# ciudad: "Madrid"

# Luego, imprime el contenido del diccionario.
"""
persona = {"nombre":"ana","edad":"10","ciudad":"madrid"}
print(persona)
"""
"""
mascota = {
    "nombre": "Luna",
    "animal": "perro",
    "edad": 5
}

print("Nombre:",mascota["nombre"])
print("Edad:",mascota["edad"])
"""

#Pide al usuario que ingrese una palabra. 
# Luego, crea un diccionario donde las claves sean las letras y los valores cuántas veces aparece cada letra en la palabra.

#Ejemplo (si el usuario escribe "banana"):
"""
ingreso_palabra = input("Ingrese una palabra:   ")
contador = {}
for letra in ingreso_palabra:
    if letra in contador:
        contador[letra] += 1
    else:
        contador[letra] = 1

print(contador)
"""


#Aumenta el precio de la "banana" en 20 unidades y luego muestra el diccionario actualizado.
"""
frutas = {"manzana": 100, "banana": 80, "naranja": 90}

frutas["banana"] += 20

print(frutas)

"""



#Pide al usuario que ingrese un color. Verifica si ese color está en el diccionario. 
# Si está, muestra el código hexadecimal. Si no, muestra un mensaje de "Color no encontrado".
"""
colores = {"rojo": "#FF0000", "verde": "#00FF00", "azul": "#0000FF"}

ingreso_color = input("Ingrese un color: ")

if ingreso_color in colores:
    print("El codigo del color es: ", colores[ingreso_color])
else:
    print("color no encontrado")

"""

#Tienes un diccionario con un coche. Cambia el modelo y agrega el año.
"""
coche = {
    "marca": "Toyota",
    "modelo": "Corolla"
}

coche["modelo"] = "Honda"
coche["año"] = 1990

print(coche)

"""

#Crea un diccionario vacío llamado alumno. Agrega las claves nombre, edad y curso con sus respectivos valores.
"""
alumno = {}

alumno["nombre"] = "pepe"
alumno["edad"] = 10
alumno["curso"] = "cine"

print(alumno)

"""


#Tienes un diccionario con asignaturas. Elimina la asignatura "historia".
"""
asignaturas = {
    "matemáticas": 8,
    "historia": 7,
    "ciencias": 9
}

del asignaturas["historia"]
print(asignaturas)

"""

#cree un diccionario con 3 países y 3 capitales, mostrar todo usado un bucle for 
"""
paises = {"españa":"madrid","paises bajos":"amsterdam","italia":"roma"}

for pais,capital in paises.items():
    print(f"{pais}:{capital}")

"""

#tienes un diccionario con una persona. Pide un nuevo valor para la edad y actualizalo 
"""
persona = {"nombre":"juan","edad":"20"}

nuevo_valor = int(input("Ingrese un nuevo valor para la edad:  "))

persona["edad"] = nuevo_valor

print(persona)
"""
#cree un diccionario llamado notas con las asignaturas matematicas, lengua, sociales 
#asignale un valor a cada una y luego asigna la nota de lengua
"""
notas = {"matemáticas":8,"lengua":2,"sociales":1}

print(notas["lengua"])

"""

#Crea un diccionario con tres animales y los sonidos que hacen. Luego intenta acceder al sonido, por ejemplo de gato, usando .get() para evitar errores 
# si no esta 
"""
animales = {"perro":"guag","gato":"","oso":"grr"}

print(animales.get("oso"),"no se encontro el sonido")

"""


#sumarle 50 puntos y subir al nivel 2
"""
juego = {"puntos": 100, "nivel": 1}

juego["puntos"] += 50
juego["nivel"] += 1

print(juego)

"""
#pide al usuario su nombre y edad, guardarlo en un diccionario y imprimirlo 
"""
nombre = input("ingrese su nombre: ")
edad = int(input("ingrese su edad "))

diccionario = {"nombre":nombre,"edad":edad}

print(diccionario)
"""

#Dado un diccionario con frutas y la cantidad de cada una, cuenta cuántas frutas hay en total.
"""
frutas = {"manzana":1,"peras":3,"durazno":4,"banana":2}
total = 0

for cantidad in frutas.values():
    total += cantidad
    
print("El total de frutas es : ", total)
"""

#Pide al usuario una fruta y dile si está o no en el diccionario.
"""
frutas = {"manzana":1,"peras":3,"durazno":4,"banana":2}

buscada = input("Qué tipo de fruta estás buscando: ")

if buscada in frutas:
    print("Si está ",buscada)
else:
    print("No esta en la lista")

"""

#Imprime solo los elementos cuyo valor sea mayor que 3.
"""
frutas = {"manzana":1,"peras":3,"durazno":4,"banana":2}

for fruta,cantidad in frutas.items():
    if cantidad > 3:
        print("Es mayor a 3")

"""

#Usa un bucle while para pedir frutas y cantidades, y guárdalas en un diccionario. Termina cuando se escriba "salir".
"""
frutas = {}

while True:
    nombre = input("Ingrese una fruta:   . Si desea salir escriba salir   ")
    if nombre == "salir":
        break
    cantidad = input("Ingrese la cantidad:   ")
    frutas[nombre] = cantidad

print(frutas)

"""

#Suma todos los valores del diccionario.
"""
frutas = {"manzana":1,"peras":3,"durazno":4,"banana":2}

suma = 0

for valor in frutas.values():
    suma += valor

print("suma total es: ", suma)

"""

#Pide al usuario una frase y cuenta cuántas veces aparece cada palabra.

frase = input("Ingrese una frase:  ")
palabras = frase.split() 
contador = {}


for palabra in palabras:
    if palabra in contador:
        contador += 1
    else:
        contador = 1
print("el total es: ", contador)