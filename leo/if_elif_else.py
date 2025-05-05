
# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
# El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N.
# El grupo B está formado por el resto.

nombre = input("Ingrese su nombre: ")
sexo = input("Tu sexo es Masculino o Femenino? ").lower()

# Convertimos la primera letra del nombre a mayúscula para hacer una comparación uniforme
primera_letra = nombre[0].upper()

if sexo == "femenino" and primera_letra < "M" or sexo == "masculino" and primera_letra > "N":
    print("Tu grupo es el A")
else:
    print("Tu grupo es el B")

"""
"""

#### LEO ####
name= input("Nombre: ")
gender= input ("Sexo: (M o H) ")

if gender == "M":
    if name.lower() < "m":
        group= "A"
    else:
        group= "B"

else:
    if name.lower() >"n":
        group= "A"
    else:
        group= "B"

print ("Tu grupo es", group)

"""


# #Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
# Renta	Tipo impositivo
# Menos de 10000€	5%
# Entre 10000€ y 20000€	15%
# Entre 20000€ y 35000€	20%
# Entre 35000€ y 60000€	30%
# Más de 60000€	45%
# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

"""
renta = float(input("Ingrese cual su renta anual? "))

if renta < 10000:
    tipo = 5
elif renta < 20000:
    tipo = 15
elif renta < 35000:
    tipo = 30
elif renta < 60000:
    tipo = 45

print("Tiene que pagar el " , tipo , "%")

# """
# En una determinada empresa, sus empleados son evaluados al final de cada año. 
# Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios.
# Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. 
# A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. 
# La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.
# Nivel	Puntuación
# Inaceptable	0.0
# Aceptable	0.4
# Meritorio	0.6 o más
# Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.
"""
print("NIVEL DE LOS EMPLEADOS")
bonificacion = 2400
inaceptable	= 0.0
aceptable	= 0.4
meritorio	= 0.6

puntos = float(input("Ingrese el valor del resultado final: "))

if puntos == inaceptable:
    nivel = "inaceptable"
elif puntos == aceptable:
    nivel = "aceptable"
elif puntos >= 0.6: 
    nivel = "meritorio"
else: 
    nivel = ""

if nivel == "":
    print("puntuacion no valida")
else:
    print("Tu rendimiento es ", nivel )
    print("Te corresponde cobrar " , bonificacion * puntos)

"""

#Escribir un programa para una empresa que tiene salas de juegos para todas las edades y 
# quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. 
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. 
# Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

"""
edad = float(input("Ingrese su edad: "))


if edad < 4:
    print("Entras gratis")
elif edad >= 4 and edad <= 18:
    print("debes pagar 5 euros")
elif edad > 18: 
    print("Tenes que pagar 10 euros")
else:
    print("Edad erronea")


"""
# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, 
# y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
# Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
"""

print("Pizzeria Bella Napoli. \nTipos de pizza\n\t1- Vegetariana\n\t2- No Vegetariana\n")

tipo = input("Ingrese el tipo de pizza que usted quiera: ")

if tipo == "1":
    print("Ingrediente de pizza Vegetariana\n\t1-Pimiento\n\t2-Tofu\n")
    ingrediente = input("Indique el ingrediente que desea ")
    print("Pizza Vegetariana con Tomate, Mozzarella y ", end= "")
    if ingrediente == "1":
        print("pimiento")
    else:
        print("tofu")
else:
    print("Ingredientes de pizza No Vegetariana\n\t1-Peperoni\n\t2-Jamon\n\t3-Salom")
    ingrediente = input("Indique el ingrediente que desea ")
    print("Pizza no vegetariana con Mozzarella, tomate " , end= "")
    if ingrediente == "1":
        print("peperoni")
    elif ingrediente == "2":
        print("Jamon")
    else:
        print("Salmon")


"""

#Solicitar al usuario un número de cliente. Si el número es el 1000, imprimir "Ganaste un premio".

# numero = int(input("Ingrese el numero de cliente: "))

# if numero == 1000:
#     print("ganas el premio")
# else:
#     print("Segui participando")

#####

#Solicitar al usuario que ingrese dos números y mostrar cuál de los dos es menor. No considerar el caso en que ambos números son iguales.
"""
numero1 = int(input("ingresa el 1er numero: "))
numero2 = int(input("ingresa el 2do numero: "))

if numero1 < numero2:
    print("El" , numero1 , "es el menor")
else:
    print("el" , numero2 , "es el mayor")


"""
#Solicitar al usuario que ingrese dos números y mostrar cuál de los dos es menor. Considerar el caso en que ambos números son iguales.
"""
numero1 = int(input("ingresa el 1er numero: "))
numero2 = int(input("ingresa el 2do numero: "))

if numero1 <  numero2:
    print("el" , numero1, "es el mayor")
elif numero1 == numero2:
    print("los numeros son iguales")
else:
    print("el", numero2, "es el menor")

"""

#Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, 
# otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. 
# Si el día ingresado no es ninguno de esos, imprimir otro mensaje.
"""
dia = input("ingrese un dia")

if dia == "lunes":
    print("hoy es lunes")
elif dia == "viernes":
    print("hoy es viernes")
elif dia == "sabado " or dia == "domingo":
    print("es fin de semana")
else:
    print("no es Osvaldo")

"""

