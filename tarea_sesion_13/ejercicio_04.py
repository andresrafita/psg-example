# 4. Crea un ciclo infinito que reciba una palabra por teclado y verifique si es palindroma, termina la ejecucion si se ingresa la palabra "salir"

while True:
    palabra = input("Ingresa una palabra (o escribe 'salir' para terminar): ")
    
    if palabra.lower() == 'salir':
        print("Saliendo del programa...")
        break
    
    if palabra == palabra[::-1]:
        print(f"{palabra} es un palíndromo.")
    else:
        print(f"{palabra} no es un palíndromo.")



















