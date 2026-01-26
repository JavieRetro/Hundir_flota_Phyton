import random
from funciones_flota import(
    flota,
    Agua,
    Hundido,
    Oculto,
    mostrarTablero,
    colocar_barcos,
    disparar,
    quedan_barcos
)

print("🌊🚢 HUNDIR LA FLOTA 🚢🌊")

# --------------------------------
# SELECCIÓN DE MODO DE JUEGO
# --------------------------------
print("1. Un jugador")
print("2. Dos jugadores")

modo = int(input("Elige el modo de juego(1, 2): "))
while modo not in [1, 2]:
    modo = int(input("Opción inválida. Escoge 1 o 2: "))

#Pedimos el tamaño para el tablero
tam = int(input("Introduce un tamaño para el tablero (8 o 10): "))
#Validación del tamaño si es correcto o no
while tam not in [8, 10]:
    tam = int(input("Tamaño inválido, introduce otro(8 o 10): "))

#-----------------------
# MODO 1 JUGADOR
#-----------------------

if modo == 1:

    #Creacion de tableros
    #El tablero visible es el que ve el jugador mientras juega, formado por piezas ⬜
    tablero_visible = [[Oculto for _ in range(tam)] for _ in range(tam)]

    #El tablero oculto contiene la información del juego
    #Tanto el agua como los barcos
    tablero_oculto = [[" " for _ in range(tam)] for _ in range(tam)]

    #Colocamos los barcos dentro del tablero oculto aleatoriamente y asi descubrirlos
    colocar_barcos(tablero_oculto, flota)

    #----------------
    #Bucle principal
    #----------------
    #Mientras quedan barcos por hundir en el tablero oculto...
    while quedan_barcos(tablero_oculto):

        #El tablero visible sigue siendo el unico que se muestra
        mostrarTablero(tablero_visible)

        try:
            fila = int(input(f" Introduce la primera coordenada:(0, {tam-1})"))
            columna = int(input(f"Introduce la primera coordenada: Columna: (0, {tam-1})"))
        except ValueError:
            print("Entrada inválida, escoge otra.")
            continue

        if fila < 0 or fila >= tam or columna < 0 or columna >= tam:
            print("Fuera del tablero")
            continue
        #Realizamos el disparo para actualizar el tablero visible

        disparar(tablero_visible, tablero_oculto, fila, columna)

    #------------------
    #Final del juego
    #------------------

    print("Enhorabuena,hundiste toda la flota")
    print("Tablero completo: ")
    for i in range(tam):
        for j in range(tam):
            if tablero_oculto[i][j] == " ":
                tablero_visible[i][j] = Agua
            elif tablero_oculto[i][j] in ["P","B","S","C","L"]:
                tablero_visible[i][j] = Hundido
            
    mostrarTablero(tablero_visible)

#--------------------------------
#MODO 2 JUGADORES
#--------------------------------
else:    
    jugador1 = input("Nombre del jugador 1: ")
    jugador2 = input("Nombre del jugador 2: ")

    moneda = random.choice([jugador1, jugador2])

    print(f"La moneda decide que empieza {moneda}")

    tablero_visible1 = [[Oculto for _ in range(tam)]for _ in range(tam)]
    tablero_oculto1 = [[" " for _ in range(tam)]for _ in range(tam)]

    tablero_visible2 = [[Oculto for _ in range(tam)]for _ in range(tam)]
    tablero_oculto2 = [[" " for _ in range(tam)]for _ in range(tam)]

    colocar_barcos(tablero_oculto1, flota)
    colocar_barcos(tablero_oculto2, flota)

    turno = moneda

    while True:

        if turno == jugador1:
            print(f"\n Turno de {jugador1}")
            mostrarTablero(tablero_visible2)

            try:
                fila = int(input(f"{jugador1} Introduce la primera coordenada:(0, {tam-1}) "))
                columna = int(input(f"{jugador1}Introduce la primera coordenada:(0, {tam-1}) "))
            except ValueError:
                print("Entrada inválida, escoge otra.")
                continue

            if fila < 0 or fila >= tam or columna < 0 or columna >= tam:
                print("Fuera del tablero")
                continue
            #Realizamos el disparo para actualizar el tablero visible

            disparar(tablero_visible2, tablero_oculto2, fila, columna)
            mostrarTablero(tablero_visible2)

            if not quedan_barcos(tablero_oculto2):
                print(f"{jugador1} ha ganado la partida") 
                break

            turno = jugador2   

        else:
            print(f"\n Turno de {jugador2}")
            mostrarTablero(tablero_visible1)

            try:
                fila = int(input(f"{jugador2} Introduce la primera coordenada:(0, {tam-1}) "))
                columna = int(input(f"{jugador2}Introduce la primera coordenada:(0, {tam-1}) "))
            except ValueError:
                print("Entrada inválida, escoge otra.")
                continue

            if fila < 0 or fila >= tam or columna < 0 or columna >= tam:
                print("Fuera del tablero")
                continue
            #Realizamos el disparo para actualizar el tablero visible

            disparar(tablero_visible1, tablero_oculto1, fila, columna)
            mostrarTablero(tablero_visible1)

            if not quedan_barcos(tablero_oculto1):
                print(f"{jugador2} ha ganado la partida") 
                break
            turno = jugador1

