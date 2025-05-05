"""
# for variable in range(donde empieza, donde termina, salto)
# mostrar una lista desde el 0 hasta el 10, de a 1
for n in range(11):
    print(n) 

# lista del 1 al 12 de los impares
for n in range(1,13,2):
    print(n)

# Escribir un programa que pida al usuario una palabra y la muestre 10 veces por pantalla.
palabra = input("Ingrese una palabra: ")
for n in range(10):
    print(palabra)

# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
edad = int(input("Ingrese su edad: "))
for n in range(edad):
    print("Has cumplido : ", n+1 , "años")

# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
numero = int(input("Ingrese un numero entero: "))
for n in range(1,numero + 1 , 2):
    print(n, end= ". ")

# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
numero = int(input("Ingrese un numero entero: "))
for n in range(numero , -1 , -1):
    print(n , end= ", ")

# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
# y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
cantidad = float(input("Ingrese una cantidad a invertir: "))
interes = float(input("Ingrese el interes anual: "))
años = int(input("Ingrese el numero de años: "))
for n in range(años):
    cantidad *= 1 + interes/100
    print("Capital tras " , n+1 , "años" , round(cantidad,2))

# Dibujo de triángulo de asteriscos
n = int(input("Introduzca la altura del triángulo con un número entero positivo : "))
for i in range(n):
    for j in range(i + 1):
        print("*", end="")
    print("")

# Tabla de multiplicar
for y in range(1,11):
    for x in range(1,11):
        print(x * y, end="\t")
    print("")

# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
entero = int(input("Ingrese un numero entero : "))
for x in range(1, entero +1  , 2):
    for y in range(x , 0 , -2):
        print(y , end= " ")
    print("")   

# Imprimir todos los dígitos decimales, del 0 al 9, utilizando una repetición.
for n in range(10):
    print(n)

# Imprimir todos los números entre el 100 y el 199.
for n in range(100 , 200):
    print(n)

# Imprimir los números entre el 5 y el 20, saltando de tres en tres.
for n in range(5, 21, 3):
    print(n)

# Requerir al usuario que ingrese un número entero positivo e imprimir todos los números correlativos entre el ingresado por el usuario y uno menos del doble del mismo.
entero = int(input("Ingrese un numero entero: "))
for n in range(entero , entero * 2):
    print(n)

# Escribir un programa que solicite al usuario una cantidad y luego itere la cantidad de veces dada. En cada iteración, solicitar al usuario que ingrese un número. Al finalizar, mostrar la suma de todos los números ingresados.
cantidad = int(input("Ingrese una cantidad: "))
total = 0
for n in range(cantidad):
    numero = int(input("Ingrese un numero entero: "))
    total += numero
    print(total)

# Solicitar al usuario que ingrese una frase y luego imprimir un listado de las vocales que aparecen en esa frase (sin repetirlas).
frase = input("Ingrese una frase: ")
for n in "aeiou":
    if n in frase:
        print(n)

# Solicitar al usuario que ingrese una frase y luego imprimir la cantidad de vocales que se encuentran en dicha frase.
frase = input("Ingrese una frase: ")
vocales = 0
for n in frase:
    if n in "aeiou":
        vocales += 1
print(vocales)

# Escribir un programa que muestre la sumatoria de todos los números entre el 0 y el 100.
x = 0
for n in range(101):
    x += n
print(x) 

# Dado un número entero positivo, mostrar su factorial.
entero = int(input("Ingrese un numero entero: "))
f = 1 
if entero != 0:
    for i in range(1,entero + 1):
        f = f * i
print(f)

# Escribe un programa que pida al usuario un número y muestre su tabla de multiplicar del 1 al 10.
numero = int(input("Ingrese un numero entero: "))
for n in range(1,11):
    print(f"{numero} x {n} = {numero * n}")

# Escribe un programa que pida al usuario una palabra y luego la imprima de atrás hacia adelante.
palabra = input("Ingrese una palabra: ")
for n in range(len(palabra) - 1, -1, -1):
    print(palabra[n], end="")
print()

# Pide al usuario un número y haz una cuenta regresiva desde ese número hasta 1.
numero = int(input("Ingrese un numero entero: "))
for n in range(numero,0, -1):
    print(n)

# Pide al usuario un número, y luego calcula y muestra la suma de todos los números impares entre 1 y ese número (inclusive).
numero = int(input("Ingrese un número entero: "))
suma_impares = 0
for n in range(1, numero + 1):
    if n % 2 != 0:
        suma_impares += n
print("La suma de los números impares es:", suma_impares)
"""
"""
# Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. 
# La sucesión comienza con los números 0 y 1 y, a partir de éstos, cada elemento es la suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
a = 0
b = 1
for n in range(10):
    print(a, end=" ")
    a = b
    b += a

"""

