# Estructura de un condicional if
print("Inicio")
condicion = True
if condicion:
    # Bloque de codigo
    print("Cumple condicion")
print("Fin")

### Ejemplo: dado un numero, imprimir si es par
print("Inicio")
numero = 4
if numero % 2 == 0: # Si el modulo de 2 es 0
    print ("El numero es par")
print("Fin")

# Estructura de un if-else
print("Inicio")
condicion = False
if condicion:
    # Bloque de codigo
    print("Cumple condicion")
else:
    # Bloque de codigo
    print("No cumple condicion")
print("Fin")

### Ejemplo: Dado un numero, imprimir si es par o impar
print("Inicio")
numero = 3
if numero % 2 == 0: #Si el modulo de 2 es 0
    print("El numero es par")
else:
    print("El numero es impar")
print("Fin")

# Estructura de if-anidado
print("Inicio Anidado")
condicion_1 = True
condicion_2 = False
if condicion_1:
    print("Cumple condicion 1")
    if condicion_2:
        print("Cumple condicion 2")
    else:
        print("No cumple condicion 2")
else:
    print("No cumple condicion 1")
print("Fin")

### Ejemplo: Dado un numero, imprimir si es par, impar o cero
print("Inicio par, impar o cero")
numero = 0
if numero > 0 or numero < 0:
    if numero % 2 == 0: #Si el modulo de 2 es 0
        print("El numero es par")
    else:
        print("El numero es impar")
else:
    print("El numero es cero")
print("Fin")

# Estructura de un condicional elif
print("Inicio elif")
condicion_1 = False
condicion_2 = True
if condicion_1:
    print("Cumple condicion 1")
elif condicion_2:
    print("Cumple condicion 2")
else:
    print("No cumple condicion 1 ni 2")
print("Fin")

#### Ejemplo: Dado un numero, imprimir si es positivo, negativo o cero
print("Inicio positivo, negativo o cero")
numero = 0
if numero > 0:
    print("El numero es positivo")
elif numero < 0:
    print("El numero es negativo")
elif numero != 0:
    print("El numero es cero")
else:
    print("Error")
print("Fin")

# Estructura de operador ternario
print("Inicio Ternario")
condicion = True
resultado = "Cumple" if condicion else "no cumple"
print(resultado)
print("Fin")

### Ejemplo: Dado un numero, imprimir si es par o impar
print("Inicio ternario par, impar")
numero = 3
resultado = "El numero es par" if numero % 2 == 0 else "El numero es impar"
print(resultado)
print("Fin")

# Estructura Truthiness
print("Truthiness Enteros")
dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))
print(dividendo,divisor)
if divisor: #divisor != 0
    print(dividendo/divisor)
else:
    print("No se puede dividir entre cero")
print("Fin")

### Ejemplo: Introducir dos numeros flotantes y dividirlos
print("Truthiness Flotantes")
dividendo = float(input("Dividendo: "))
divisor = float(input("Divisor: "))
print(dividendo,divisor)
if divisor: #divisor != 0.0
    print(dividendo/divisor)
else:
    print("No se puede dividir entre cero")
print("Fin")

### Ejemplo2: Introducir una cadena y verificar si es vacia
print("Truthiness Cadenas")
cadena = input("Cadena: ")
print(cadena)
if cadena: # len(cadena) != 0 or cadena != ""
    print("La cadena no esta vacia")
else:
    print("La cadena esta vacia")
print("Fin")

### Ejemplo3: Introducir una tupla y verificar si es vacia
print("Truthiness Tuplas") # Aplica igual para listas y conjuntos
tupla = tuple(input("Tupla: "))
print(tupla)
if tupla: # len(tupla) != 0 or tupla != ""
    print("La tupla no esta vacia")
else:
    print("La tupla esta vacia")
print("Fin")

### Ejemplo4: Introducir la clave un valor y verificar si es vacio
print("Truthiness Diccionarios") 
diccionario = {}
clave = input("Clave: ")
valor = input("Valor: ")
if clave:
    diccionario = {clave:valor}
print(diccionario)
if diccionario: #diccionario != {}
    print("El diccionario no esta vacio")
