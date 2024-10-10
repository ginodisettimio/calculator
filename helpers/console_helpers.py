import os
from termcolor import cprint


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def display_menu():
    cprint('\nCALCULADORA', 'yellow')
    cprint('\n1.Suma \n2.Resta \n3.Division \n4.Multiplicación \n5.Potencia \n6.Mostrar historial \n7.Borrar historial', "light_cyan")
