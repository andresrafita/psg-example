# Estructura de funcion
def funcion():
    print("Bloque de codigo")

funcion()

### Ejemplo1: Crear una funcion para imprimir una lista de 10 numero pares y llamarla dos veces
print ("Ejemplo 1")
print ("1. Definir función")
def imprimir_pares():
    pares = [i for i in range(0, 21, 2)]
    print (pares)
 
print ("2. Llamar función")
imprimir_pares()
imprimir_pares()

#### Ejercicio1: crear una funcion que imprima un mensaje de bienvenida del siguiente conjunto de forma aleatoria
#### mensajes = {"Bienvenido al Python Study Group 🐍",
#### "¡Hola y bienvenido al Python Study Group! ✨",
#### "Hola, aprendamos Python juntos 🐍"}
def bienvenida():
    mensajes = {"Bienvenido al Python Study Group 🐍",
    "¡Hola y bienvenido al Python Study Group! ✨",
    "Hola, aprendamos Python juntos 🐍"}
    print (mensajes.pop())
bienvenida()

# Funcion sin argumentos y con un retorno
def funcion():
    return "Bloque de codigo"
resultado = funcion()
print(resultado)

### Ejemplo 3, crear una funcion que devuelva un saludo en diferentes idiomas
print ("Ejemplo 2")
print ("1. Definir función")
def saludo():
    saludos = {"Hola", "Hello", "Bonjour", "Ciao"}
    return saludos.pop()
print ("2. Llamar función")
resultado = saludo()
print (resultado)

#### Ejercicio2: Devolver una fruta aleatoria del siguiente conjunto
#### frutas = {'🍅','🍌','🍎','🍇','🍉'}
def devolver_fruta():
    frutas = {'🍅','🍌','🍎','🍇','🍉'}
    return frutas.pop()

fruta = devolver_fruta()
print (fruta)

# Funcion sin argumentos y con multiples retornos
def funcion():
    return "Bloque", "de", "codigo"
resultado = funcion()
print(resultado)

### Ejemplo3, crear una funcion que devuelva un saludo en dos idiomas
print ("Ejemplo 3")
print ("1. Definir función")
def saludo():
    saludos_es = {"Hola", "Holi", "Buenos días"}
    saludos_en = {"Hello", "Hi", "Good morning"}
    return saludos_es.pop(), saludos_en.pop()
print ("2. Llamar función")
resultado = saludo()
print (resultado)

#### Ejercicio4: Devolver una fruta y un color aleatorio de los siguientes conjuntos
#### {'🍅','🍌','🍎','🍇','🍉'}
#### {'🔴','🟠','🟡','🟢','🔵'}
def devolver_fruta_color():
    frutas = {'🍅','🍌','🍎','🍇','🍉'}
    colores = {'🔴','🟠','🟡','🟢','🔵'}
    return frutas.pop(), colores.pop()

fruta, color = devolver_fruta_color()
print (fruta, color)

# Funcion con un argumento y sin retorno


### Ejemplo4: crear una funcion que imprima el cuadrado de un numero
print ("Ejemplo 4")
print ("1. Definir función")
def cuadrado(numero):
    print (numero**2)
 
print ("2. Llamar función")
cuadrado(5)
cuadrado(10)

#### Crear una funcion que imprima el mensaje de bienvenida de acuerdo al idioma enviado como argumento, si no existe imprimir un mensaje por defecto
#### mensajes = {"es":"Bienvenido al Python Study Group 🐍",
#### "en": "Hello and welcome to the Python Study Group! ✨",}

def bienvenida(idioma):
    mensajes = {
        "es":"Bienvenido al Python Study Group 🐍",
        "en": "Hello and welcome to the Python Study Group! ✨",
    }
    print (mensajes.get(idioma, "¡Hola!"))

bienvenida("es")
bienvenida("en")
bienvenida("fr")

# Funcion con multiples argumentos y sin retorno

### Ejemplo5: crear una funcion que reciba una cadena y un entero y repita la cadena el numero de veces
print ("Ejemplo 5")
print ("1. Definir función")
def repetir(cadena, veces):
    print (cadena*veces)
print ("2. Llamar función")
repetir("✨🎉", 10)

#### Ejercicio5: Crear un funcion que reciba una lista de animales, un entero y devuelva una lista con los animales repetidos el numero de veces
#### ['🐶','🐱','🐭','🐹','🐰']
def repetir_animales(animales, veces):
    lista = [animal*veces for animal in animales]
    print (lista)

