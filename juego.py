from jugador import Jugador
from tablero import Tablero
class Juego:
    def __init__(self, nombre1:str, nombre2:str, ficha1:str, ficha2:str):
        self.tablero = Tablero()
        self.jugador1 = Jugador(ficha1, nombre1)
        self.jugador2 = Jugador(ficha2, nombre2)
    def turno(self, jugador:Jugador, fila:int, columna:int):
        self.tablero.poner_ficha(jugador.get_ficha(), fila, columna)
        self.tablero.mostrar_tablero()
    def hay_ganador(self):
        tab = self.tablero.contenedor
        # filas (ok)
        for fila in tab:
            if fila[0] != ' ' and fila[0] == fila[1] == fila[2]:
                return fila[0]
        # diagonales (ok)
        if tab[1][1] != ' ':
            if tab[0][0] == tab[1][1] == tab[2][2] or tab[0][2] == tab[1][1] == tab[2][0]:
                return tab[1][1]
        # columnas (ok)
        for col in range(3): 
            if tab[0][col] != ' ' and tab[0][col] == tab[1][col] == tab[2][col]:
                return tab[0][col]
tateti = Juego('ju1', 'ju2', 'x', 'o')
tateti.turno(tateti.jugador1, 0, 0)
#tateti.turno(tateti.jugador2, 1, 1)
#tateti.turno(tateti.jugador2, 2, 2)
print(tateti.hay_ganador())
