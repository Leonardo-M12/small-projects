#Código para cruz y cero con contador.
import sys

the_Board = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '} #El tablero de juego.

test_board = {'1': '1', '2': '2', '3': '3',
            '4': '4', '5': '5', '6': '6',
            '7': '7', '8': '8', '9': '9'} #Tablero de prueba para mostrar posiciones.

turn = 'X'
count = 1

def print_board(Board): #Mostrar el tablero.
    print()
    print(Board['1'] + '|' + Board['2'] + '|' + Board['3'])
    print('-+-+-')
    print(Board['4'] + '|' + Board['5'] + '|' + Board['6'])
    print('-+-+-')
    print(Board['7'] + '|' + Board['8'] + '|' + Board['9'])
    print()

#Sistema de juego principal. Ir ajustando.
def game():
    global turn
    global move
    global count

    while True: #Bucle principal del juego.
        #Bienvenida e indicaciones.
        print("¡Bienvenidos a cruz y cero!")
        print("El jugador 1 usará las X y el jugador 2, las O.\n")
        print("""En su turno, cada jugador debe seleccionar una posición, escribiendo
el número correspondiente a dicha posición. Los números que corresponden
a cada posición se encuentran en el siguiente tablero:""")
        print_board(test_board) #Mostrar el tablero de prueba.
        print("¡Que inicie el juego!")

        #Iniciar juego.
        while True:
            if count == 10:
                print("Empate. El juego ha acabado.")
                break

            if turn == 'X': #Turno de X.
                print("Turno de X.")
                validate_input()

                the_Board[move] = 'X' #Actualizar tablero.
                print_board(the_Board) #Mostrar tablero actualizado.

                validate_winner() #Ver si hay ganador.

                if validate_winner() == 'X':
                    print("X ha ganado.")
                    break #Ver qué pasa cuando el juego acaba.
                else:
                    turn = 'O'
                    count += 1
                    continue

            else:
                print("Turno de O.")
                validate_input()

                the_Board[move] = 'O' #Actualizar tablero.
                print_board(the_Board) #Mostrar tablero actualizado.

                validate_winner()
                if validate_winner() == 'O':
                    print("O ha ganado.")
                    break #Ver qué pasa cuando el juego acaba.
                else:
                    turn = 'X'
                    count += 1
                    continue
                
        #Ver qué pasa tras el juego.
        print("¿Jugar de nuevo? Escribe 0 para salir o 1 para jugar de nuevo.")
        #Validación de respuesta.
        while True:
            query = input("> ")
            if query not in {"0", "1"}:
                print("Escribe 0 o 1.")
                continue
            else:
                break
        #Análisis de opciones.    
        if query == '0':
            sys.exit() #Salir del juego.
        else:
            for key in the_Board.keys():
                the_Board[key] = ' ' #Resetear tablero
                count = 1 #Resetear contador
            continue



#Validación de entrada.
def validate_input():
    global move
    
    while True:    
        move = input("Selecciona una posición: ")
        if the_Board.get(move, 0) == 0: #Si el usuario escribe algo no válido, esto le friega el intento de buguear.
            print("Escribe un número correspondiente a una posición válida.")
            continue
        elif the_Board[move] != ' ':
            print("Posición ya ocupada.")
            continue
        else:
            break #Aquí la variable move ya fue creada.

        

#Validación de ganador.
def validate_winner():
    global turn

    if the_Board['1'] == the_Board['2'] == the_Board['3'] != ' ': #Horizontales
        return turn
    elif the_Board['4'] == the_Board['5'] == the_Board['6'] != ' ':
        return turn
    elif the_Board['7'] == the_Board['8'] == the_Board['9'] != ' ':
        return turn
    elif the_Board['1'] == the_Board['4'] == the_Board['7'] != ' ': #Verticales
        return turn
    elif the_Board['2'] == the_Board['5'] == the_Board['8'] != ' ':
        return turn
    elif the_Board['3'] == the_Board['6'] == the_Board['9'] != ' ':
        return turn
    elif the_Board['1'] == the_Board['5'] == the_Board['9'] != ' ': #Diagonales
        return turn    
    elif the_Board['3'] == the_Board['5'] == the_Board['7'] != ' ':
        return turn


if __name__ == '__main__':
    game()