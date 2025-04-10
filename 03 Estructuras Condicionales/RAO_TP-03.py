import random
from statistics import mode, median, mean

# Ejercicio 1
# Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

print("Ejercicio 1")
edad = int(input ("Ingrese su edad: " ))
#Compara si la edad ingresada es mayor a 18 años.
if edad > 18:
    print("Es mayor de edad")


# Ejercicio 2
# Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, 
# deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá 
# mostrar el mensaje “Desaprobado”.

print("Ejercicio 2")
nota = int(input("Ingrese su nota: "))
#Compara si la nota ingresada es mayor o igual que 6
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# Ejercicio 3
# Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, 
# imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por 
# pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) 
# en Python para evaluar si un número es par o impar.

print("Ejercicio 3")
num1 = int(input("Ingrese un número par: "))
#Calcula el resto de la division en 2, en caso que sea 0, el numero es par.
if (num1 % 2 == 0):
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")



# Ejercicio 4
# Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes 
# categorías pertenece: 
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años.

print("Ejercicio 4")
edad1 = int(input("Ingrese su edad: "))
print ("Pertenece a la categoría: ")
if (edad1 > 0 and edad1 < 12):
    print("Niño/a")
elif (edad1 >= 12 and edad1 < 18):
    print("Adolescente")
elif (edad1 >= 18 and edad1 < 30):
    print("Adulto/a joven")
#En caso de que no se cumpla ninguna de las demás condiciones significa
#que el usuario ingreso un número mayor a 30. Suponiendo que el usuario
#ingresa números enteros positivos.
else:
    print("Adulto/a mayor")


# Ejercicio 5
#Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). 
# Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje 
# "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese 
# una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para 
# evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

print("Ejercicio 5")
password = input("Ingrese una contraseña entre 8 y 14 caracteres: ")
#La funciónn len nos devuelve la cantidad de caracteres de la cadena
largo = len(password)
if (largo >= 8 and largo <= 15):
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")


# Ejercicio 6
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista numeros_aleatorios, 
# calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o 
# no hay sesgo. Imprimir el resultado por pantalla.

#Utilizando la libreria random importada en las primeras lineas del archivo
#generamos una lista de 50 números del 1 al 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

#Utilizamos mode, median y mean para calcular moda, mediana y media respectivamente, las funciones
#se encuentran en el paquete statistics importado al comienzo del archivo.

print("Ejercicio 6")
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

#Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda.
if (media > mediana and mediana > moda):
    print("Lo lista posee SESGO POSITIVO")
#Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda.
elif (media < mediana and mediana < moda):
    print("Lo lista posee SESGO NEGATIVO")
#Sin sesgo: cuando la media, la mediana y la moda son iguales.
elif (media == mediana and mediana == moda):
    print("Lo lista NO POSEE SESGO")



# Ejercicio 7
# Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir 
# un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string 
# tal cual lo ingresó el usuario e imprimirlo por pantalla.

print("Ejercicio 7")
frase = input("Ingrese una frase o palabra: ")
#Uso la función len para saber el tamaño de lo ingresado le resto 1 para obtener el ultimo carácter, dado que la posición empieza en 0.
ultimo_caracter = frase[len(frase)-1]
vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

# Con el fin de evitar la creación de un if con varios elif, creo una lista con las vocales tanto mayusculas como minusculas y la recorro
# con un for, en caso de que encuentre alguna coincidencia le agrega a la frase el signo de exclamanción al final, finalmente imprimo el
# resultado
for i in vocales:
    if (ultimo_caracter == i):
        frase = frase + "!"
print(frase)


# Ejercicio 8
#Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas.
#2. Si quiere su nombre en minúsculas.
#3. Si quiere su nombre con la primera letra mayúscula.

