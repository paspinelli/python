
#Escribir una funcion a la que se le pase un nombre como cadena y muestr por pantalla el saludo "hola, nombre"
"""
def saludo(nombre):
    print("hola, ", nombre)
    return

saludo("juan")

"""
#Escribir una función que reciba un número entero positivo y devuelva su factorial.
"""
def factorial(numero):
    tmp = 1
    for i in range(numero):
        tmp *= i +1 
    return tmp

print(factorial(4))

"""
#Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
# La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. 
# Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.
#return amount + amount*vat/100
"""
def factura(cantidad, iva = 21):
    return cantidad + cantidad * iva /100
print(factura(1000,10))
print(factura(1000))
"""

#Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.
"""
def area(radio):
    pi = 3.1415
    return pi * radio **2

def volumen(radio , altura):
    return area(radio) * altura

print(volumen(3,56))

### 
"""
"""
def circle_area(radius):
    pi = 3.1415
    return pi*radius**2

def cilinder_volume(radius, high):
    return circle_area(radius)*high

print(cilinder_volume(3,56))

"""

    #Solicitar al usuario que ingrese su dirección email.
    #Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo. 
    # Una dirección se considerará válida si contiene el símbolo "@".
"""
email = input("Ingresar tu email completo: ")    

def chequear(correo):
    if "@" in correo:
        print("Tu email esta completo")
    else:
        print("Tu email es erroneo")

chequear(email)
"""

"""
def validar(email):
    caracterBuscado="@"
    emailValido=False
    for c in email:
        if c==caracterBuscado:
            return True
    return False

 
direccion=input("Tu email: ")
if validar(direccion):
    print("Dirección válida")
else:
    print("Dirección inválida")

"""

#Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos (utilizando una función que realice dicha suma).

#nro = int(input("Ingrese cualquier número, cuando quiera finalizar ingrese 0"))
"""
def sumardigitos(numero):
    suma = 0
    while numero != 0:
        digito = numero % 10
        suma += digito
        numero = numero // 10
    return suma


numero = int(input("Ingrese cualquier número, cuando quiera finalizar ingrese 0  "))
while numero != 0:
    print("La suma es: ", sumardigitos(numero))
    numero = int(input("Ingrese cualquier número, cuando quiera finalizar ingrese 0  "))
"""

#Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos. 
# Al finalizar, mostrar la sumatoria de todos los números ingresados y la suma de sus dígitos. 
# Reutilizar la misma función realizada en el ejercicio 2.

"""
def sumadigitos(numero):
    suma = 0
    while numero != 0:
        digito = numero % 10
        suma += digito
        numero = numero //10
        return suma


sumatoria = 0
numero = int(input("Ingresar los numeros a sumar:  "))
while numero != 0:
    print("La suma es: ", sumadigitos(numero))
    sumatoria += numero
    numero = int(input("Ingresar los numeros a sumar:  "))
    print("La sumatoria es: ", sumatoria)
    print("Los digitos suman: ", sumadigitos(sumatoria))
"""

#Requerir al usuario que ingrese un número entero e informar si es primo o no, utilizando una función booleana que lo decida.

"""
def primo(numero):
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True
    

numero = int(input("Ingrese un numero: "))

if primo(numero):
    print("Es primo")
else:
    print("No es primo")

"""


#Solicitar al usuario un número entero y luego un dígito. 
#Informar la cantidad de ocurrencias del dígito en el número, utilizando para ello una función que calcule la frecuencia.
"""
def frecuencia(numero_entero, digito):
    acumulador = 0
    while numero_entero != 0:
        suma += 1
        numero_entero = int(input("Ingrese un numero entero: "))
    while digito != 0:
        suma += digito
        digito = int(input("Ingrese un solo digito: "))
        return 
        
numero_entero = int(input("Ingrese un numero entero: "))
digito = int(input("Ingrese un solo digito: "))

def frecuencia(numero,digito):
   cantidad=0
   while numero!=0:
       ultDigito=numero%10
       if ultDigito==digito:
           cantidad+=1
       numero=numero//10
   return cantidad

 
num=int(input("Número: "))
un_digito=int(input("Dígito: "))
print("Frecuencia del dígito en el número:",frecuencia(num,un_digito))
"""

#Escribir un programa que pida números al usuario, motrar el factorial de cada uno y, al finalizar, la cantidad total de números leídos en total. 
# Utilizar una o más funciones, según sea necesario.
"""
f = 1
def factorial(numeros):
"""

#Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. 
# Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.
"""
def dni(numero):
    if numero >= 7 and numero <= 9:
        return True
    else:
        return False
    
numero = int(input("Ingrese su numero de DNI: "))

if dni(numero) == True:
    print("Tu DNI es valido")
else:
    print("Tu DNI esta erroneo")
"""
"""
def validardni(dni):
    cantidad = 0
    while dni != 0:
        cantidad += 1
        dni // 10
    return cantidad == 7 or cantidad == 8

"""
#Escribir una función que, dado un string, retorne la longitud de la última palabra. 
# Se considera que las palabras están separadas por uno o más espacios. 
# También podría haber espacios al principio o al final del string pasado por parámetro.
"""
def ultpalabra(frase):
    if len(frase) == 0:
        return 0 
    cantidad = 0
    for i in range(len(frase)):
        if frase[i] != " ":
            cantidad += 1 
        else:
            if i < len(frase)-1 and frase[i+1]!=' ':
                print("Cantidad es = 0")
    return cantidad

"""


#Escribir una función que reciba un número entero y devuelva True si el número es par, o False si es impar.
"""
def numero(par):
    if par % 2 == 0:
        return True
    else:
        return False

# Pedimos un número al usuario
num = int(input("Ingresa un número entero: "))

# Mostramos el resultado
if numero(num):
    print("El número es par")
else:
    print("El número es impar")
"""
"""
#Escribir una función que reciba un número entero positivo y devuelva la suma de todos los números desde 1 hasta ese número. 
# Por ejemplo, si el usuario ingresa 5, la función debe devolver 1 + 2 + 3 + 4 + 5 = 15.

def numero(positivo):
    suma = 0  # Variable para acumular la suma
    for i in range(1, positivo + 1):  # Desde 1 hasta positivo (incluido)
        suma += i  # Sumamos cada número al acumulador
    return suma  # Devolvemos el resultado

# Probemos la función
num = int(input("Ingresa un número entero positivo: "))
resultado = numero(num)
print("La suma de 1 hasta", num, "es:", resultado)

"""
#Escribir una función que reciba un número entero y 
# devuelva una cadena que diga "positivo" si el número es mayor que 0, "negativo" si es menor que 0, o "cero" si es igual a 0.
"""
def numero(valor):
    if valor > 0:
        return "positivo"
    elif valor < 0:
        return "negativo"
    else:  # Si no es mayor ni menor que 0, entonces es 0
        return "cero"

# Probemos la función
num = int(input("Ingresa un número entero: "))
resultado = numero(num)
print("El número es:", resultado)
"""

#Escribir una función que reciba un número entero positivo y devuelva la cantidad de dígitos que tiene.
#  Por ejemplo, si el número es 123, la función debe devolver 3; si es 50, debe devolver 2.
"""
def numero(cantidad):
    if cantidad == 0:  # Caso especial para el 0
        return 1
    digitos = 0
    while cantidad > 0:
        digitos += 1
        cantidad //= 10  # División entera para quitar el último dígito
    return digitos

# Probemos la función
num = int(input("Ingresa un número entero positivo: "))
resultado = numero(num)
print("El número", num, "tiene", resultado, "dígitos")
"""

#Escribir una función que reciba una cadena de texto y devuelva True si la cadena tiene más de 5 caracteres, o False si tiene 5 o menos caracteres.
"""
def oracion(frase):
    return len(frase) > 5

texto = input("Ingresa una cadena de texto: ")
print("¿Tiene más de 5 caracteres?", oracion(texto))
"""

#Escribir una función que reciba una cadena de texto y devuelva el número de vocales (a, e, i, o, u) que contiene. 
# Por ejemplo, si la cadena es "hola", la función debe devolver 2 (por la "o" y la "a").
"""
def contar_vocales(texto):
    vocales = "aeiou"  # Definimos las vocales (puedes incluir "AEIOU" si quieres mayúsculas)
    contador = 0       # Variable para contar las vocales
    for letra in texto:  # Recorremos cada carácter en la cadena
        if letra.lower() in vocales:  # Convertimos a minúscula y verificamos si es vocal
            contador += 1
    return contador    # Devolvemos el total de vocales

# Probemos la función
cadena = input("Ingresa una cadena de texto: ")
resultado = contar_vocales(cadena)
print("El número de vocales es:", resultado)

#Escribir una función que reciba un número entero positivo y devuelva True si el número es un palindrome 
# (se lee igual de izquierda a derecha que de derecha a izquierda), o False si no lo es.
def es_palindromo(numero):
    texto = str(numero)       # Convertimos el número a cadena
    inverso = texto[::-1]     # Invertimos la cadena
    return texto == inverso   # Comparamos si son iguales

# Probemos la función
num = int(input("Ingresa un número entero positivo: "))
if es_palindromo(num):
    print("El número es un palíndromo")
else:
    print("El número no es un palíndromo")

"""

# meses_tupla = ("enero", "febrero", "marzo","abril", "mayo")
# meses_lista = ["enero", "febrero", "marzo","abril", "mayo"]
#diccionario : debe llevar clave y valor

