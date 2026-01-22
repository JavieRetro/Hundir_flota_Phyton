import random

Agua = "🌊"
Tocado = "🔥"
Hundido = "☠️"
Barco = "B"

flota = {
    "portaaviones": 5,
    "buque": 4,
    "submarino": 3,
    "Crucero": 2,
    "Lancha": 1
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
        tamaño = flota[nombre]
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
                        tablero[fila][columna + i] = Barco
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
                        tablero[fila + i][columna] = Barco
                colocado = True


#-------------------
# COMPROBAMOS HUNDIMIENTO
#-------------------
def comprobar_barcos_hundidos(tablero_oculto, fila, columna):

    n = len(tablero_oculto)

    # Revisamos partes del barco que queden por hundr
    for i in range(n):
        for j in range(n):
            if tablero_oculto[i][j] == Barco:
                return False
    return True

# ------------------
# MOVIMIENTO(DISPARO)
#--------------------
def disparar(tablero_visble, tablero_oculto, fila, columna):

    if tablero_oculto[fila][columna] != Agua:
        