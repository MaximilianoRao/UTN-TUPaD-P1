import random
#Maximiliano Rao
#Ejercicio 1
#Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.


for i in range(101):  
    print(i)


#Ejercicio 2
# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

numero = int(input("Ingresa un número entero: "))
# Alternativa usando bucles
contador = 0
absoluto = abs(numero)

while absoluto > 0:
    absoluto //= 10
    contador += 1

# Si el número es 0, tiene 1 dígito
if numero == 0:
    contador = 1

print(f"El número {numero} tiene {contador} dígitos.")



#Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

valor1 = int(input("Ingresa el primer valor entero: "))
valor2 = int(input("Ingresa el segundo valor entero: "))

valor1 += 1

suma = 0
for numero in range(valor1, valor2):
    suma += numero

print(f"La suma de los números entre {valor1-1} y {valor2}, excluyéndolos, es: {suma}")

#Ejercicio 4
#Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

total = 0


while True:
    numero = int(input("Ingresa un número entero. Ingresa 0 para finalizar: "))
    if numero == 0:
        break
    total += numero

print(f"El total acumulado es: {total}")

#Ejercicio 5
#Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.


numero_secreto = random.randint(0, 9)

print("Adivina el número entre 0 y 9")

intentos = 0 
adivinado = False


while not adivinado:
    intento = int(input("Ingresa el número: "))
    intentos += 1 
    if intento == numero_secreto:
        print("¡Felicidades! Adivinaste el número.")
        adivinado = True
    else:
        print("Número incorrecto. ¡Inténtalo de nuevo!") 
   
# Mostrar cuántos intentos fueron necesarios
print(f"Lo adivinaste en {intentos} intentos.")

#Ejercicio 6
#Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

print("Números pares entre 0 y 100:")
for numero in range(100, -1, -2):
    print(numero)


#Ejercicio 7
#Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.


numero = int(input("Ingresa un número entero positivo: "))
if numero >= 0:
    suma = 0
    for i in range(numero + 1):
        suma += i
    print(f"La suma de los números entre 0 y {numero} es: {suma}")
else:
    print("Error. No ingreso un número positivo.")


#Ejercicio 8
#Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).




pares = 0
impares = 0
positivos = 0
negativos = 0

print(f"Ingresa 100 números enteros:")
for i in range(100):
    numero = int(input(f"Ingresa el número {i + 1}: "))

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1


print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")



#Ejercicio 9
#Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores.


suma = 0
print(f"Ingresa 100 números enteros:")
for i in range(100):
    numero = int(input(f"Ingresa el número {i + 1}: "))
    suma += numero 

media = suma / 100
print(f"\nLa media de los números ingresados es: {media}")

#Ejercicio 10
#Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario.

numero = int(input("Ingresa un número: "))
numero_absoluto = abs(numero)
numero_invertido = 0

while numero_absoluto > 0:
    digito = numero_absoluto % 10
    numero_invertido = numero_invertido * 10 + digito 
    numero_absoluto //= 10 


if numero < 0:
    numero_invertido = -numero_invertido

# Mostrar el número invertido
print(f"El número invertido es: {numero_invertido}")