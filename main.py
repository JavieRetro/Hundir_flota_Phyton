from funciones_flota import(
    flota,
    Agua,
    mostrarTablero,
    colocar_barcos,
    comprobar_barcos_hundidos,
    disparar,
    faltan_barcos
)

print("🌊🚢 HUNDIR LA FLOTA 🚢🌊")

#Tamaño para el tablero

tam = int(input("Introduce un tamaño para el tablero (8 o 10): "))

while tam not in [8, 10]:
    tam = int(input("Tamaño inválido, introduce otro(8 o 10): "))

#Creacion de tableros
tablero_visible = [[Agua for _ in range(tam)] for _ in range(tam)]
tablero_oculto = [[" " for _ in range(tam)] for _ in range(tam)]

#Colocamos los barcos dentro del tablero oculto y asi descubrirlos
colocar_barcos(tablero_oculto, flota)

#----------------
#Bucle principal
#----------------

while faltan_barcos(tablero_oculto):
    mostrarTablero(tablero_visible)

    try:
        fila = int(input(f"Fila: (0, {tam-1})"))
        columna = int(input(f"Columna: (0, {tam-1})"))
    except ValueError:
        print("Entrada inválida, escoge otra.")
        continue

    if fila < 0 or fila >= tam or columna < 0 or columna >= tam:
        print("Fuera del tablero")
    
    #Realizamos el disparo para actualizar el tablero visible

    disparar(tablero_visible, tablero_oculto, fila, columna)

#------------------
#Final del juego
#------------------

mostrarTablero(tablero_visible)
print("Enhorabuena,hundiste toda la flota")