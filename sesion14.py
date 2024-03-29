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
def juego_piedra_papel_tijera():
    while True:
        jugada1 = input("Jugador 1, elige piedra, papel o tijera (o escribe 'salir' para terminar): ").lower()
        jugada2 = input("Jugador 2, elige piedra, papel o tijera (o escribe 'salir' para terminar): ").lower()

        if jugada1 == 'salir' or jugada2 == 'salir':
            print("¡Juego terminado!")
            break
        
        resultado = determinar_ganador(jugada1, jugada2)
        print(f"Jugador 1 eligió {jugada1}, Jugador 2 eligió {jugada2}. Resultado: {resultado}")

def determinar_ganador(jugada1, jugada2):
    reglas = {
        ('piedra', 'tijera'): 'Jugador 1 gana',
        ('papel', 'piedra'): 'Jugador 1 gana',
        ('tijera', 'papel'): 'Jugador 1 gana',
        ('tijera', 'piedra'): 'Jugador 2 gana',
        ('piedra', 'papel'): 'Jugador 2 gana',
        ('papel', 'tijera'): 'Jugador 2 gana',
        ('piedra', 'piedra'): 'Empate',
        ('papel', 'papel'): 'Empate',
        ('tijera', 'tijera'): 'Empate'
    }

    return reglas.get((jugada1, jugada2), 'Jugada no válida')

# Ejecutar el juego
juego_piedra_papel_tijera()



























































































