# meses_dic = {"enero":1,"febrero":2,"marzo":3,"abril":4,"mayo":5}

#Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un 
# curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de 
# cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso,
#  y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.
"""
curso = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
total_creditos = 0

for asignatura,creditos in curso.items():
    print(asignatura, "tiene", creditos , "creditos")
    total_creditos += creditos
print("Numero total de creditos", total_creditos)

"""
"""
meses_lista = [("enero",1), ("febrero",2), ("marzo"),"abril", "mayo"]
print(meses_lista[1][1])
"""
#Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona 
# (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. 
# Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
"""
persona = {}
continuar = True 

while continuar: 
    clave = input("Qué dato quiere introduccir? ")
    valor = input(clave + " : ")
    persona[clave] = valor
    print(persona)
    continuar = input("Quiere añadir más información? Si no ").lower == "si"

"""
# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
# pregunte al usuario por una fruta, un número de kilos y 
# muestre por pantalla el precio de ese número de kilos de fruta. 
# Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

# Fruta	Precio
# Plátano	1.35
# Manzana	0.80
# Pera	0.85
# Naranja	0.70
"""
frutas = {"Plátano":1.35, "Manzana":0.80, "Pera": 0.85, "Naranja": 0.70}

fruta = input("Qué fruta quisiera: ")
kilos = float(input("Qué cantidad quisiera: "))

if fruta in frutas:
    print(kilos, "kilos de", fruta, "valen" , frutas[fruta] * kilos , "$" )
else:
    print("No se encuentra en la lista")

"""
#Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla 
# la misma fecha en formato de <mes> de aaaa donde <mes> es el nombre del mes.

#split("/")

"""
mes = {"enero":1, "febrero":2, "marzo":3,"abril":4,"mayo":5,"junio":6,"julio":7,"agosto":8,"septiembre":9,"octubre":10,"noviembre":11,"diciembre":12}

fecha = input("Ingrese una fecha en formato que lo tiene que ignresar dd/mm/aaaa:  ")

fecha = fecha.split("/")

print("La fecha que ingreso es", fecha[0], "de", mes[int(fecha[1])] , "de", fecha[2])
#####
"""
"""
meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}

fecha = input('Introduce una fecha en formato dd/mm/aaaa: ')

fecha = fecha.split('/')

print(fecha[0], 'de', meses[int(fecha[1])], 'de', fecha[2])

"""
#Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio. 
# Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la compra, 
# y una de las funciones anteriores, y utilice la función pasada para aplicar los descuentos o
#  el IVA a los productos de la cesta y devolver el precio final de la cesta.
"""
def aplicar_descuento(precio, descuento):
    return precio - precio * descuento / 100

def aplicar_iva(precio, porcentaje):
    return precio + precio * porcentaje /100

def precio_basquet(basquet, funcion):
    total = 0 
    for precio, descuento in basquet.items():
        total += funcion(precio, descuento)
    return total

print("el precio con descuento es: ", precio_basquet({1000:20,500:10,100:1},aplicar_descuento))
print("El precio de la compra con iva es: ", precio_basquet({1000:20,500:10,100:1},aplicar_iva))

"""

#Escribir una función 
# que reciba otra función y una lista, y devuelva otra lista con el resultado de aplicar la función dada a cada uno de los elementos de la lista.


"""
def aplicarfuncionlista(funcion, lista):
    l = []
    for i in lista:
        l.append(funcion(i))
    return l

def cuadrado(n):
    return n * n

print(aplicarfuncionlista(cuadrado,[1,2,3,4]))
"""
#Escribir una función que simule una calculadora científica que permita calcular el seno, coseno, tangente, exponencial 
# y logaritmo neperiano. La función preguntará al usuario el valor y la función a aplicar, 
# y mostrará por pantalla una tabla con los enteros de 1 al valor introducido y el resultado de aplicar la función a esos enteros.
"""
from math import sin, cos, tan, exp, log

def apply_function(f, n):
    '''
    Función que aplica una función a los enteros desde 1 hasta n.
    Parámetros:
        f: Es una función que recibe un número real y devuelve otro.
        n: Es un número entero positivo.
    Devuelve:
        Un diccionario con los pares i:f(i) para cada valor entero i de 1 a n.
    '''
    functions = {'sin':sin, 'cos':cos, 'tan':tan, 'exp':exp, 'log':log}
    result = {}
    for i in range(1, n+1):
        result[i] = functions[f](i)
    return result

def calculator():
    '''
    Función que aplica una función seleccionada por el usuario (seno, coseno, tangente, exponencial o logarítmo) a la lista de enteros desde 1 hasta n. 
    Imprime por pantalla una tabla con la secuencia de enteros y el resultado de aplicarles la función introducida.
    Parámetros:
        f: Es una cadena con la función a aplicar (sin, cos, tan, exp o log).
        n: Es un entero positivo.
    '''
    f = input('Introduce la función a aplicar (sin, cos, tan, exp, log): ')
    n = int(input('Introduce un entero positivo: '))
    for i, j in apply_function(f, n).items():
        print (i, '\t', j)
    return

calculator()
"""
# Escribir una funcióin que reciba otra función y una lista con el resultado aplicar la función dada a cada uno de los
# elementos de esa lista.
"""
def aplicar_funcion_lista (funcion, lista):
    l= []
    for i in lista:
        l.append(funcion(i))
    return l

def cuadrado(n):
    return n*n

print (aplicar_funcion_lista(cuadrado,[1,2,3,4,5,6,7,8,9]) )
"""

