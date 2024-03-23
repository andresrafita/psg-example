# 6. Crea una calculadora por consola que realice las operaciones de suma, resta, multiplicacion y division. Ingresa dos numeros y la operacion a realizar, verifica si la operacion es válida y muestra el resultado:
# Numero 1: 10
# Numero 2: 5
# Operacion: +
# -------------
# Resultado: 15

num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))
operacion = input("Operación (+, -, *, /): ")

if operacion == '+':
    resultado = num1 + num2
elif operacion == '-':
    resultado = num1 - num2
elif operacion == '*':
    resultado = num1 * num2
elif operacion == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Error: No se puede dividir por cero")
        resultado = None
else:
    print("Error: Operación no válida")
    resultado = None

if resultado is not None:
    print("-------------")
    print("Resultado:", resultado)