else:
    print("El diccionario esta vacio")
print("Fin")

### Ejemplo5: Introducir un valor y verificar si es None
print("Truthiness None") 
valor = None
print(valor,type(valor))
if valor: #valor != None
    print("El valor no es None")
else:
    print("El valor es None")
print("Fin")

## Ejemplo final: El operador ternario es util para asignar valores a variables
entero = int(input("Entero: "))
resultado = "Diferente de 0" if entero else "Igual a 0"
print(resultado)
flotante = float(input("Flotante: "))
resultado = "Diferente de 0.0" if flotante else "Igual a 0.0"
print(resultado)
cadena = input ("Cadena: ")
resultado = "No esta vacia" if cadena else "Esta vacia"
print(resultado)

#### Ejercicio1: Tienes un dispositivo que mide la temperatura y si la temperatura es mayor a 30C enciende un ventilador y si es menor a 20C lo apaga
temperatura = float(input("Temperatura: "))
if temperatura > 30:
    print("Encender ventilador")
elif temperatura < 20:
    print("Apagar ventilador")

#### Ejercicio2: Tienes una cesta de frutas y quieres saber si tienes manzanas, si hay manzanas las cuentas y si no hay compras dos manzanas
cesta = ['🍎','🍑','🍓','🍉']
print(cesta)
if '🍎' in cesta:
    print(f"Hay {cesta.count('🍎')} manzanas")
else:
    cesta.extend(['🍎','🍎'])
    print(cesta)
# Con operador ternario
cesta = ['🍑','🍓','🍉']
print(cesta)
resultado = f"Hay {cesta.count('🍎')} manzanas" if '🍎' in cesta else cesta.extend(['🍎','🍎'])
print(resultado)
print(cesta) # Tener cuidado al usar un operador ternario puede salir errores si no haces bien

#### Ejercicio3: En un diccionario tienes almacenado un animal y quieres saber si es un mamifero
animal = {'especie':'🐶','nombre':'Firulais','mamifero':True}
print(animal)
if animal.get('mamifero'): #animal['mamifero']
    print('Es un mamifero')
else:
    print('No es un mamifero')

#### Ejercicio4: Dado dos conjuntos, verificar si tienen elementos en comun y mostrarlos y si no, unirlos
#### {'⚽','🏀','⚾'},{'🏈','🏉','🎾'}

conjunto_1 = {'⚽','🏀','⚾'}
conjunto_2 = {'🏈','🏉','🎾'}
print(conjunto_1,conjunto_2)
if conjunto_1.isdisjoint(conjunto_2): # len(conjunto_1.intersection(conjunto_2)) == 0
    conjunto_1.update(conjunto_2)
    print(conjunto_1)
else:
    print("Tienen elementos en comun")
    print(conjunto_1.intersection(conjunto_2))

#### Ejercicio5: Validar si un correo electronico es valido usando input
#### ✅: mail@domain.com, ma.il@domain.com
#### ❌: mail@domain, maildomain.com,@.
#### ❌: mail@@domain.com, mail@.com
correo = input("Correo: ") #Solucion anidada
if "@" in correo and "." in correo and correo.count("@") == 1:
    if correo.find("@") < correo.rfind(".") and correo.find("@") > 0 and correo.rfind(".") < len(correo) - 1:
        if correo.rfind(".") - correo.find("@") > 1:
            if correo.find(".") - correo.find("@") > 1:
                print("El correo es valido")
            else:
                print("El correo no es valido")
        else:
            print("El correo no es valido")
    else:
        print("El correo no es valido")
else: 
    print("El correo no es valido")

correo = input("Correo: ") #Solucion con elif
if "@" not in correo or "." not in correo or correo.count("@") != 1:
    print("El correo no es valido")
elif correo.find("@") >= correo.rfind(".") or correo.find("@") == 0 or correo.rfind(".") == len(correo) - 1:
    print("El correo no es valido")
elif correo.rfind(".") - correo.find("@") <= 1:
    print("El correo no es valido")
elif correo.find(".") - correo.find("@") == 1:
    print("El correo no es valido")
else:
    print("El correo es valido")












































