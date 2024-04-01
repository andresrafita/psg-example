# 3. Crear una función recursiva para obtener el N numero de la serie de Fibonacci

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Ejemplo de uso
n = 10
print("El", n, "º número de la serie de Fibonacci es:", fibonacci(n))















