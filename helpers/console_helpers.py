import os
from termcolor import cprint


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def display_menu():
    cprint('\nCALCULADORA', 'yellow')
    cprint('\n1.Operaciones aritmeticas \n2.Conversor de unidades \n3.Mostrar historial \n4.Borrar historial \n5.Actualizar cuenta \n0.Salir', "light_cyan")


def display_arithmetics():
    cprint('\n1.Suma \n2.Resta \n3.División \n4.Multiplicación \n5.Potencia \n0.Volver', 'light_yellow')


def display_conversor():
    cprint('\n1.Fahrenheit \n2.Celsius \n3.Kelvin \n0.Volver', 'light_yellow')