#Escribir una funcion que reciba otra funcion boleana y una  lista, y devuelva otra lista con los elementos de la lista que devuelvan true 
#al aplicar la funcion boleana 
"""
def funcion(funcion,lista):
    l = []
    for i in lista:
        if funcion(i):
            l.append(i)
    return l

def par(n):
    return n % 2 == 0

print(funcion(par,[1,2,2,3,4,5,6,6,7,8,9,0,10]))
"""
"""
def aplicar_funcion(funcion, lista):
    l = []
    for i in lista:
        if funcion(i):
            l.append(i)
    return l

def par(n):
    return n % 2 == 0

print(aplicar_funcion(par,[1,2,3,4,5,6,7,8,9]))
"""

#Escribir una función reciba una lista de notas y devuelva la lista de calificaciones correspondientes a esas notas.
"""
def calificaciones(nota):
    if nota < 5:
        return "no aprobo"
    elif nota > 7:
        return "aprobo con lo justo"
    elif nota > 9:
        return "sobresaliente"
    elif nota < 2:
        return "debe mejorar" 
    else:
        return "nota invalida"

def resultado(notas):
    return list(map(calificaciones,notas))

print(resultado([3,8,10,1]))
"""
"""
def grade(score):
  
    if score < 5:
        return 'SS'
    elif score < 7:
        return 'AP'
    elif score < 9:
        return 'NT'
    elif score < 10:
        return 'SB'
    else:
        return 'MH'

def apply_grade(scores):
   
    return list(map(grade, scores))

print(apply_grade([6.5, 5, 3.4, 8.2, 2.1, 9.7, 10]))

"""

#Escribir un programa que pida números positivos al usuario. Mostrar el número cuya sumatoria de dígitos fue mayor y la cantidad de números cuya sumatoria #de dígitos fue menor que 10. Utilizar una o más funciones, según sea necesario.
#revisar 
"""

def suma_digitos(numero):
    suma = 0
    while numero != 0:
        digito = numero % 10
        suma = suma + digito
        numero = numero // 10
    return suma

cantidad = 0
mayor = -1
numero = input("Ingrese un numero positivo: ")

while cantidad > 0:
    suma = suma_digitos(numero)
    if suma > mayor: 
        mayor = suma
        n_mayorsuma = numero
    if suma < 10:
        cantidad = cantidad +1
    numero = input("Ingrese un numero positivo: ")

print(mayor)
print(cantidad)
"""

#Crea un función EscribirCentrado, que reciba como parámetro un texto y lo escriba centrado en pantalla (suponiendo una anchura de 80 columnas; pista: #deberás escribir 40 - longitud/2 espacios antes del texto). Además subraya el mensaje utilizando el carácter =.
"""
def EscribirCentrado(texto):
    anchura_pantalla = 80
    espacios = (anchura_pantalla - len(texto)) // 2
    print(" " * espacios + texto)
    print(" " * espacios + "=" * len(texto))

# Ejemplo de uso
EscribirCentrado("Hola, mundo!")

"""

#Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. Crea una función EsMultiplo que reciba los dos #números, y devuelve si el primero es múltiplo del segundo.
"""
def esmultiplo(primer_nro,segundo_nro):
    return primer_nro % segundo_nro == 0

def principal():
    numero_1 = int(input("Ingrese el primer numero entero: "))
    numero_2 = int(input("Ingrese el segundo numero entero: "))
    if esmultiplo(numero_1,numero_2):
        print("numero 1 es multiplo de numero 2")
    elif esmultiplo(numero_2,numero_1):
        print("numero 2 es mutiplo de numero 1")
    else:
        print("No es multiplo")

principal()
"""
#Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto y devuelve una cadena con un espacio adicional tras cada letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use dicha función.
"""
def convertirespaciado(texto):
    return " ".join(texto)

def principal():
    texto = input("Ingrese un texto: ")
    texto_convertido = convertirespaciado(texto)
    print("El texto convertido con el espacio adicional es: ", texto_convertido)

principal()
"""

#Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.

#Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, solamente tenemos tres oportunidades para intentarlo.
"""

def login(usuario,contraseña, intentos):
    if usuario == "usuario1" and contraseña == "asdasd":
        return True,intentos 
    else:
        return False,intentos+1

def main():
    intentos = 0 
    max_intentos = 3
    while intentos < max_intentos:
        usuario = input("Ingrese el usuario: ") 
        contraseña = input("Ingrese la contraseña: ") 
        acceso,intentos = login(usuario,contraseña,intentos)
        if acceso:
            print("Login exitoso, Bienvenido")
            return
        else:
            print("usuario o contraseña incorrecto. Intento", intentos , "de " , max_intentos)
    print("Se excedio de numeros intentos, acceso denegado")

main()

"""
#Escribe una función que reciba dos números y una operación (+, -, *, /) y devuelva el resultado.
###############
"""
def calculadora(nro1, nro2, operacion):
    if operacion == "+":
        return nro1 + nro2
    elif operacion == "-":
        return nro1 - nro2
    elif operacion == "*":
        return nro1 * nro2
    elif operacion == "/":
        return nro1 / nro2 if nro2 != 0 else "No podes dividir por 0"
    else:
        return "Operacion no valida"
    
print(calculadora(10,2,"+"))

"""
#Crea una función que cuente el número de vocales en una palabra o frase

"""
def contar_vocales(texto):
    vocales = "aeiou"
    return sum(1 for letra in texto if letra in vocales)

print(contar_vocales("hola que tal"))

"""
"""
#Escribe una función que invierta una cadena sin usar [::-1].

def invertir_cadena(cadena):
    invertida = ""
    for letra in cadena:
        invertida = letra + invertida
    return invertida

print(invertir_cadena("hola que tal"))

"""

#Escribe una función que determine si un número es primo.
"""
def primo(numero):
    if numero - 2:
        return False
    for i in range(2,int(numero ** 0.5)+1):
        if numero % i == 0:
            return False
    return True

print(primo(8))
"""


#escriba una funcion que devuelva los primeros n numeros de la serie de fibonaci
# 0,1,1,2,3,5,8,13,21,34
"""
def fibonaci(n):
    serie = [0,1]
    for _ in range(n - 2):
        serie.append(serie[-1]+serie[-2])
    return serie[:n]

print(fibonaci(1000))
"""

#Escriba una funcion que determine si la palabra es un palidromo
# anita lava la tina // neuquen
"""
def palidromo(palabra):
    palabra = palabra.lower().replace(" ","")
    return palabra == palabra[::-1]
print(palidromo("neuquen"))
"""

#escriba una funcion que sume los digitos de un numero entero
"""
def suma_digitos(n):
    return sum(int(digito) for digito in str (abs(n)))

print(suma_digitos(1234))

"""

#Escribir una funcion que elimine los elemntos duplicados de una lista
"""
def eliminar_duplicados(lista):
    return list(set(lista))

print(eliminar_duplicados([1,2,2,3,4.5,6,4.5,9]))
"""

#crear una funcion contar_palabras(texto) que devuelva un diccionario con la cantidad de veces que aparece cada palabra 
"""
def contar_palabra(texto):
    palabras = texto.lower().split()
    conteo = {}
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra,0)+1
    return conteo 

print(contar_palabra("hola mundo hola python hola"))

"""


#Enunciado: Escribe una función doble(numero) que reciba un número entero o decimal y devuelva su doble. Prueba la función con diferentes números.
"""
def doble(numero):
    return numero * 2

print(doble(2))

"""
#Escribe una función area_rectangulo(base, altura) que reciba la base y la altura de un rectángulo y devuelva su área. Prueba con diferentes valores.
"""
def area_rectangulo(base,altura):
    return base * altura

print(area_rectangulo(10,100))
"""
#Escribe una función es_positivo(numero) que reciba un número y devuelva True si es mayor que 0, o False en caso contrario. Prueba con diferentes números.
"""
def es_positivo(numero):
    if numero > 0:
        return True
    else:
        return False
    
print(es_positivo(2))
print(es_positivo(-22))
"""
#Escribe una función mayor(a, b) que reciba dos números y devuelva el mayor de ellos. Si son iguales, devuelve cualquiera. Prueba con diferentes pares de números.
"""
def mayor(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:  # Si a == b
        return a  # o return b, ya que son iguales
print(mayor(4, 2))  
print(mayor(2, 2)) 
print(mayor(2, 4))  
"""
"""
def mayor(a, b):
    return max(a, b)
print(mayor(4, 2))  # Imprime 4
print(mayor(2, 2))  # Imprime 2
print(mayor(2, 4))
"""

#Escribe una función contar_caracteres(texto) que reciba una cadena de texto y devuelva la cantidad de caracteres (incluyendo espacios). Prueba con diferentes frases.
"""
def contar_caracteres(texto):
    return len(texto)

print(contar_caracteres("hola como estas     "))
"""

