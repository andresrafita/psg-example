# 2. Imprimir los 20 primeros numeros primos

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

cantidad_numeros_primos = 0
numero_actual = 2

while cantidad_numeros_primos < 20:
    if es_primo(numero_actual):
        print(numero_actual)
        cantidad_numeros_primos += 1
    numero_actual += 1



















