from juego import Juego

print('Bienvenido al tateti! \n\nPor: Geronimo Giordano\n')
jug1_nombre = input("Cual es el nombre del jugador 1? \n")
jug2_nombre = input("Cual es el nombre del jugador 2? \n")
ficha1 = 'x'
ficha2 = 'o'
tateti = Juego(jug1_nombre, jug2_nombre, ficha1, ficha2)
print(f'{tateti.jugador1.get_nombre()} es x, {tateti.jugador2.get_nombre()} es o.')
ganador = ''
while ganador == '':
    tateti.tablero.mostrar_tablero()
    print('Le toca al jugador 1!')
    f = int(input('Ingrese fila: ')) - 1
    c = int(input('Ingrese columna: ')) - 1

    tateti.turno(tateti.jugador1, f, c)
    if tateti.hay_ganador():
        ganador = tateti.jugador1.get_nombre()
        print(f'Gano {ganador}!')
        break 
    tateti.tablero.mostrar_tablero()
    print('Le toca al jugador 2!')
    f = int(input('Ingrese fila: ')) - 1
    c = int(input('Ingrese columna: ')) - 1

    tateti.turno(tateti.jugador2, f, c)
    if tateti.hay_ganador():
        ganador = tateti.jugador2.get_nombre()
        print(f'Gano {ganador}!')
