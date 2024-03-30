# 6. Crea un ciclo infinito que reciba un nümero por teclado y verifique si es un numero primo, termina la ejecución si se ingresa el numero 0

while True:
    numero = int(input("Ingrese un número (0 para salir): "))
    
    if numero == 0:
        print("Programa terminado.")
        break
    
    if numero < 2:
        print("El número no es primo.")
        continue
    
    es_primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
    
    if es_primo:
        print("El número es primo.")
    else:
        print("El número no es primo.")



