animales = ['🐶','🐱','🐭','🐹','🐰']
repetir_animales(animales, 3)

print (resultado)

# Funciones con multiples argumentos y con un retorno

### Ejemplo6: crear una funcion qeu reciba dos numeros y devuelva una lista con la suma, resta, multiplicacion y division de los numeros
print ("Ejemplo 6")
print ("1. Definir función")
def operaciones(numero1, numero2):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2
    return [suma, resta, multiplicacion, division]
 
print ("2. Llamar función")
resultado = operaciones(10, 5)
print (resultado)

#### Ejercicio6: Crear una funcion que reciba dos enteros y una cadena devolver el resultado de la operacion de los numeros egun la cadena puede ser suma, resta, multiplicacion o division
def operacion(numero1, numero2, operacion):
    if operacion == "suma":
        return numero1 + numero2
    elif operacion == "resta":
        return numero1 - numero2
    elif operacion == "multiplicacion":
        return numero1 * numero2
    elif operacion == "division":
        return numero1 / numero2
    else:
        return "Operación no válida"

resultado = operacion(10, 5, "suma")
print (resultado)

# Funcion con multiples argumentos y con multiples retornos

### Ejemplo7: crear una funcion que reciba dos numeros y devuelva la suma, resta, multiplicacion y division de los dos numeros
print ("Ejemplo 7")
print ("1. Definir función")
def operaciones(numero1, numero2):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2
    return suma, resta, multiplicacion, division
 
print ("2. Llamar función")
suma, resta, multiplicacion, division = operaciones(10, 5)
print (suma, resta, multiplicacion, division)

#### Ejercicio7: Crear un juego de piedra,papel o tijera, donde reciba dos jugadas por teclado y devuelva las jugadas y el resultado, si ingresa "salir", entonces terminar el juego
def jugar_piedra_papel_tijera(jugada1, jugada2):
    if jugada1 == jugada2:
        resultado = "Empate"
    elif jugada1 == "piedra" and jugada2 == "tijera":
        resultado = "Jugador 1 gana"
    elif jugada1 == "papel" and jugada2 == "piedra":
        resultado = "Jugador 1 gana"
    elif jugada1 == "tijera" and jugada2 == "papel":
        resultado = "Jugador 1 gana"
    else:
        resultado = "Jugador 2 gana"
    return jugada1, jugada2, resultado

while True:
    jugador1 = input("Jugador 1: ")
    if jugador1 == "salir":
        break
    jugador2 = input("Jugador 2: ")
    if jugador2 == "salir":
        break
    resultado = jugar_piedra_papel_tijera(jugador1, jugador2)
    print (resultado)

# Variable global
"""
def funcion():
    variable_local = "Variable local"
    print(variable_global)
    print(variable_local)
funcion()
print(variable_global)
print(variable_local)
"""

### Ejemplo8: de la siguiente lista de numeros obtener el mayor y menor numero con una funcion
numeros = [10,5,20,15,25,30] #global

def mayor_menor(): #no recibe argumentos
    mayor = max(numeros) #local
    menor = min(numeros) #local
    return mayor, menor #devuelve dos valores

resultado = mayor_menor()
print(resultado)

#### Ejercicio8: de la siguiente cadena global convertir en formato titulo y contar las vocales aeiou con una funcion
def formato_vocales():
    titulo = cadena.title()
    vocales = sum([1 for letra in titulo if letra in "aeiou"])
    return titulo, vocales
cadena = "python es un lenguaje de programación"
resultado = formato_vocales

print(resultado)

# Estructura de un *arg
def function(*args):
    print(args)
    print(type(args))
funcion("Bloque","de","codigo")

### Ejemplo 9: crear una funcion que reciba un numero y una cantidad de cadenas, concatene las cadenas y la devuelva repetida N veces
print("1. Definir función")
def concatenar(numero, *cadenas):
    concatenado = ""
    for cadena in cadenas:
        concatenado += cadena
    return concatenado*numero

print("2. Llamar función")
resultado = concatenar(3,"🍎","🍌","🍍")
print(resultado)

#### Ejercicio9: crear una funcion que reciba N objetos y genere una tupla y una lista con los objetos usando *args
def tupla_lista(*args):
    tupla = tuple(args)
    lista = list(args)
    return tupla,lista

