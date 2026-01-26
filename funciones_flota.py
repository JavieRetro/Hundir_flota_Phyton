import random

Agua = "🌊"
Tocado = "🔥"
Hundido = "☠️"
Oculto = "⬜"

flota = {
    "Portaaviones": ("P", 5),
    "buque": ("B", 4),
    "submarino": ("S", 3),
    "Crucero": ("C", 2),
    "Lancha": ("L", 1)
}
# ====================
# MOSTRAR TABLERO
# ====================

def mostrarTablero(tablero):
     # Línea en blanco para separar visualmente el tablero del texto anterior
    n = len(tablero)

    print()
    print("  ", end="")
    for i in range(n):
        print(f"{i:^ 6}|", end="")
    print("")
    print(" " + "-" * (n * 7))

    for i in range(n):
        print(i, end="")
        for j in tablero[i]:
            print(f"{j:^5}|", end="")
        print("")
        print(" " + "-" * (n * 7))
    print()

def colocar_barcos(tablero, flota):

    n = len(tablero)
    #Recorremos cada barco de la flota
    for nombre in flota:
        letra, tamaño = flota[nombre]
        colocado = False

    #Metodo while con el cuál buscamos colocar cada barco
        while not colocado:

            orientacion = random.choice(["H", "V"])
            fila = random.randint(0, n-1)
            columna = random.randint(0, n-1)

#-----------------------
# COLOCACIÓN HORIZONTAL
#------------------------  
            if orientacion == "H" and columna + tamaño <= n:
                espacio_libre = True 

                #Comprobamos si las casillas del tablero estan libre
                for i in range(tamaño):

                    if tablero[fila][columna +i] != " ":
                        espacio_libre = False 
                        break

                if espacio_libre:
                    for i in range(tamaño):
                        tablero[fila][columna + i] = letra
                    colocado = True

#-----------------------
# COLOCACIÓN VERTICAL
#------------------------  

            elif orientacion == "V" and fila + tamaño <= n:
                espacio_libre = True 

                #Comprobamos si las casillas del tablero estan libre
                for i in range(tamaño):

                    if tablero[fila + i][columna] != " ":
                        espacio_libre = False 
                        break

                if espacio_libre:
                    for i in range(tamaño):
                        tablero[fila + i][columna] = letra
                    colocado = True


#---------------------
# NOMBRE DEL BARCO
#---------------------
def nombre_barco(letra):

    for nombre in flota:
        if flota[nombre][0] == letra:
            return nombre 

#-------------------
# COMPROBAMOS HUNDIMIENTO
#-------------------
def comprobar_barcos_hundidos(tablero, letra):

    n = len(tablero)
    # Revisamos partes del barco que queden por hundr
    for fila in tablero:
        if letra in fila:
            return False
    return True

# ------------------
# MOVIMIENTO(DISPARO)
#--------------------
def disparar(tablero_visible, tablero_oculto, fila, columna):

    #Repetir casilla de disparo
    if tablero_visible[fila][columna] != Oculto:
        print("Ya disparaste a esa posicion, prueba otra.")
        return
    
    contenido = tablero_oculto[fila][columna]

    #Barco tocado
    if contenido != " ":
        tablero_visible[fila][columna] = Tocado
        tablero_oculto[fila][columna] = "🔥"
        nombre = nombre_barco(contenido)
        print(f"{nombre} tocado.")

        if comprobar_barcos_hundidos(tablero_oculto, contenido):
            print(f"☠️{nombre} hundido")
            marcar_hundido(tablero_visible)
    else:
        print("🌊 Agua")
        tablero_visible[fila][columna] = Agua

#---------------------
# BARCO HUNDIDO
#---------------------
def marcar_hundido(tablero_visible):
    n = len(tablero_visible)
    for fila in range(n):
        for columna in range(n):
            if tablero_visible[fila][columna] == Tocado:
                tablero_visible[fila][columna] = Hundido

# ====================
# ¿QUEDAN BARCOS?
# ====================
def quedan_barcos(tablero):
    for fila in tablero:
        for letra in ["P", "B", "S", "C", "L"]:
            if letra in fila:
                return True
    return False   