#Escribir un programa que permita al usuario ingresar 6 números enteros, que pueden ser positivos o negativos. 
# Al finalizar, mostrar la sumatoria de los números negativos y el promedio de los positivos.
#No olvides que no es posible dividir por cero, por lo que es necesario evitar que el programa arroje un error si no se ingresaron números positivos.

"""

suma_negativos = 0
suma_positivos = 0
cantidad_positivos = 0 


for n in range(7):
    numeros = int(input("Ingrese 6 numeros enteros positivos o negativos: "))
    if numeros > 0:
        suma_positivos += numeros
        
    elif numeros / 0:
        print("Ingrese numeros positivos")
    else:
        suma_negativos += numeros
"""
"""   
    
suma_negativos = 0
suma_positivos = 0
cantidad_positivos = 0 

for n in range(7):
    numeros = int(input("Ingrese 6 numeros enteros positivos o negativos: "))
    if numeros > 0:
        suma_positivos += numeros
        cantidad_positivos += 1
    else:
        suma_negativos += numeros
print("La suma de los negativos es: ", suma_negativos, )
if cantidad_positivos != 0:
    print("El promedio de lo positivo es: " , suma_positivos / cantidad_positivos)
else:
    print("No se ingresaron numeros positivos")

"""

# Un grupo de amigos decide organizar un juego de estrategia, para lo cual forman dos equipos de 6 integrantes cada uno, 
# donde un integrante de cada equipo es el “jefe” y los otros 5 son sus “oficiales”. La regla más importante del juego es que sólo se 
# comunicarán mediante un canal común, por lo que deben buscar la forma de ocultar el contenido de sus mensajes. Uno de los equipos decide 
# utilizar un método antiguo de encriptación llamado “la cifra del césar”, que consiste en correr cada letra del mensaje –considerando 
# la posición de cada una en el alfabeto– una determinada cantidad de lugares. Ejemplo: si el corrimiento es de 2 lugares, la palabra “ATAQUE” se transforma en “CVCSWG”.

# Cada día, el “jefe” del equipo debe enviar un mensaje a cada uno de sus oficiales. Escribir un programa que permita encriptar los 5 mensajes.
#  El corrimiento (cantidad de lugares que se correrán las letras) será dado por el usuario antes de comenzar a encriptar. Los 5 mensajes usarán el mismo corrimiento.
# Nota: si el alfabeto termina antes de poder correr la cantidad de lugares necesarios, se vuelve a comenzar desde la letra “a”. 
# Ejemplo: la palabra “EXTRA” corrida 3 lugares se convierte en “HAWUD”. Utilizando el alfabeto español, de 27 letras, 
# el siguiente cálculo matemático permite volver a comenzar por el principio una vez que se llegó a la “z”: (índice de la letra a correr+corrimiento)%27
# Sólo se encriptarán las letras de los mensajes, dejando al resto de caracteres sin modificación.
"""
alfabeto = "abcdefghijkmnñopqrstuvwxyz"
correr = int(input("Cuántos lugares desea correr el mensaje? "))

for n in range(6):
    mensaje = input("Ingrese el mensaje en encriptar: ")
    encriptado = ""
    for caracter in mensaje:
        if caracter.lower() in alfabeto:
            indice = alfabeto.find(caracter.lower())
            indice = (indice + correr)%27
            encriptado += alfabeto[indice]
        else:
            encriptado += caracter
print("*** mensaje encriptado: " ,encriptado)

"""
#Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese rango,  que sean bisiestos y múltiplos de 10. 
# Nota: para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.

"""
año_inicio= int(input("Ingrese el primer año: "))
año_fin= int(input("Ingrese el ultimo año: "))

for anio in range(año_inicio,año_fin +1):
    if not anio % 10 == 0:
        continue
    elif not anio % 4 == 0:
        continue
    elif anio % 1000 != 0 or anio % 400 == 0:
        print(anio)
    else:
        print("Error")

"""
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
"""
key = "contraseña"
password = ""

while password != key:
    password = input("introduzca la contraseña: ")

print("contraseña correcta")
"""
"""

#Escribir un programa que pida al usuario un número entero positivo mayor que 2 y muestre por pantalla si es un número primo o no.

numero = int(input("Pida al usuario un numero entero positivo mayor que dos: "))
i = 2

while numero % i != 0:
    i += 1
    if i == numero:
        print("Es un numero primo")
    else:
        print("no es primo")

"""

#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

#             -1   
#     m  a  m  a 
# -1  0  1  2  3
"""
palabra = input("Ingrese una palabra: ")


for n in range(len(palabra) -1, -1):
    print(palabra[n])

"""

#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
"""
frase = input("Ingrese una frase: ")
letra = input("ingrese una letra: ")
cantidad= 0

for n in frase:
    if n in letra:
        cantidad += 1

print("La cantidad de veces que aparece ", letra, "en" , frase, "es" , cantidad)
        
"""


# def nombre de la funcion (argumentos formales(pueden o no existir)):
    #codigo 
    #return