lista,tupla = tupla_lista(1,1.1, True, "🍎")
print(lista)
print(tupla)

# Estructura de un **kwargs
def funcion(**kwargs):
    print(kwargs)
    print(type(kwargs))

funcion(nombre="Jhon",apellido="Doe",genero="M")

### Ejemplo10: crear una funcion que reciba los datos de una persona y devuelva un mensaje con los datos
print("1. Definir función")
def datos_persona(**datos):
    mensaje = ""
    for clave, valor in datos.items():
        mensaje += f"{str(clave).title()}: {str(valor).upper()}\n"
    return mensaje
print("2. Llamar función")
resultado = datos_persona(nombre="Jhon", apellido="Doe",edad=20, boliviano=True)
print(resultado)

#### Ejercicio10: crea un simulador de lavar platos con una función que reciba los objetos a lavar y el tiempo de lavado de cada objeto devuelva un mensaje con los objetos lavados y el tiempo total de lavado
def lavar(**objetos):
    tiempo_total=0
    mensaje=""
    for objeto, tiempo in objetos.items():
        tiempo_total += tiempo
        mensaje += f"{objeto}: {tiempo} minutos\n"
    mensaje += f"Tiempo total: {tiempo_total} minutos"
    return mensaje
resultado = lavar(plato=5,vaso=3,tenedor=1,cuchara=0.5)
print(resultado)

# Acceso a la documentación con .__doc__
print("Acceso a la documentación")
def funcion():
    """
    Documentacion aqui
    """
    print("Bloque de codigo")
print(funcion.__doc__)
print("Fin de la ejecución")

### Ejemplo11: crear tres funciones una principal que reciba un numero y dos funciones anidads que devuelvan el cuadrado y el cubo del numero
print("1. Definir funcion principal")
def principal(numero):
    cuadrado = cuadrado_numero(numero)
    cubo = cubo_numero(numero)
    return cuadrado, cubo
print("2. Definir funcion Cuadrado")
def cuadrado_numero(numero):
    return numero**2
print("3. Definir funcion Cubo")
def cubo_numero(numero):
    return numero**3

#### Ejercicio11: crear funciones de limpieza de una cadena para obtener las letras y convertir todo en mayusculas crea funciones de limpieza y funcion una princial
def limpiar_letras(cadena):
    """
    Elimina los numeros de una cadena y espacios
    """
    return "".join([letra for letra in cadena if letra.isalpha()])
def limpiar_mayusculas(cadena):
    """
    Convierte una cadena en mayusculas
    """
    return cadena.upper()
def limpiar(cadena):
    cadena = limpiar_letras(cadena)
    cadena = limpiar_mayusculas(cadena)

# Funcion recursiva
print("1. Definir función")
def numero_par(numero):
    if numero == 0:
        return 0
    else:
        return numero_par(numero-1)+2
print("2. Llamar funcion")
resultado = numero_par(10)
print(resultado)

### Ejemplo12: crear una funcion recursiva para obtener el 10mo numero par
print ("Ejemplo 12")
print ("1. Definir función")
def numero_par(numero):
    if numero == 0:
        return 0
    else:
        return numero_par(numero-1) + 2
 
print ("2. Llamar función")
resultado = numero_par(10)
print (resultado)

#### Ejercicio12: Crear una funcion recursiva para obtener el factorial de un numero (5! = 5*4*3*2*1 = 120)
def factorial(n):
    # Caso base: factorial de 0 es 1
    if n == 0:
        return 1
    # Caso recursivo: factorial de n es n * factorial(n-1)
    else:
        return n * factorial(n-1)

# Ejemplo de uso
numero = 5
resultado = factorial(numero)
print(f"El factorial de {numero} es: {resultado}")

#Funcion anonima o lambda
lambda argumento: expresion

### Ejemplo13: crear una funcion anonima para obtener el cuadrado de un numero
print ("Ejemplo 13")
cuadrado = lambda numero: numero**2
resultado = cuadrado(5)
print (resultado)
resultado = cuadrado(10)
print (resultado)

#### Ejercicio13: Crear una funcion anonima para obtener de una cadena las letras solo los alfanumericos y convertir en mayusculas: 
#### Cadena = "Python es un lenguaje de programación"
cadena = "Python es un lenguaje de programación"
limpiar = lambda cadena: "".join([letra for letra in cadena if letra.isalnum()]).upper()
resultado = limpiar(cadena)
print (cadena)
print (resultado)










































































































