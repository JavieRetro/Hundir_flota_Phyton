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
#Ofrecemos al usuario elegir cual opción desea jugar
print("1. Un jugador")
print("2. Dos jugadores")

modo = int(input("Elige el modo de juego(1, 2): "))
#Al elegir un modo, validamos que la opción sea correcta
while modo not in [1, 2]:
    modo = int(input("Opción inválida. Escoge 1 o 2: "))

#--------------------------
# TAMAÑO DEL TABLERO
#--------------------------
#Pedimos el tamaño para el tablero, solo 8x8 o 10x10
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
    #Tanto el agua " " como los barcos con letras
    tablero_oculto = [[" " for _ in range(tam)] for _ in range(tam)]

    #Colocamos los barcos dentro del tablero oculto aleatoriamente 
    colocar_barcos(tablero_oculto, flota)

    #----------------
    #Bucle principal
    #----------------
    #Mientras quedan barcos por hundir en el tablero oculto...
    while quedan_barcos(tablero_oculto):

        #El tablero visible sigue siendo el unico que se muestra
        mostrarTablero(tablero_visible)

        #Establecemos las coordenadas del disparo
        try:
            fila = int(input(f" Introduce la primera coordenada:(0, {tam-1})"))
            columna = int(input(f"Introduce la primera coordenada: Columna: (0, {tam-1})"))
        except ValueError:
            #Si introducimos algo que no sea un numero, tenemos establecido un control de errores
            print("Entrada inválida, escoge otra.")
            continue
        #Comprobamos si las coordenadas están dentro del tablero
        if fila < 0 or fila >= tam or columna < 0 or columna >= tam:
            print("Fuera del tablero")
            continue
        #Realizamos el disparo para actualizar los tableros
        disparar(tablero_visible, tablero_oculto, fila, columna)

    #---------------------------
    #Final del juego(1 Jugador)
    #---------------------------
    print("Enhorabuena,hundiste toda la flota")
    print("Tablero completo: ")

    #Cuando acabamos la partida, revelamos todo el tablero
    for i in range(tam):
        for j in range(tam):
            if tablero_oculto[i][j] == " ":
                tablero_visible[i][j] = Agua
            elif tablero_oculto[i][j] in ["P","B","S","C","L"]:
                tablero_visible[i][j] = Hundido
    #Mostramos el tablero final completo        
    mostrarTablero(tablero_visible)

#--------------------------------
#MODO 2 JUGADORES
#--------------------------------
else:
    #Establecemos los datos de los jugadores    
    jugador1 = input("Nombre del jugador 1: ")
    jugador2 = input("Nombre del jugador 2: ")

    #La moneda decide solo quien empieza la partida
    moneda = random.choice([jugador1, jugador2])

    print(f"La moneda decide que empieza {moneda}")

    #Creamos los tableros para el jugador 1....
    tablero_visible1 = [[Oculto for _ in range(tam)]for _ in range(tam)]
    tablero_oculto1 = [[" " for _ in range(tam)]for _ in range(tam)]

    #Y para el jugador 2
    tablero_visible2 = [[Oculto for _ in range(tam)]for _ in range(tam)]
    tablero_oculto2 = [[" " for _ in range(tam)]for _ in range(tam)]

    #Colocamos los barcos en ambos tableros ocultos
    colocar_barcos(tablero_oculto1, flota)
    colocar_barcos(tablero_oculto2, flota)

    #La moneda elige quien empieza
    turno = moneda


    #----------------
    #Bucle principal
    #----------------
    while True:
        
        # -----------------------------
        # TURNO DEL JUGADOR 1
        # -----------------------------
        if turno == jugador1:
            print(f"\n Turno de {jugador1}")
            #El jugador 1 ve el tablero visible del jugador 2
            mostrarTablero(tablero_visible2)
            
            #Elige las coordenadas del disparo
            try:
                fila = int(input(f"{jugador1} Introduce la primera coordenada:(0, {tam-1}) "))
                columna = int(input(f"{jugador1}Introduce la primera coordenada:(0, {tam-1}) "))
            except ValueError:
                print("Entrada inválida, escoge otra.")
                continue

            if fila < 0 or fila >= tam or columna < 0 or columna >= tam:
                print("Fuera del tablero")
                continue
           
            #Realiza el disparo al tablero del jugador 2 
            disparar(tablero_visible2, tablero_oculto2, fila, columna)

            #Se muestra el tablero tras el disparo
            mostrarTablero(tablero_visible2)

            #Comprobamos si el jugador 1 al final gana
            if not quedan_barcos(tablero_oculto2):
                print(f"{jugador1} ha ganado la partida") 
                break
            #Cambiamos de turno
            turno = jugador2

        # -----------------------------
        # TURNO DEL JUGADOR 2
        # -----------------------------
        else:
            print(f"\n Turno de {jugador2}")

            #El jugador 2 ve el tablero visible del jugador 1
            mostrarTablero(tablero_visible1)

            #Elige las coordenadas del disparo
            try:
                fila = int(input(f"{jugador2} Introduce la primera coordenada:(0, {tam-1}) "))
                columna = int(input(f"{jugador2}Introduce la primera coordenada:(0, {tam-1}) "))
            except ValueError:
                print("Entrada inválida, escoge otra.")
                continue

            if fila < 0 or fila >= tam or columna < 0 or columna >= tam:
                print("Fuera del tablero")
                continue

            #Realiza el disparo al tablero del jugador 1
            disparar(tablero_visible1, tablero_oculto1, fila, columna)

            # Se muestra el tablero tras el disparo
            mostrarTablero(tablero_visible1)

            # Comprobamos si el jugador 2 ha ganado
            if not quedan_barcos(tablero_oculto1):
                print(f"{jugador2} ha ganado la partida") 
                break
            #Cambio de turno
            turno = jugador1