#Escribe una función suma_hasta_n(n) que reciba un número entero positivo n y devuelva la suma de todos los números desde 1 hasta n. 
# Prueba con diferentes valores de n.
"""
def suma_hasta_n(n):
    suma = 0
    for i in range(1,n+1):
        suma += i
    return suma

print(suma_hasta_n(9))
"""
#Escribe una función es_par(numero) que reciba un número entero y devuelva True si es par, o False si es impar. Prueba con diferentes números.
"""
def es_par(numero):
    if numero % 2 == 0:
        return True
    return False
print(es_par(2))
print(es_par(3))
"""

#Escribe una función promedio(lista) que reciba una lista de números y devuelva su promedio. Si la lista está vacía, devuelve 0. Prueba con diferentes listas.
"""
def promedio(lista):
    if len(lista) == 0:
        return 0
    suma = sum(lista)
    promedio = suma / len(lista)
    return promedio

print(promedio([1, 2, 3, 4]))  # Debería imprimir 2.5
print(promedio([]))           # Debería imprimir 0
print(promedio([10]))         # Debería imprimir 10
print(promedio([5, 5, 5]))    # Debería imprimir 5.0    
"""
"""
#Escribe una función contar_vocales(texto) que reciba una cadena de texto y devuelva el número de vocales (a, e, i, o, u) que contiene. 
# Considera también vocales en mayúsculas. Prueba con diferentes frases.

def contar_vocales(texto):
    vocales = "aeiouAEIOU"  # Incluimos mayúsculas
    contador = 0  # Inicializamos el contador

    for letra in texto:  # Recorremos cada letra de la cadena
        if letra in vocales:  # Si la letra es una vocal
            contador += 1  # Incrementamos el contador

    return contador  # Devolvemos el total de vocales

# Pruebas
print(contar_vocales("Hola Mundo"))  # Salida esperada: 4
print(contar_vocales("PYTHON"))  # Salida esperada: 0
print(contar_vocales("El sol brilla en el cielo"))  # Salida esperada: 10

"""

#Escribe una función que reciba un número y devuelva una lista con sus múltiplos hasta 100.
"""
def lista_multiplos(numero):
    for i in range(1, 11):
        print(numero * i) 

lista_multiplos(10)
"""

#Crea una función llamada contar_vocales(palabra) que reciba una palabra como argumento y devuelva cuántas vocales tiene (a, e, i, o, u).
"""
def contar_vocales(palabra):
    vocales = "aeiou"
    contador = 0
    for i in palabra:
        if i in vocales:
            contador += 1
    return contador
    
print(contar_vocales("hola como estas ?"))
"""
#verificar con una funcion si una persona puede entrar a un sitio segun su edad
#si es mayor a 21 puede entrar 
#si tiene entre 18 y 21 con supervisacion de un mayor 
#si tiene menor de 18 no puede entrar porque es menor 
"""
def verficacion_acceso(edad):
    if edad >= 21:
        return "Puedes ingresar" 
    elif edad >= 18 or edad <= 21:
        return "Puedes ingresar con un mayor"
    elif edad < 18:
        return "No puedes ingresar"
    else:
        return "Número erroneo"
    
edad_usuario = int(input("Ingrese su edad:  "))

resultado = verficacion_acceso(edad_usuario)
print(resultado)

"""

#usar una funcion para clasificar un nombre, como corto, mediano, largo 
# si tiene menos de 4 letras o tiene 4 letras es corto, 
#si es menor o igual a 7 es medio 
#si no es largo 
"""
def clasificacion(nombre):
    longitud = len(nombre)
    if longitud <= 4 or longitud == 4:
        return "Tu nombre es corto"
    if longitud <= 7:
        return "Tu edad es media"
    else:
        return "tu nombre es largo"
    
nombre_tamaño = input("Ingrese cual es tu nombre:  ")
revision = clasificacion(nombre_tamaño)
print(revision)

"""

#Cree un codigo que verifique si el mensaje enviado en un stream contiene cinco palabras a eleccion prohibidas 
"""
def verificacion(mensaje):
    palabras_prohibidas = ["javi","javier","presi","liberal","lali"]
    for palabra in palabras_prohibidas:
        if palabra in mensaje:
            return "Es una palabra prohibidad"
    return "Segui así k-p😎"


chat = input("Ingrese su mensaje: ")
resultado = verificacion(chat)
print(resultado)
"""

