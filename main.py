from funciones_flota import(
    flota,
    Agua,
    Hundido,
    Oculto,
    mostrarTablero,
    colocar_barcos,
    comprobar_barcos_hundidos,
    disparar,
    quedan_barcos
)

print("🌊🚢 HUNDIR LA FLOTA 🚢🌊")

#Pedimos el tamaño para el tablero

tam = int(input("Introduce un tamaño para el tablero (8 o 10): "))

#Validación del tamaño si es correcto o no
while tam not in [8, 10]:
    tam = int(input("Tamaño inválido, introduce otro(8 o 10): "))

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
