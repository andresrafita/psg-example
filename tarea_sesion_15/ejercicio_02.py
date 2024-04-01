# 2. Crear un programa para crear una canasta de frutas, solicitar frutas por teclado y almacenar en una lista, si se ingresa "salir" termina la ejecución. Solo se permiten las siguientes frutas caso contrario lanzar una excepcion personalizada: 🍎🍇🍈🍉🍌🍍🍑

frutas_permitidas = ['🍎', '🍇', '🍈', '🍉', '🍌', '🍍', '🍑']

while True:
    try:
        fruta = input("Ingrese una fruta (🍎🍇🍈🍉🍌🍍🍑) o 'salir' para terminar: ")
        if fruta == 'salir':
            print("¡Canasta de frutas finalizada!")
            break
        elif fruta not in frutas_permitidas:
            raise ValueError("Fruta no permitida")
        else:
            print("Agregando", fruta, "a la canasta.")
            # Aquí podrías agregar la fruta a una lista de canasta si lo deseas.
    except ValueError as ve:
        print(ve)





















