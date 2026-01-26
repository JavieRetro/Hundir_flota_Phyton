import random

#----------------------
# CONSTANTES DEL JUEGO
#----------------------
Agua = "🌊"
Tocado = "🔥"
Hundido = "☠️"
Oculto = "⬜"

#-------------------
# FLOTA
#-------------------
#Cada barco va definido por su letra y su tamaño
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
#Mostramos un tablero con coordenadas en pantalla
def mostrarTablero(tablero):
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

#-------------------------------
# COLOCACION ALEATORIA DE BARCOS
#-------------------------------
#Colocamos todos los barcos en el tablero oculto
def colocar_barcos(tablero, flota):

    n = len(tablero)
    #Recorremos cada barco de la flota
    for nombre in flota:
        letra, tamaño = flota[nombre]
        colocado = False

        #Metodo while con el cuál buscamos colocar cada barco aleatoriamente
        while not colocado:
            #Elegimos su orientación de forma aleatoria
            orientacion = random.choice(["H", "V"])
            #Y su posición inicial
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
                #Si hay espacio libre en el tablero, colocamos el barco
                if espacio_libre:
                    for i in range(tamaño):
                        tablero[fila][columna + i] = letra
                    colocado = True

            #-----------------------
            # COLOCACIÓN VERTICAL
            #----------------------- 
            elif orientacion == "V" and fila + tamaño <= n:
                espacio_libre = True 

                #Comprobamos si las casillas del tablero estan libre
                for i in range(tamaño):
                    if tablero[fila + i][columna] != " ":
                        espacio_libre = False 
                        break

                #Si hay espacio libre en el tablero, colocamos el barco
                if espacio_libre:
                    for i in range(tamaño):
                        tablero[fila + i][columna] = letra
                    colocado = True


#---------------------
# NOMBRE DEL BARCO
#---------------------
#Devuelve el nombre a partir de su letra
def nombre_barco(letra):
    #Recorremos la flota hasta encontrar la flota que corresponde.
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
    #Si la letra sigue sin aparecer, 
    #es que se ha hundido   
    return True

# ------------------
# MOVIMIENTO(DISPARO)
#--------------------
def disparar(tablero_visible, tablero_oculto, fila, columna):

    #Si la casilla no esta en oculto, significa que ya disparamos ahí antes
    if tablero_visible[fila][columna] != Oculto:
        print("Ya disparaste a esa posicion, prueba otra.")
        return

    #En el tablero oculto el contenido de la casilla    
    contenido = tablero_oculto[fila][columna]

    #------------------
    # DISPARO AL BARCO
    #------------------
    if contenido != " ":
        #Marcamos la casilla como tocada en ambos tableros
        tablero_visible[fila][columna] = Tocado
        tablero_oculto[fila][columna] = Tocado
        nombre = nombre_barco(contenido)
        print(f"{nombre} tocado.")

        #Si tras el disparo no quedan partes sin dar, el barco se considera hundido
        if comprobar_barcos_hundidos(tablero_oculto, contenido):
            print(f"☠️{nombre} hundido")
            #Marcamos a nivel visual en el tablero visible las partes del barco hundidas
            marcar_hundido(tablero_visible)

    #-----------------
    # DISPARO AL AGUA
    #-----------------
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
# Comprobamos si quedan barcos sin hundir buscando en el 
#tablero oculto las letras
def quedan_barcos(tablero):
    for fila in tablero:
        for letra in ["P", "B", "S", "C", "L"]:
            if letra in fila:
                #True si aun quedan barcos
                return True
    #False si todos se hundieron        
    return False   