#hacer un programa que funcione como identificador del clima 
#soleado un buen día para ir a pasear 
#lluvioso no olvides llevar paraguas 
#nublado podria llover más tarde cuidado 
#nevado abrigate que hace frio 
#no reconozco ese tipo de clima 
"""
def identificador_clima(clima):
    clima = clima.lower()
    if clima == "soleado":
        return "Un buen día para ir a pasear"
    elif clima == "lluvioso":
        return "No olivdes llevar paraguas"
    elif clima == "nublado":
        return "Podria llover más tarde, cuidado"
    elif clima == "nevado":
        return "Abrigate que hace frio"
    else:
        return "No reconozco este tipo de clima"
    
estado_clima = input("Cómo está el clima hoy?")
restulado = identificador_clima(estado_clima)
print(restulado)
"""

#Hacer un programa que verifique la disponibilidad de un usuario ingresando 5 nombres 
"""
def verificacion_usuario(usuario):
    usuarios_disponibles = ["Juan","Martin","Sol","Ana","Cala"]
    if usuario.lower() in usuarios_disponibles:
        return "No se encuentran disponibles, lo siento"
    else:
        return "Se encuentra disponible"
    
consulta_usuario = input("Ingrese la persona que quiere hablar: ")
resultado = verificacion_usuario(consulta_usuario)
print(resultado)
"""

#realizar un detector de saludos que detecte si se realizaron uno de los 5 saludos predefinidos
"""
def detector_saludos(frase):
    saludos_aprobados = ["hola","hi","hallo","check","man"]
    for saludo in saludos_aprobados:
        if saludo in frase.lower():
            return "Se hizo uno de los saludos"
    return "No se realizó un saludo"

mayonesa = input("Ingrese una frase:  ")
resultado = detector_saludos(mayonesa)
print(resultado)
"""

#Crear un menu interactivo de opciones con 3 botones 
#el 1 va a decir "hola que tengas un gran día"
#el 2 va a decir "sigue adelante lo estás haciendo bien"
# el 3 va a decir "saliendo del programa"

"""
def menu_interactivo():
    print("\n - - - MENU - - - ")
    print("1 - SALUDAR")
    print("2 - FRASE")
    print("3 - SALIR")

def evaluar_menu(opcion):
    if opcion == "1":
        return "Hola, que tengas un gran día"
    elif opcion == "2":
        return "Sigue adelante lo estás haciendo bien"
    elif opcion == "3":
        return "Saliendo del programa"
    else:
        return "Opción no valida"
    
opcion = ""
while opcion != "3": 
    menu_interactivo()
    opcion = input("Elige una opción: ")
    evaluar_menu(opcion)
"""
"""

def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Saludar")
    print("2. Mostrar una frase motivadora")
    print("3. Salir")

def ejecutar_opcion(opcion):
    if opcion == "1":
        print("¡Hola! Espero que tengas un buen día.")
    elif opcion == "2":
        print("¡Sigue adelante, lo estás haciendo bien!")
    elif opcion == "3":
        print("Saliendo del programa...")
    else:
        print("Opción no válida.")

# Bucle principal
opcion = ""
while opcion != "3":
    mostrar_menu()
    opcion = input("Elige una opción: ")
    ejecutar_opcion(opcion)
""" 
#Realizar un programa que haga una verificacion de contraseña sabiendo que la contraseña es secreto123
""" 
def verificacion(contraseña):
    contraseña_real = "secreto123"
    while contraseña.lower() != contraseña_real.lower():
        return "No es la contraseña correcta"

opcion = input("ingrese una contraseña: ")
resultado = verificacion(opcion)
print(resultado)
""" 
"""
def verficar_contraseña():
    contraseña_correcta = "secreto123"
    intento = ""
    while intento != contraseña_correcta:
        intento = input("Introduzca la contraseña: ")
        if intento != contraseña_correcta:
            print("Contraseña incorrecta, intente otra vez")
    print("contraseña correcta, bienvendio")

verficar_contraseña()
"""

#hacer un programa que verifique si un nombre es valido 
#para que el nombre sea valido tiene que tiene que tener menor o igual que 3 letras 
"""
def es_nombre_valido(nombre):
    if len(nombre) <= 3:
        return False
    if " " in nombre:
        return False
    return True

def pedir_nombre():
    nombre = ""
    while True:
        nombre = input("Escribe nombre de usuario mínimo 3 letras sin espacios: ")
        if es_nombre_valido(nombre):
            print("Nombre valido", nombre)
            break
        else:
            print("nombre invalido, intente de nuevo")

pedir_nombre()

"""

#Escribir un programa que valide un inicio de sessión donde el usuario sera admin y la contraseña sera clave1234 tendra como intentos maximos 3
"""
def inicio_de_session():
    usuario_correcto = "admin"
    contraseña_correcta = "clave1234"
    intentos = 3
    while intentos > 0:
        usuario = input("ingrese usaurio: ")
        contraseña = input("ingrese contraseña: ")
        if usuario == usuario_correcto and contraseña == contraseña_correcta:
            print("Inicio de session exitoso, bienvendio")
            return
        else:
            intentos = intentos - 1
            print(f"Datos incorrectos. Te quedan {intentos} intentos")
    print("Has agotado los intentos, acceso bloqueado")

inicio_de_session() 
"""

