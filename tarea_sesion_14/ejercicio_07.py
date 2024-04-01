# 7. Simular un tres en raya con funciones donde reciba las jugadas y devuelva el ganador hasta que alguien ingrese "salir"

def imprimir_tablero(tablero):
    for fila in tablero:
        print("|".join(fila))
    print("-----")

def verificar_ganador(tablero):
    for fila in tablero:
        if fila.count(fila[0]) == len(fila) and fila[0] != ' ':
            return fila[0]
    for col in range(len(tablero[0])):
        if tablero[0][col] == tablero[1][col] == tablero[2][col] and tablero[0][col] != ' ':
            return tablero[0][col]
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != ' ':
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != ' ':
        return tablero[0][2]
    return None

def jugar_tres_en_raya():
    tablero = [[' ']*3 for _ in range(3)]
    jugador = 'X'
    ganador = None

    while not ganador:
        imprimir_tablero(tablero)
        jugada = input("Turno del jugador " + jugador + ". Ingrese la fila y la columna separadas por espacio (ejemplo: 1 2): ")
        if jugada == "salir":
            print("¡Hasta luego!")
            return

        fila, columna = map(int, jugada.split())
        if tablero[fila-1][columna-1] == ' ':
            tablero[fila-1][columna-1] = jugador
            ganador = verificar_ganador(tablero)
            if jugador == 'X':
                jugador = 'O'
            else:
                jugador = 'X'
        else:
            print("Esa casilla ya está ocupada. Intenta de nuevo.")

    imprimir_tablero(tablero)
    print("¡El jugador", ganador, "ha ganado!")

# Ejecutar el juego
jugar_tres_en_raya()




















