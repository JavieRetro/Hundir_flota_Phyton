from funciones_flota import(
    flota,
    Agua,
    mostrarTablero,
    colocar_barcos,
    comprobar_barcos_hundidos,
    disparar
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