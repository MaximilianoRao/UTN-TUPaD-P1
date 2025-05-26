#Maximiliano Rao
#Práctico 11: Aplicación de la Recursividad


#Ej1
def factorial (num):
    if num == 0:
        return 1
    else:
        #Multiplico el número actual por el factorial del número anterior.
        return num * factorial(num-1)

#Ej2
def fibonacci (num):
    #Devuelvo el mismo número en caso de que el número sea 0 ó 1.
    if num == 0 or num == 1:
        return num
    else:
        #Sumo el fibonacci de la posición anterior y la antepenultima
        return fibonacci(num-1) + fibonacci(num-2)

#Ej3
def potencia(base, exponente):
    if exponente == 0:
        return 1
    elif exponente > 0:
        #Se multiplica la base por la potencia de la base y exponente - 1.
        return base * potencia(base, exponente - 1)
    else:
        #Para casos de que el exponente sea negativo, se calcula 1 sobre el exponente en positivo.
        return 1 / potencia(base, -exponente)
    
#Ej4
def decimal_a_binario(num):
    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    else:
        #Llamo nuevamente a la función con la parte entera del resultado de dividir el número entre 2, esto se concatenará al string del resto de dividir al número entre 2.
        return (decimal_a_binario(num // 2) + str(num % 2))
        
#Ej5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    #Llamo nuevamente a la función con la palabra sin el primer y ultimo caracter.
    return es_palindromo(palabra[1:-1])


#Ej6
def suma_digitos(n):
    if n < 10:
        return n
    else:
        #Retorno la suma del ultimo digito y la llamada a la función del número sin ese ultimo digito.
        return (n % 10) + suma_digitos(n // 10) 


#Ej7
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        #Sumo la cantidad de bloques del piso con la llamada a la función con ese número menos 1.
        return n + contar_bloques (n - 1)

#Ej8
def contar_digito(numero, digito):
    if numero == 0:
        return 1 if digito == 0 else 0
    ultimo = numero % 10
    #En caso de que el digito coincida suma 1 y llama a la función con el número sin el último digito. De lo contrario solo llama a la función con el número sin el último digito sin sumar.
    if ultimo == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)



#Programa Principal

#Ej1
print("Ejercicio 1")
limite = int(input("Ingrese el número hasta donde debe calcularse el factorial: "))
for i in range(1,limite+1):
    print(factorial(i))

#Ej2
print("Ejercicio 2")
limite = int(input("Ingrese la posición hasta donde se debe calcular la serie Fibonacci: "))
for i in range(0,limite+1):
    print (f"Fibonacci en la posición {i}: {fibonacci(i)}")


#Ej3
# Pruebas
print("Ejercicio 3")
print(f"2^3 = {potencia(2, 3)}")  # 8
print(f"5^0 = {potencia(5, 0)}")  # 1
print(f"7^1 = {potencia(7, 1)}")  # 7
print(f"3^4 = {potencia(3, 4)}")  # 81


#Ej4
print("Ejercicio 4")
# Pruebas
print(f"0 en base decimal es {decimal_a_binario(0)} en binario")  
print(f"1 en base decimal es {decimal_a_binario(1)} en binario")  
print(f"2 en base decimal es {decimal_a_binario(2)} en binario")  
print(f"5 en base decimal es {decimal_a_binario(5)} en binario")  
print(f"10 en base decimal es {decimal_a_binario(10)} en binario")

#Ej5
print("Ejercicio 5")
# Pruebas
print("La palabra 'reconocer' es palindromo: ", es_palindromo("reconocer"))
print("La palabra 'neuquen' es palindromo: ", es_palindromo("neuquen"))  
print("La palabra 'python' es palindromo: ", es_palindromo("python"))   
print("La palabra 'a' es palindromo: ", es_palindromo("a"))        
print("La palabra '' es palindromo: ", es_palindromo(""))   


#Ej6
print("Ejercicio 6")
# Prueba
print(f"La suma de digitos del número 5 es: {suma_digitos(5)}")
print(f"La suma de digitos del número 123 es: {suma_digitos(123)}")
print(f"La suma de digitos del número 2024 es: {suma_digitos(2024)}")
print(f"La suma de digitos del número 987654 es: {suma_digitos(987654)}")


#Ej7
print("Ejercicio 7")
# Prueba
print(f"El total de bloques necesarios para una pirámide de 1 bloques es su base es: {contar_bloques(1)}")
print(f"El total de bloques necesarios para una pirámide de 2 bloques es su base es: {contar_bloques(2)}")
print(f"El total de bloques necesarios para una pirámide de 4 bloques es su base es: {contar_bloques(4)}")


#Ej8
print("Ejercicio 8")
# Prueba
print(f"La cantidad de veces que aparece 2 en el número 12233421 es: {contar_digito(12233421, 2)}")
print(f"La cantidad de veces que aparece 5 en el número 5555 es: {contar_digito(5555, 5)}")
print(f"La cantidad de veces que aparece 7 en el número 123456 es: {contar_digito(123456, 7)}")
print(f"La cantidad de veces que aparece 0 en el número 0 es: {contar_digito(0, 0)}")