#Solicitar al usuario que ingrese los nombres de dos personas, los cuales se almacenarán en dos variables. 
# A continuación, imprimir “coincidencia” si los nombres de ambas personas comienzan con la misma letra ó si terminan con la misma letra. 
# Si no es así, imprimir “no hay coincidencia”.
"""

persona1 = input("ingrese el nombre de la primera persona: ")
persona2 = input("ingrese el nombre de la segunda persona: ")

if persona1[0].upper == persona2[0].upper or persona1[-1].upper == persona2[-1].upper:
    print("Hay coincidencia")
else:
    print("no hay coincidencia")
"""

#Crear un programa que permita al usuario elegir un candidato por el cual votar. 
# Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verde, candidato C por el partido azul. 
# Según el candidato elegido (A, B ó C) se le debe imprimir el mensaje “Usted ha votado por el partido [color que corresponda al candidato elegido]”. 
# Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar “Opción errónea”.
"""
candidato_rojo = "a"
candidato_verde = "b"
candidato_azul = "c"

candidato = input("ingrese la letra del candidado, sea A , B o C: ")

if candidato == "A":
    print("Usted eligio al candidado Rojo")
elif candidato == "B":
    print("Usted eligio al candidado Verde")
elif candidato == "C":
    print("Usted eligio al candidado Azul")
else:
    print("Es una opcion erronea")
"""

"""
candidato = input("ingrese la letra del candidado, sea A , B o C: ")

if candidato.upper() == "A":
    print("Usted ah votado")

"""

#Escribir un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “es vocal”.
#Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter, informarle que no se puede procesar el dato.
"""

letra= input("ingrese una letra: ")

if len(letra) != 1: 
    print("No se puede procesar el dato")
else:
    if letra in "aeiou":
        print("Si, es una vocal")
"""

#Hacer un programa que permita saber si un año es bisiesto. 
# Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.
"""
anio = int(input("Ingrese el año: "))

if anio % 4 == 0:
    if anio % 100 != 0 or anio % 400 == 0:
        print("Es año bisiestro")
    else:
        print("no es bisiestro")
else:
    print("no es bisiestro")

"""



# Un instituto de enseñanza de inglés necesita un programa que le permita, cada día, procesar observaciones sobre las clases de ese día. 
# El instituto dicta clases a estudiantes de distintos niveles y 
# cada nivel tiene clases en un día de la semana diferente: los lunes se dicta el nivel inicial,
#  los martes el nivel intermedio, los miércoles el nivel avanzado, los jueves son para práctica hablada 
# y los viernes se dicta inglés para viajeros.

# Se debe comenzar por solicitar al usuario que ingrese la fecha actual en formato "día, DD/MM", donde [día] es un día de la semana,

#  DD es el número de día y MM es el número de mes.
# 
#  Si el usuario ingresa un día de la semana inexistente o una fecha cuyo día supere el número 31
#  o el mes supere el número 12, finalizar el programa indicando que se produjo un error. 

# Debe permitirse que ingrese el día de la semana en minúsculas o mayúsculas indistintamente. 
# Como precondición se tiene que lo ingresado por el usuario tendrá la forma <[alfanumérico], [numérico]/[numérico]>.

# Una vez indicada la fecha, el usuario necesita poder indicar si ese día se tomaron exámenes, pero eso sólo si se trata de los niveles inicial,
#  intermedio o avanzado, ya que las prácticas habladas y el inglés para viajeros no tienen exámenes. 
# Si hubo exámenes, el usuario ingresará cuántos alumnos aprobaron y cuántos no, y el programa le mostrará el porcentaje de aprobados.

# Si el día fue el correspondiente a práctica hablada, el usuario deberá ingresar el porcentaje de asistencia a clase 
# y el programa le indicará "asistió la mayoría" en caso de que la asistencia sea mayor al 50% o "no asistió la mayoría" si no es así. 

# Si se trata del inglés para viajeros y la fecha actual corresponde al día 1 del mes 1 o del mes 7, 
# se deberá imprimir "Comienzo de nuevo ciclo" y solicitar al usuario que ingrese la cantidad de alumnos del nuevo ciclo 

# y el arancel en $ por cada alumno, para luego imprimir el ingreso total en $.

# Listas de días y meses válidos
dia_semana = ["lunes", "martes", "miércoles", "jueves", "viernes"]
meses = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
dias_del_mes = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]

# Solicitar la fecha
fecha = input("Fecha (formato 'día, DD/MM'): ")

""""""

fecha=input("Fecha (formato 'día, DD/MM'): ")
fecha=fecha.lower()
diasemana=fecha[0:fecha.find(',')]
dianro=int(fecha[fecha.find(',')+2:fecha.find('/')])
mesnro=int(fecha[fecha.find('/')+1:])
if dianro>31 or mesnro>12:
    print("Fecha incorrecta")
else:
    if diasemana in "lunes,martes,miércoles":
        respuesta=input("¿Se tomaron exámenes? S/N: ")
        if respuesta.lower()=="s":
            aprobados=int(input("Cantidad de aprobados: "))
            reprobados=int(input("Cantidad de reprobados: "))
            print("Porcentaje de aprobados:", (aprobados*100)/(aprobados+reprobados), "%")
    elif diasemana=="jueves":
        asistencia=int(input("Porcentaje de asistencia: "))
        if asistencia>50:
            print("Asistió la mayoría")
        else:
            print("No asistió la mayoría")
    elif diasemana=="viernes":
        if dianro==1 and (mesnro==1 or mesnro==7):
            print("Nuevo ciclo")
            alumnos=int(input("Cantidad de alumnos: "))
            arancel=float(input("Arancel: $"))
            print("Ingreso total: $", alumnos*arancel)
    else:
        print("Fecha incorrecta")
print("Fin del programa")