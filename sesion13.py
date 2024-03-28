# Estructura de control for
print("Inicio")
for i in range(5):
    print(i)
print("Fin")

### Ejemplo1: sumar los numeros del 1 al 10 de 2 en 2
suma = 0 
for i in range(1,11,2): #1,3,5,7,9
    suma += i # suma = suma + i
print(suma)

### Ejemplo2: crear un arbol de navidad de 6 niveles
for i in range(0,6):
    print(" " * (5-i) + "*" * i * 2 + "*")

### Ejemplo3: crear una serie de numeros cuadrados del 1 a 10
for i in range(1,11):
    print(i**2, end=" ")

### Ejemplo4: crear una lista de numeros pares del 1 al 10
pares = []
for i in range(0,11,2):
    pares.append(i)
print(pares)

#### Ejercicio1: imprimir los 10 primeros de la serie numeros cubicos
for i in range(1,11):
    print(i**3, end=" ")

# Ciclo for con secuencia
for fruta in ['🍎','🍌','🍇','🍉']:
    print(fruta)

### Ejemplo5: imprimir los elementos de una lista de fiestas
fiesta = ['🎄','🎡','🎁','🎊','✨','🕯️']
for objeto in fiesta:
    print(objeto)

### Ejemplo6: imprimir los elementos de una tupla de frutas separadas por coma
frutas = ('🍅','🍇','🍍','🍉','🍊')
for fruta in frutas:
    print(fruta,end=", ")

### Ejemplo 7: imprimir los elementos de un diccionario
diccionario = {'🍅':'tomate','🍇':'uva','🍍':'piña','🍉':'sandia','🍊':'naranja'}
for clave in diccionario:
    print(clave, diccionario[clave])

### Ejemplo8: imprimir los elementos de la cadena de evolucion añadiendo una flecha
ciclo_vida = '🥚🐣🐥🐤🐔🍗'
for etapa in ciclo_vida:
    print(i, end="->")

## Recorrer elementos con indexacion (listas,tuplas) mediante:
### in como pertenencia

### Ejemplo9: listar los elementos de la siguiente serie ['🐶','😺','🐰','🐭']
animales = ['🐶','😺','🐰','🐭']
for animal in animales:
    print(i)

### Ejemplo10: listar los elementos de la siguiente serie ['🐶','😺','🐰','🐭']
animales = ['🐶','😺','🐰','🐭']
for i in range(len(animales)):
    print(animales[i])

### Ejemplo11: listar los elementos de la siguiente serie ['🐶','😺','🐰','🐭']
animales = ['🐶','😺','🐰','🐭']
for i,animal in enumerate(animales):
    print(i,animal,animales[i])

#### Ejercicio2: imprimir la cantidad de veces los elementos de la cadena '⚽🏀🏐🎱' de acuerdo a su posicion mas 1
esferas = '⚽🏀🏐🎱'
for i, esfera in enumerate(esferas):
    print(esfera*(i+1))

#While
### Ejemplo12: imprimir los numeros mientras sean menores o igual a 5 empezando desde 0
i = 0
while i <= 5:
    print(i)
    i += 1

### Ejemplo13: sumar los numeros mientras no se ingrese por teclado el numero 0
suma = 0
numero = int(input("Ingrese un numero: "))
while numero != 0:
    suma += numero
    numero = int(input("Ingrese un numero: "))
print(suma)

#### Ejercicio3: ingresa un numero por teclado y genera un contador hasta 0 si el numero es negativo no hace nada
numero = int(input("Ingrese un numero: "))
while numero >= 0:
    print(numero)
    numero -= 1

# Break
### Ejemplo14: de la siguiente lista de frutas imprimir los elementos hasta que se encuentre un gusano con for
frutas = ['🍎','🍌','🍇','🍉','🐛','🍍','🍊']
for fruta in frutas:
    if fruta == '🐛':
        break
    print(fruta)
print("Fin")

#Con while
frutas = ['🍎','🍌','🍇','🍉','🐛','🍍','🍊']
i = ""
while i != '🐛':
    i = frutas.pop(0)
    print(i)
print("Fin")

### Ejemplo15: crear un ciclo infinito que imprima un contador incremental
contador = 0
while True:
    print(contador)
    contador += 1

### Ejemplo16: crear un infinito que pida una cadena de texto la ponga en mayusculas y la imprima hasta que se ingrese la palabar salir
print("Ejemplo 16")
while True:
    texto = input("Ingrese un texto: ")
    if texto == "salir":
        break
    print(texto.upper())











































































