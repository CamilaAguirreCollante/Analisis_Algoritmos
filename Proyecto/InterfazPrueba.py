"""
    Autores: 
        María Camila Aguirre Collante
        Jessica Tatiana Naizaque Guevara
"""
import copy
from operator import truediv
from tabnanny import check
from colorama import *
#from termcolor import colored, cprint

init(autoreset=True)
#definir colores que serán usados
yellow = Back.YELLOW
blue = Back.BLUE
red = Back.RED
green = Back.GREEN
cyan = Back.CYAN
purple = Back.MAGENTA
white = Back.WHITE

'''
@Entradas -> dim=dimensiones del tablero de juego
@Salida -> creación del tablero de juego
'''
def createBoard(dim):
    board = []
    for i in range(dim):
        board.append([])
        for j in range(dim):
            board[i].append(0)
        #end-for
    #end-for
    return initialBoard(board)
#end-def

'''
@Entradas -> tablero de juego
@Salida -> ubica los colores iniciales
'''
def initialBoard(board):
    boardTemp = copy.deepcopy(board)
    dim = len(boardTemp)
    if dim == 5:
        boardTemp[0][0] = "R!"
        boardTemp[4][1] = "R!"
        boardTemp[0][2] = "G!"
        boardTemp[3][1] = "G!"
        boardTemp[1][2] = "B!"
        boardTemp[4][2] = "B!"
        boardTemp[3][3] = "Y!"
        boardTemp[0][4] = "Y!"
        boardTemp[4][3] = "W!"
        boardTemp[1][4] = "W!"
    elif dim == 6:
        boardTemp[0][0] = "G!"
        boardTemp[4][0] = "G!"
        boardTemp[5][0] = "Y!"
        boardTemp[0][1] = "Y!"
        boardTemp[0][2] = "C!"
        boardTemp[2][2] = "C!"
        boardTemp[0][4] = "R!"
        boardTemp[3][2] = "R!"
        boardTemp[1][4] = "W!"
        boardTemp[4][2] = "W!"
        boardTemp[0][5] = "B!"
        boardTemp[5][2] = "B!"
    for i in range(len(boardTemp)):
        for j in range(len(boardTemp)):
            if boardTemp[i][j] == 0:
                boardTemp[i][j] = "0"
            #end-if
        #end-for
    #end-for
    return boardTemp

def showBoard(board):
    boardTemp = copy.deepcopy(board)
    print("-"*(7 * len(boardTemp)+1))
    for i in range(len(boardTemp)):
        for j in range(len(boardTemp)):
            if boardTemp[i][j] == "R" or boardTemp[i][j] == "R!":
                boardTemp[i][j]= str(i)+str(j)
                print("| ", end = "")
                print(red + " {:3}".format(boardTemp[i][j]), end = " ")
            elif boardTemp[i][j] == "G" or boardTemp[i][j] == "G!":
                boardTemp[i][j]= str(i)+str(j)
                print("| ", end = "")
                print(green + " {:3}".format(boardTemp[i][j]), end = " ")
            elif boardTemp[i][j] == "B" or boardTemp[i][j] == "B!":
                boardTemp[i][j]=str(i)+str(j)
                print("| ", end = "")
                print(blue + " {:3}".format(boardTemp[i][j]), end = " ")
            elif boardTemp[i][j] == "Y" or boardTemp[i][j] == "Y!":
                boardTemp[i][j]=str(i)+str(j)
                print("| ", end = "")
                print(yellow + " {:3}".format(boardTemp[i][j]), end = " ")
            elif boardTemp[i][j] == "W" or boardTemp[i][j] == "W!":
                boardTemp[i][j]=str(i)+str(j)
                print("| ", end = "")
                print(white + " {:3}".format(boardTemp[i][j]), end = " ")
            elif boardTemp[i][j] == "C" or boardTemp[i][j] == "C!":
                boardTemp[i][j]=str(i)+str(j)
                print("| ", end = "")
                print(cyan + " {:3}".format(boardTemp[i][j]), end = " ")
            elif boardTemp[i][j] == "P" or boardTemp[i][j] == "P!":
                boardTemp[i][j]=str(i)+str(j)
                print("| ", end = "")
                print(purple + " {:3}".format(boardTemp[i][j]), end = " ")
            else:
                boardTemp[i][j]=str(i)+str(j)
                print("| ", end = "")
                print(Back.BLACK + " {:3}".format(boardTemp[i][j]), end = " ")
                #print("| {:4}".format(boardTemp[i][j]), end = " ")
        #end-for
        print("|")
        print("-"*(7 * len(boardTemp)+1))
    #end-for