print("Ejercicio 8")
name = input("Ingrese su nombre: ")
opcion = int(input("Elija una opción: \n 1. Si quiere su nombre en mayúsculas. \n 2. Si quiere su nombre en minúsculas. \n 3. Si quiere su nombre con la primera letra mayúscula. \nIngrese el número de la opción elegida: "))

if (opcion == 1):
    #upper() es la funcion para pasar una cadena a mayúsculas
    print(name.upper())
elif (opcion == 2):
    #lower() es la funcion para pasar una cadena a minísculas
    print(name.lower())
elif (opcion == 3):
    #title() es la funcion para pasar una cadena a modo titulo, la primera letra en mayúscula.
    print(name.title())


# Ejercicio 9
#Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la 
# escala de Richter e imprima el resultado por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

print("Ejercicio 9")
magnitud = float(input("Ingrese la magnitud del terremoto: "))
print("La clasificación del terrremoto segun la escala de Richter es:")
if(magnitud < 3):
    print("Muy leve")
elif(magnitud >= 3 and magnitud < 4):
    print("Leve")
elif(magnitud >= 4 and magnitud < 5):
    print("Moderado")
elif(magnitud >= 5 and magnitud < 6):
    print("Fuerte")
elif(magnitud >= 6 and magnitud < 7):
    print("Muy Fuerte")
elif(magnitud >= 7):
    print("Extremo")


# Ejercicio 10
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. 
# El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

print("Ejercicio 10")
# Al final del input uso la función upper() para dejarlo en mayúscula sin importar como lo ingrese.
hemisferio = input("Ingrese el hemisferio en el que se encuentra \n N : para NORTE \n S : para SUR\n ").upper()
# Al final del input uso la función lower() para dejarlo en minúscula sin importar como lo ingrese.
mes = input("Ingrese el mes del año: ").lower()
dia = int(input("Ingrese el día: "))
print("La estación del año es:")
# La metodologia que utilice fue analizar los meses, luego el hemisferio, en la meses limites analizaba el día primero y luego el hemisferio.
if(mes == "enero"):
    if(hemisferio == "N"):
        print("Invierno")
    else:
        print("Verano")
elif(mes == "febrero"):
    if(hemisferio == "N"):
        print("Primavera")
    else:
        print("Otoño")
elif(mes == "marzo"):
    if(dia <= 20):
        if(hemisferio == "N"):
            print("Invierno")
        else:
            print("Verano")
    else:
        if(hemisferio == "N"):
            print("Primavera")
        else:
            print("Otoño")
elif(mes == "abril"):
    if(hemisferio == "N"):
        print("Primavera")
    else:
        print("Otoño")
elif(mes == "mayo"):
    if(hemisferio == "N"):
        print("Primavera")
    else:
        print("Otoño")
elif(mes == "junio"):
    if(dia <= 20):
        if(hemisferio == "N"):
            print("Primavera")
        else:
            print("Otoño")
    else:
        if(hemisferio == "N"):
            print("Verano")
        else:
            print("Invierno")
elif(mes == "julio"):
    if(hemisferio == "N"):
        print("Verano")
    else:
        print("Invierno")
elif(mes == "agosto"):
    if(hemisferio == "N"):
        print("Verano")
    else:
        print("Invierno")
elif(mes == "septiembre"):
    if(dia <= 20):
        if(hemisferio == "N"):
            print("Verano")
        else:
            print("Invierno")
    else:
        if(hemisferio == "N"):
            print("Otoño")
        else:
            print("Primavera")
elif(mes == "octubre"):
    if(hemisferio == "N"):
        print("Otoño")
    else:
        print("Primavera")
elif(mes == "noviembre"):
    if(hemisferio == "N"):
        print("Otoño")
    else:
        print("Primavera")
elif(mes == "diciembre"):
    if(dia <= 20):
        if(hemisferio == "N"):
            print("Otoño")
        else:
            print("Primavera")
    else:
        if(hemisferio == "N"):
            print("Invierno")
        else:
            print("Verano")
