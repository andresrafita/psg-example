# 2. Calculadora flexible: Crea una calculadora que acepte diferentes operaciones matematicas como argumentos de palabras clave y realice los calculos correspondientes, las operaciones son suma, resta, multiplicación y división

def calculadora(**kwargs):
    if 'suma' in kwargs:
        return sum(kwargs['suma'])
    elif 'resta' in kwargs:
        result = kwargs['resta'][0]
        for num in kwargs['resta'][1:]:
            result -= num
        return result
    elif 'multiplicacion' in kwargs:
        result = 1
        for num in kwargs['multiplicacion']:
            result *= num
        return result
    elif 'division' in kwargs:
        result = kwargs['division'][0]
        for num in kwargs['division'][1:]:
            if num != 0:
                result /= num
            else:
                return "Error: división por cero"
        return result
    else:
        return "Operación no válida"

# Ejemplos de uso
print(calculadora(suma=[5, 3, 2])) # Resultado: 10
print(calculadora(resta=[10, 3, 2])) # Resultado: 5
print(calculadora(multiplicacion=[2, 3, 4])) # Resultado: 24
print(calculadora(division=[20, 2, 5])) # Resultado: 2.0























