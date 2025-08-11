class PosOcupadaExcep(Exception):
    ...
class Tablero:
    def __init__(self):
        self.contenedor = [['', '', ''], ['', '', ''], ['', '', '']]
    def lugar_vacio(self, fila, columna):
        if self.contenedor[fila[columna]] != '':
            return False
    def poner_ficha(self, ficha, fila, columna):
        if self.lugar_vacio(fila, columna):
            self.contenedor[fila[columna]] = ficha
        else:
            PosOcupadaExcep('La posición elegida esta ocupada!!')
