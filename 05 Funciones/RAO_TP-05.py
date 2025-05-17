#Maximiliano Rao
#Práctico 2: Funciones en Python

import math
# Definición de funciones
#Ejercicio 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

#Ejercicio 2
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

#Ejercicio 3
def informacion_personal(nombre,apellido,edad, residencia):
   print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.") 

#Ejercicio 4
def calcular_area_circulo(radio):
    return round((math.pi * (radio**2)),2)

def calcular_perimetro_circulo(radio):
    return  round((math.pi * radio * 2),2)


#Ejercicio 5
def segundos_a_horas(segundos):
    print(f"Los segundos ingresados son {round(segundos/3600,5)} horas")


#Ejercicio 6
def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f"{numero} * {i} = {numero*i}")

#Ejercicio 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b   
    if (b != 0):
        division = a / b 
    else:
        "División por cero"
    return (suma, resta, multiplicacion, division)

#Ejercicio 8
def calcular_imc(peso, altura):
    return round(peso/(altura ** 2),2)


#Ejercicio 9
def celsius_a_fahrenheit(celsius):
    return ((celsius * (9/5))+32)

#Ejercicio 10
def calcular_promedio(a, b, c):
    return (round((a+b+c)/3,2))


# Programa principal

#Ejercicio 1
imprimir_hola_mundo()

#Ejercicio 2
print("-" * 30)
saludar_usuario(input("Ingrese su nombre: "))

#Ejercicio 3
print("-" * 30)
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su lugar de residencia: ")
informacion_personal(nombre,apellido,edad,residencia)

#Ejercicio 4
print("-" * 30)
radio = int(input("Ingrese el radio del círculo: "))
print(f"El área del círculo es: {calcular_area_circulo(radio)}")
print(f"El perímetro del círculo es: {calcular_perimetro_circulo(radio)}")

#Ejercicio 5
print("-" * 30)
print("El programa se encarga de convertir los segundos ingresados a horas")
segundos_a_horas(int(input("Ingresar los segundos:  ")))

#Ejercicio 6
print("-" * 30)
print("El programa imprime la tabla de multiplicar del número ingresado")
numero = int(input("Ingrese un número: "))
tabla_multiplicar(numero)


#Ejercicio 7
print("-" * 30)
#Ejemplos de ejecución
a = 10
b = 3
print(f"Este programa imprime el resultado de las 4 operaciones básicas entre {a} y {b}")
resultados = operaciones_basicas(a, b)

print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")


#Ejercicio 8
print("-" * 30)
print("Este programa devuelve el índice de masa corporal (IMC).")
peso = float(input("Ingrese el peso en kg: "))
altura = float(input("Ingrese la altura en metros: "))
print(f"El IMC es {calcular_imc(peso, altura)}")


#Ejercicio 9
print("-" * 30)
print("Este programa convierte grados Celsius a Fahrenheit")
temp = float(input("Ingrese la temperatura en °C: "))
print(f"La temperatura es {celsius_a_fahrenheit(temp)} °F")


#Ejercicio 10
print("-" * 30)
print("Este programa calcula el promedio de 3 números")
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))
print(f"El promedio es {calcular_promedio(a, b, c)}")
