class Jugador:
    def __init__(self, ficha, nombre):
        self.__ficha__ = ficha
        self.__nombre__ = nombre
    def get_nombre(self):
        return self.__nombre__
    def get_ficha(self):
        return self.__ficha__