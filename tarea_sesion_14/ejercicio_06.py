# 6. Crear una funcion que reciba una lista de numeros y devuelva solo los numeros pares

def numeros_pares(lista):
    return [num for num in lista if num % 2 == 0]

# Ejemplo de uso
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Números pares:", numeros_pares(numeros))




