#Contar cuántas vocales tiene una palabra 
"""
def contar(palabra):
    vocales = "aeiouAEIOU"
    contador = 0
    i = 0
    while i < len(palabra):
        if palabra [i] in vocales:
            contador += 1
        i += 1
    return contador


texto = input("Ingrese una palabra: ")
resultado = contar(texto)
print(resultado)
"""

#Haz una función que lea números del usuario hasta que escriba 0, y devuelva la suma total.
"""
def suma_numeros():
    suma_total = 0
    numeros = int(input("Ingrese un numeor que quiera sumar. El programa termina cuando ingrese 0:  "))
    while numeros != 0:
        suma_total += numeros
        numeros = int(input("Ingrese un numeor que quiera sumar. El programa termina cuando ingrese 0:  "))
    return suma_total


resultado = suma_numeros()
print(resultado)
"""        
    
#Crea una función donde el usuario intente adivinar un número secreto entre 1 y 10. Usa while para repetir hasta que lo adivine.
"""
import random 

def adivinar_numero():
    secreto = random.randint(1,10)
    numero = int(input("Ingrese un número entre el 1 y 10: "))
    while numero != secreto:
        numero = int(input("Ingrese un número entre el 1 y 10: "))
    return numero

resultado = adivinar_numero()
print("El número es: ", resultado)
"""

#Haz una función que pida una contraseña al usuario hasta que escriba la correcta. Usa while.

"""
def validar_contraseña():
    password = "pass"
    solicitud = input("Ingrese un contraseña: ")
    while solicitud != password:
        solicitud = input("Ingrese un contraseña: ")
    return solicitud

resultado = validar_contraseña()
print("La contraseña es: ", resultado)
"""

#Escribe una función que reciba un número y muestre una cuenta regresiva hasta 0.
"""
def cuenta_regresiva(n):
    while n >= 0:
        print(n)
        n -= 1
    print("despegue")

pedir_nro = int(input("Ingrese un número random : "))

cuenta_regresiva(pedir_nro)
"""

#Haz una función que repita un saludo hasta que el usuario escriba "salir".
"""
def repetir_saludo():
    saludo = input("Ingrese un saludo:  . Si desea salir ingrese salir. ")
    while saludo != "salir":
        saludo = input("Ingrese un saludo:  . Si desea salir ingrese salir. ")
    return saludo

resultado = repetir_saludo()
print(resultado)
"""

#Haz una función que invierta una palabra ingresada por el usuario usando while.
"""
def palabra_invertida(palabra):
    i = len(palabra) - 1 
    invertida = ""
    while i >= 0:
        invertida += palabra[i]
        i -= 1 
    return invertida

ingrese_palabra = input("Ingrese una palabra: ")
resultado = palabra_invertida(ingrese_palabra)
print(resultado)

"""

#Haz una función que sume números positivos que el usuario ingresa hasta que ponga un número negativo.
"""
def suma_positivos():
    total = 0 
    solicitud_positivos = int(input("Ingrese números positivos. Si desea terminar ingrese un número negativo. "))
    while solicitud_positivos > 0:
        total += solicitud_positivos
        solicitud_positivos = int(input("Ingrese números positivos. Si desea terminar ingrese un número negativo. "))
    return total

resultado = suma_positivos()
print("La suma total de los números es: ", resultado)
"""


#Escribe una función que reciba una palabra y una letra, y devuelva cuántas veces aparece esa letra.
"""
def contador_palabra(palabra,letra):
    i = 0
    contador = 0
    while i < len(palabra):
        if palabra [i] == letra:
            contador += 1
        i += 1
    return contador

palabra = input("Ingrese una palabra: ")
letra = input("Ingrese un letra: ")

resultado = contador_palabra(palabra,letra)
print(resultado)

"""
#Haz una función que pida una contraseña al usuario. Solo tiene 3 intentos para acertarla.
"""
def solicitud_contraseña():
    password = "password"
    contador = 3
    while contador  > 0:
        solicitud = input("Ingrese la contraseña: ")
        if solicitud == password:
            print("La contraseña es correcta.")
            return
        else:
            contador -= 1
            print("Te quedan: ", contador, "intentos")
    print("demasiados intentos, acceso denegado")

print(solicitud_contraseña)
"""

#Crea una función que reciba un número entero y muestre sus dígitos en orden inverso.
"""
def invertir_digitos(numero):
    numero = abs(numero)
    while numero > 0: 
        print(numero % 10)
        numero //= 10

n = int(input("Escriba un número: "))
print("Digitos en orden inverso")
invertir_digitos(n)
"""