#end-def

def checkFinished(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "0":
                return False    
            #end if
        #end for
    #end for
    return True
#end def

def checkBox(board, color, coordenate):
    i = int(coordenate[0])
    j = int(coordenate[1])
    n = len(board)
    if board[i][j] == "0":
        if i > 0:
            if board[i-1][j] == color or board[i-1][j] == color+"!": #Si su casilla de arriba es del mismo color
                return True
            #end if
        #end if
        if j > 0:
            if board[i][j-1] == color or board[i][j-1] == color+"!": #Si su casilla izquierda es del mismo color
                return True
            #end if
        #end if
        if i < n-1:
            if board[i+1][j] == color or board[i+1][j] == color+"!": #Si su casilla de abajo es del mismo color
                return True
            #end if
        #end if
        if j < n-1:
            if board[i][j+1] == color or board[i][j+1] == color+"!": #Si su casilla derecha es del mismo color
                return True
            #end if
        #end if
        print("******No hay casillas adyacentes del color seleccionado.\n")
    elif "!" not in board[i][j]:
        return True
    #end if
    if "!" in board[i][j]:
        print("******No puede cambiar una casilla inicial.\n")
    #end if
    return False
#end def


def selectMove(board):
    finished = False #Verificar que el juego no haya finalizado (cuando todas las casillas tienen color)
    while not finished:
        parameters = False #Verificar que los parámetros estén correctos y que haya seleccionado una casilla correcta
        while not parameters:
            print("Recuerde que los colores son:  ", red + " {:4}".format("Red"), green + " {:6}".format("Green"), blue + " {:5}".format("Blue"), yellow + " {:7}".format("Yellow"), white + " {:6}".format("White"), cyan + " {:5}".format("Cyan"), purple + " {:7}".format("Purple"))
            move = str(input("Digite la inicial del color que desea utilizar y la casilla que desea jugar (Ej: R 34): "))
            movements = move.split()
            if len(movements) == 2:
                if movements[0].isalpha():
                    if movements[1].isnumeric():
                        if movements[0].upper() == "R" or movements[0].upper() == "G" or movements[0].upper() == "B" or movements[0].upper() == "Y" or movements[0].upper() == "W" or movements[0].upper() == "C" or movements[0].upper() == "P": 
                            if len(movements[1])  == 2:
                                if int(movements[1][0]) >= 0 and int(movements[1][0]) < len(board) and int(movements[1][1]) >= 0 and int(movements[1][0]) < len(board):
                                    parameters = checkBox(board, movements[0].upper(), movements[1])
                                else:
                                    print("******Número de casilla incorrecta.\n")
                                #end if
                            else:
                                print("******Número de casilla incorrecta.\n")
                            #end if
                        else:
                            print("******Inicial de color inválida.\n")
                        #end if
                    else:
                        print ("******Parámetro casilla incorrecto.\n")
                    #end if
                else:
                    print ("******Parámetro color incorrecto.\n")
                #end if
            else:
                print("******Cantidad de parámetros enviados incorrecta.\n")
            #end if
        #end while
        board[int(movements[1][0])][int(movements[1][1])] = movements[0].upper()
        showBoard(board)
        finished = checkFinished(board)
        print(finished)
    #end while
#end def