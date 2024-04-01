# Ejercicio1:division entre cero
print ("Inicio Ejemplo 1")
x = 1 / 0
print (x)
print ("Fin Ejemplo 1")

print ("Inicio Ejemplo 1")
try:
    x = 1 / 0
    print (x)
except Exception as e:
    print("💀 Error:", e, type(e))
print ("Fin Ejemplo 1")

# Ejercicio1: Crea un programa que solicite dos numeros y realice la division de ambos numeros. Si hay un error mostrar un mensaje de error. El programa se detiene si se ingresa "salir"
while True:
    try:
        num1 = input("Ingrese el primer número: ")
        if num1 == "salir":
            break
        num2 = input("Ingrese el segundo número: ")
        if num2 == "salir":
            break
        num1 = float(num1)
        num2 = float(num2)
        print("Resultado:", num1 / num2)
    except Exception as e:
        print("💀 Error:", e)

# Ejemplo2: division por cero
print ("Inicio Ejemplo 2")
divisor = 0
try:
    x = 1 / divisor
    print (x)
except ZeroDivisionError as e:
    print("0️⃣ Error:", e, type(e))
except Exception as e:
    print("💀 Error:", e, type(e))
print ("Fin Ejemplo 2")

# Ejemplo3: de la lista de calificaciones obtener el promedio
calificaciones = [20,40,80,"A"] # intenta de nuevo quitando la "A"
suma = 0
try:
    for i in range(len(calificaciones)+1): # quitar el +1
        suma += calificaciones[i]
    promedio = suma / len(calificaciones)
    print("Promedio:", promedio)
except ZeroDivisionError as e:
    print("0️⃣ Error:", e, type(e))
except TypeError as e:
    print("🎭 Error:", e, type(e))
except Exception as e:
    print("💀 Error:", e, type(e))

# Ejemplo 4: de la lista de calificaciones obtener el promedio
print ("Inicio Ejemplo 4")
calificaciones = [20,40,80]
suma = 0
try:
    for i in range(len(calificaciones)):
        suma += calificaciones[i]
    promedio = suma / len(calificaciones)
    print("Promedio:", promedio)
except Exception as e:
    print("💀 Error:", e, type(e))
else:
    print ("🎉 Sin errores")
print ("Fin Ejemplo 4")

# Ejercicio2: Crear un programa que solicite dos numeros y mediante una funcion devuelva la division de ambos. Si hay un error mostrar un mensaje de error. el programa se detiene si se ingresa "salir". Añadir un bloque else que muestre el resultado de la funcion
def division(num1, num2):
    return num1 / num2

while True:
    try:
        num1 = input("Ingrese el primer número: ")
        if num1 == "salir":
            break
        num2 = input("Ingrese el segundo número: ")
        if num2 == "salir":
            break
        num1 = float(num1)
        num2 = float(num2)
        resultado = division(num1, num2)
    except Exception as e:
        print("💀 Error:", e)
    else:
        print("🎉 Resultado: ",resultado)

# Ejemplo 5: simula una conexion a internet que haga ping y cerrar la conexion
print ("Inicio Ejemplo 5")
try:
    print("🔗 Ping...")
except Exception as e:
    print("💀 Error:", e)
else:
    print("🎉 Ping Exitoso")
finally:
    print("🔌 Cerrando conexión")

# Ejemplo 6: simula una conexion a internet que haga ping y cerrar la conexion
print ("Inicio Ejemplo 6")
try:
    print("🔗 Ping...")
    raise Exception("Error de conexión") #Excepción genérica
except Exception as e: # Captura cualquier excepción
    print("💀 Error:", e)
else:
    print("🎉 Ping Exitoso")
finally:
    print("🔌 Cerrando conexión")

# Ejercicio3: Escriba un programa que solicite un numero por teclado y se almacene en una lista. Si es 0 se genera una excepcion. Si la ejecucion es correcta muestra "Agregado". Termina la ejecucion solo con la palabra "salir" utilizar la excepcion KeyboardInterrumpt. Finalmente imprima siempre la suma de los numeros y la lista

numeros = []
while True:
    try:
        num = input("Ingrese un número: ")
        if num == "salir":
            break
        num = float(num)
        if num == 0:
            raise Exception("No se puede agregar el número 0")
        numeros.append(num)
    except KeyboardInterrupt as e:
        print("🛑 Error:", e)
    except Exception as e:
        print("💀 Error:", e)
    else:
        print("🎉 Número agregado")
    finally:
        print("Suma:", sum(numeros))

#ejemplo7: crear una funcion que no hace nada
print("Inicio Ejemplo 7")
def funcion():
    pass

funcion()
print("Fin Ejemplo 7")

#ejemplo8
print("Inicio Ejemplo 8")
class GusanoError(Exception):
    pass
 
frutero = ['🍎', '🍌', '🍐', '🐛', '🍇']
for fruta in frutero:
    try:
        if fruta == '🐛':
            raise GusanoError("😱 Ewww!")
        print(fruta)
    except GusanoError as e:
        print("🐛 Error:", e)
    except Exception as e:
        print("💀 Error:", e)
print("Fin Ejemplo 8")

#ejercicio4: crear un programa que solicite palabras por teclado y almacene en una lista. Si se inserta caracteres no alfabeticos se genera una excepcion personalizada y no se almacena. Si se ingresa "salir" se termina la ejecucion. Mostrar el mensaje "Palabra agregada" si no hay errores. Finalmente imprimir la lista de palabras.
class NoAlfabeticoError(Exception):
    pass

palabras = []
while True:
    try:
        palabra = input("Ingrese una palabra: ")
        if palabra == "salir":
            break
        if not palabra.isalpha():
            raise NoAlfabeticoError("Solo se permiten letras")
        palabras.append(palabra)
    except NoAlfabeticoError as e:
        print("🚫 Error:", e)
    except Exception as e:
        print("💀 Error:", e)
    else:
        print("🎉 Palabra agregada")
    finally:
        p
rint("Lista:", palabras)














































































