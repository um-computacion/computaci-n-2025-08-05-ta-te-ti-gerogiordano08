class PosOcupadaExcep(Exception):
    ...
class Tablero:
    def __init__(self):
        self.contenedor = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    def lugar_vacio(self, fila:int, columna:int):
        if self.contenedor[fila][columna] != ' ':
            return False
        else:
            return True
    def poner_ficha(self, ficha:str, fila:int, columna:int):
        if self.lugar_vacio(fila, columna):
            self.contenedor[fila][columna] = ficha
        else:
            raise PosOcupadaExcep('La posición elegida esta ocupada!!')
    def mostrar_tablero(self):
        print(f'{'|'.join(self.contenedor[0])}\n{'|'.join(self.contenedor[1])}\n{'|'.join(self.contenedor[2])}')
#tab = Tablero()
#tab.poner_ficha('x', 0, 0)
#tab.mostrar_tablero()