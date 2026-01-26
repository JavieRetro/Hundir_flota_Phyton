import random

Agua = "🌊"
Tocado = "🔥"
Hundido = "☠️"

flota = {
    "Portaaviones": ("P", 5),
    "buque": ("B", 4),
    "submarino": ("S", 3),
    "Crucero": ("C", 2),
    "Lancha": ("L", 1)
}

# ====================
# CREAR TABLERO
# ====================

#Variable donde introducimos el tamaño de nuestro tablero
tam = int(input("Introduce el tamaño del tablero(8 y 10): "))
while tam not in [8,10]:
    tam = int(input("Tamaño inválido, escoge otro(8, 10)"))

#Creamos un tablero con las dimensiones de tam
tablero= [[" " for i in range(tam)]for i in range(tam)]

# ====================
# MOSTRAR TABLERO
# ====================

def mostrarTablero(tablero):
     # Línea en blanco para separar visualmente el tablero del texto anterior
    n = len(tablero)

    print()
    print("  ", end="")
    for i in range(n):
        print(f"{i:^3}|", end="")
    print("")
    print(" " + "-" * (n * 4))

    for i in range(n):
        print(i, end="")
        for j in tablero[i]:
            print(f"{j:^3}|", end="")
        print("")
        print(" " + "-" * (n * 4))
    print()

mostrarTablero(tablero)

def colocar_barcos(tablero, flota):

    n = len(tablero)
    #Recorremos cada barco de la flota
    for nombre in flota:
        letra = flota[nombre][0]
        tamaño = flota[nombre][1]
        colocado = False

    #Metodo while con el cuál buscamos colocar cada barco
        while not colocado:

            orientacion = random.choices(["Horizontal", "Vertical"])
            fila = random.randint(0, n-1)
            columna = random.randint(0, n-1)

#-----------------------
# COLOCACIÓN HORIZONTAL
#------------------------  
            if orientacion == "Horizontal" and columna + tamaño <= n:
                espacio_libre = True 

                #Comprobamos si las casillas del tablero estan libre
                for i in range(tamaño):

                    if tablero[fila][columna +i] != " ":
                        espacio_libre = False 
        
                if espacio_libre:
                    for i in range(tamaño):
                        tablero[fila][columna + i] = letra
                    colocado = True

#-----------------------
# COLOCACIÓN VERTICAL
#------------------------  

            elif orientacion == "Vertical" and fila + tamaño <= n:
                espacio_libre = True 

                #Comprobamos si las casillas del tablero estan libre
                for i in range(tamaño):

                    if tablero[fila + i][columna] != " ":
                        espacio_libre = False 
        
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
def disparar(tablero_visble, tablero_oculto, fila, columna):

    #Repetir casilla de disparo
    if tablero_visble[fila][columna] == [Agua, Tocado, Hundido]:
        print("Ya disparaste a esa posicion, prueba otra.")
        return
    
    #Barco tocado
    if tablero_oculto[fila][columna] != " ":
        tablero_visble[fila][columna] = Tocado
        tablero_oculto[fila][columna] = Tocado
        nombre = nombre.barco(tablero_oculto[fila][columna])
        print(f"{nombre} tocado.")
        