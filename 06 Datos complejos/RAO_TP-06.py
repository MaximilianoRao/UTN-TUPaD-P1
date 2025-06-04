#Maximiliano Rao

#Ejercicio 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# Se agregan pares clave-valor
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(f"Ejercicio 1: {precios_frutas}")

#Ejercicio 2
# Se actualizan precios de claves existentes
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(f"Ejercicio 2: {precios_frutas}")

#Ejercicio 3
# Con el metodo keys de los diccionarios, obtengo todas las frutas(claves) sin los precios
lista_claves = precios_frutas.keys()
print(f"Ejercicio 3: {lista_claves}")

#Ejercicio 4
# Crear un diccionario vacío para los contactos
contactos = {}
# Cargar 5 contactos
print("Cargá 5 contactos:")
for i in range (5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número telefónico de {nombre}: ")
    contactos[nombre] = numero

# Consultar un contacto
consulta = input("\nIngresá el nombre del contacto que querés buscar: ")

# Mostrar el número si el contacto existe
if consulta in contactos:
    print(f"El número de {consulta} es {contactos[consulta]}")
else:
    print(f"No se encontró un contacto con el nombre '{consulta}'.")

#Ejercicio 5
# Solicitar una frase al usuario y la separa por espacios
frase_lista = input("Ingrese una frase: ").split()

# Obtener palabras únicas usando un set
palabras_unicas = set(frase_lista)

# Contar la cantidad de veces que aparece cada palabra
conteo_palabras = {}

for palabra in frase_lista:
    if palabra in conteo_palabras:
        conteo_palabras[palabra] += 1
    else:
        conteo_palabras[palabra] = 1

# Mostrar resultados
print(f"\nPalabras únicas: {palabras_unicas}")
print(f"Frecuencia de cada palabra: {conteo_palabras}")


#Ejercicio 6
# Diccionario para guardar alumnos y sus notas
alumnos = {}

# Ingreso de datos
for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingresá la nota {j+1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

print(alumnos)
# Mostrar promedios
print("\nPromedio de cada alumno:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")


#Ejercicio 7
# Sets de estudiantes que aprobaron cada parcial
parcial1 = {"Ana", "Luis", "María", "Juan"}
parcial2 = {"María", "Pedro", "Luis", "Sofía"}

# Estudiantes que aprobaron ambos parciales (intersección)
ambos = parcial1 & parcial2
# Estudiantes que aprobaron solo uno de los dos (diferencia simétrica)
solo_uno = parcial1 ^ parcial2
# Estudiantes que aprobaron al menos uno (unión)
al_menos_uno = parcial1 | parcial2

# Mostrar resultados
print("Aprobaron ambos parciales:")
print(ambos)
print("\nAprobaron solo uno de los dos parciales:")
print(solo_uno)
print("\nAprobaron al menos un parcial:")
print(al_menos_uno)


#Ejercicio 8
# Diccionario inicial de productos y su stock
stock_productos = {"manzanas": 10,"bananas": 5,"naranjas": 8}

# Solicitar un producto
producto = input("Ingresá el nombre de un producto: ").lower()

# Verificar si el producto existe
if producto in stock_productos:
    print(f"Stock actual de {producto}: {stock_productos[producto]} unidades")    
    # Preguntar si quiere agregar unidades
    agregar = input("¿Querés agregar más unidades? (s/n): ").lower()
    if agregar == "s":
        cantidad = int(input("¿Cuántas unidades querés agregar?: "))
        stock_productos[producto] += cantidad
        print(f"Nuevo stock de {producto}: {stock_productos[producto]} unidades")
else:
    print(f"{producto} no existe en el stock.")
    
    # Preguntar si quiere agregar el nuevo producto
    nuevo = input("¿Querés agregarlo al stock? (s/n): ").lower()
    if nuevo == "s":
        cantidad = int(input("¿Cuántas unidades querés agregar?: "))
        stock_productos[producto] = cantidad
        print(f"{producto} agregado con {cantidad} unidades.")

# Mostrar el stock final
print("\nStock actualizado:")
print(stock_productos)


#Ejercicio 9
# Agenda con algunos eventos cargados
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "14:00"): "Clase de inglés",
    ("miércoles", "09:00"): "Consulta médica"
}
# Pedir al usuario que consulte un evento
dia = input("Ingresá el día: ").lower()
hora = input("Ingresá la hora (formato HH:MM): ")
# Buscar en la agenda
clave = (dia, hora)
if clave in agenda:
    print(f"Actividad programada para {dia} a las {hora}: {agenda[clave]}")
else:
    print(f"No hay ninguna actividad programada para {dia} a las {hora}.")


#Ejercicio 10
# Diccionario original: países -> capitales
paises_a_capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Japón": "Tokio",
    "Brasil": "Brasilia"
}

# Invertir el diccionario: capitales -> países
capitales_a_paises = {}

for pais, capital in paises_a_capitales.items():
    capitales_a_paises[capital] = pais

# Mostrar el nuevo diccionario
print("Diccionario invertido (capital -> país):")
print(f"original: {paises_a_capitales}")
print(f"invertido: {capitales_a_paises}")