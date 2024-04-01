# 1. Crear una calculadora que solicite dos numeros y realice las operaciones basicas de suma, resta, multiplicacion y division con manejo de excepciones, para salir del programa se debe ingresar "salir"

def calcular(operador, num1, num2):
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    elif operador == '/':
        if num2 == 0:
            raise ValueError("Error: división por cero")
        return num1 / num2
    else:
        raise ValueError("Operador no válido")

while True:
    try:
        operacion = input("Ingrese la operación (suma, resta, multiplicacion, division) o 'salir' para salir: ")
        if operacion.lower() == 'salir':
            print("¡Hasta luego!")
            break
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = calcular(operacion, num1, num2)
        print("El resultado de la operación es:", resultado)
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print("Error:", e)



















