#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.


"""

while True:
    eco= input("Escribir aca: ")
    if eco == "Salir":
        break
    print(eco)


"""
"""
eco = ""
while eco != "salir":
    eco= input("Escribir aca: ")
    print(eco)
"""


#Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.


"""
numero = 0

teclado = int(input("ingrese un numero: "))

while teclado != 0: 
    numero += teclado
    teclado = int(input("ingrese un numero: "))
    print(numero)
"""

"""
total=0
nro=int(input("Número: "))
while nro != 0:
    total+=nro
    nro=int(input("Número: "))
    print (total)

"""

#Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números positivos ingresados.
"""
positivos = 0
nro = int(input("Ingrese un número entero: "))

while nro != 0:
    if nro > 0:
        positivos += nro
    nro = int(input("Ingrese un número entero: "))
print("La cantidad de positivos es: ", positivos)
"""

#Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.
"""

mayor = -1 

nro = int(input("Ingrese numeros enteros: ")) # primera vuelta ingrese 1 // segunda vuelta 2

while nro != 0:    # 1 es distinto que 0 // 2 es disitnto que 0? 
    if nro > mayor: # 1 es mayor que -1 ? // 2 es mayor que 1? 
        mayor = nro # mayor pasa a valer 1 // mayor pasa a valer 2 
    nro = int(input("Ingrese numeros enteros: "))
print(mayor)

"""
"""
# Inicializar la lista vacía
lista_compras = []

# Pedir al usuario que ingrese 5 productos
for i in range(5):
    producto = input(f"Ingrese el producto {i+1}: ")
    lista_compras.append(producto)

# Mostrar la lista completa
print("\nLista de compras:")
for producto in lista_compras:
    print(f"- {producto}")
"""

#Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.
"""
suma = 0
nro = int(input("Ingrese un numero entero: "))

while nro != 0:
    digito = nro % 10
    suma += digito
    nro = nro // 10
    print("La suma de los digitos seria ", suma)
"""
#Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. 
# La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.

"""
pares = 0
nro = int(input("Ingrese un numero entero: . Si desea terminar ingrese -1:   "))

while nro != -1:
    if nro % 2 == 0:
        pares +=1 
    suma = 0 
    while nro != 0:
        digito = nro % 10
        suma += digito
        nro =  nro // 10 
    print("La suma de digitos es: ", suma)
    nro = int(input("Ingrese un numero entero: . Si desea terminar ingrese -1:   "))
print("Se ingresaron ", pares, "numeros pares")
"""
"""

pares=0
n=int(input("Número (-1 para terminar el programa): "))
while n!=-1:
    if n%2 == 0:
        pares+=1
    suma=0
    while n!=0:
        digito=n%10
        suma+=digito
        n=n//10
    print("Suma de sus dígitos:", suma)
    n=int(input("Número (-1 para terminar el programa): "))
print("Se ingresaron", pares, "números pares")

"""

#Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. 
# A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error. 
# El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. 
# Si elige las opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.
"""
while True: 
    print("Opcion 1 - - Comenzar programa: ")
    print("Opcion 2 - - Imprimir listado: ")
    print("Opcion 3 - - Finalizar programa: ")
    opcion = int(input("Ingrese la opcion elegida: "))
    if opcion == 1:
        print("Comenzamos")
    elif opcion == 2:
        print("Listado")
        print("Nadia, Juan, Matias")
    elif opcion == 3: 
        print("Hasta la proxima")
        break
    else:
        print("Opcion incorrecta, debe ingresar 1, 2 o 3 ")
"""
"""
#Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). 
# Recorrer la frase, carácter a carácter, comparando con la letra buscada. 
# Si el carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. 
# Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.

frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra a buscar: ")
i = 0

while i != len(frase):
    if letra != frase[i]:
        print("No se encontro la posición ", i)
        i += 1
        continue
    print("Se encontro en la posición ", i )
    break

"""

#Crear un programa que permita al usuario ingresar los montos de las compras de un cliente 
# (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), 

# cortando el ingreso de datos cuando el usuario ingrese el monto 0.

# Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. 

# Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.

"""
total = 0
montos = int(input("Ingrese los montos a cargar: "))
while montos != 0:
    if montos < 0:
        print("Monto no valido")
    else:
        total += montos
    montos = int(input("Ingrese los montos a cargar: "))

if total > 1000:
    total -= total * 0.1
print("Monto total a pagar es: ", total)

"""

#Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero. 
# Imprimir la cantidad de números primos ingresados.
"""
primos = 0 
nro = int(input("Ingrese un número: "))

while nro != 0:
    primos += nro
    nro = int(input("Ingrese un número: "))
    if nro / nro or nro / 1:
        print("La cantidad de numeros primos son: ", primos )

"""
"""

cantidad = 0 
n = int(input("Ingrese un numero: "))
while n != 0:
    primo = True
    for i in range(2,n):
        if n % i == 0:
            primo = False 
            break
    if primo:
        cantidad += 1
    n = int(input("Ingrese un numero: "))
print("La cantidad de numeros primos es: ", cantidad)
"""

#Solicitar al usuario que ingrese una frase y 
# luego informar cuál fue la palabra más larga (en caso de haber más de una, mostrar la primera) y cuántas palabras había.
#  Precondición: se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más.

"""
frase= input("Ingrese una frase y para salir marque 0:  ")

while frase != 0:
    if frase > 1:
        palabras = len(frase)
        print("La primera frase es: ", frase)
    while frase > 1:
        len(frase, end= "")

"""
"""
frase = input("Ingrese una frase: ").strip()
cantidad = 0 
len_p_mas_larga = 0

while len(frase) != 0:
    cantidad = cantidad +1
    i = frase.find(" ")
    if i != -1:
        palabra = frase[0:i]
        while i < len(frase) and frase[i] == " ":
            i = i+1 
        frase = frase[i:]
    else:
        palabra= frase
        frase= ""
    if len(palabra) > len_p_mas_larga:
        len_p_mas_larga = len(palabra)
        p_mas_larga = palabra
if cantidad > 0: 
    print("La palabra mas larga es : ", p_mas_larga)
print("La cantidad de palabras es: ", cantidad)
"""
