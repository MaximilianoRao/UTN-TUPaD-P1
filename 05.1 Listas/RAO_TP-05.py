#Maximiliano Rao

#Ejercicio 1
#Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

multiplos_de_4 = list(range(4, 101, 4))
print(multiplos_de_4)

#Ejercicio 2
#Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo.

lista = [1, 2, 3, 4, 5]
penultimo = lista[-2]
print("El penúltimo elemento es:", penultimo)

#Ejercicio 3
#Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. 

#Se crea lista vacia
palabras = []
#Se agrega primer elemento
palabras.append("viaje")
#Se agrega segundo elemento
palabras.append("playa")
#Se agrega tercer elemento
palabras.append("arena")
print(f"Lista completa: {palabras}")


#Ejercicio 4
#Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente.
# Imprimir la lista resultante por pantalla.

animales = ["perro", "gato", "conejo", "pez"]
#Reemplazo el segundo elemento. "gato"
animales[1] = "iguana"
#Reemplazo el ultimo elemento. "pez"
animales[-1] = "loro" 
#Imprimo lista resultante.
print(f"Lista resultante: {animales}")

#Ejercicio 5
# Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)
# El programa lo que hace es buscar el máximo valor de la lista numeros con la función max() luego elimina ese valor de la
# lista con la función remove(), finalmente se imprime la lista resultante (sin el valor máximo)

#Ejercicio 6
#Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

#Creo la lista con numeros del 10 al 30 con salto de a 5.
numeros = list(range(10, 31, 5))
#Muestro los dos primeros elementos.
print(f"Los primeros dos elementos de la lista: {numeros[:2]}")



#Ejercicio 7
#Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” 
#por dos nuevos valores cualesquiera.

autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "rojo"
autos[2] = 8
print(f"Lista {autos}")

#Ejercicio 8
#Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 
# usando append directamente. Imprimir la lista resultante por pantalla.

dobles = []
#Se agregan elementos
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
#Se imprime lista resultante
print("Lista de dobles:", dobles)


#Ejercicio 9
#Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
#compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
#a) Agregar "jugo" a la lista del tercer cliente usando append.
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
#c) Eliminar "pan" de la lista del primer cliente.
#d) Imprimir la lista resultante por pantalla

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

#Se agrega jugo en el listado del tercer cliente.
compras[2].append("jugo")
#Se busca el indice donde se encuentra fideos en el segundo listado.
indice_fideos = compras[1].index("fideos")
#Se reemplaza fideos por tallarines
compras[1][indice_fideos] = "tallarines"
#Se remueve pan de la primer lista.
compras[0].remove("pan")
#Imprimimos lista actualizada.
print(f"Lista resultante: {compras}")


#Ejercicio 10
#Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#● Posición lista_anidada[0]: 15
#● Posición lista_anidada[1]: True
#● Posición lista_anidada[2][0]: 25.5
#● Posición lista_anidada[2][1]: 57.9
#● Posición lista_anidada[2][2]: 30.6
#● Posición lista_anidada[3]: False
#Imprimir la lista resultante por pantalla.

lista_anidada = [
    15,                     # lista_anidada[0]
    True,                   # lista_anidada[1]
    [25.5, 57.9, 30.6],     # lista_anidada[2][0], [2][1], [2][2]
    False                   # lista_anidada[3]
]

print(f"Lista resultante: {lista_anidada}")
