from termcolor import colored

from core.operations import *
from helpers.file_helpers import read_json_file
from config import constants
from helpers.console_helpers import clear_console


def display_menu():
    print(colored('\nCALCULADORA', 'yellow'))
    print(colored('\n1.Suma \n2.Resta \n3.Division \n4.Multiplicación \n5.Potencia \n6.Mostrar historial', "light_cyan"))


def main():
    results = read_json_file(constants.OPERATIONS_PATH)
    clear_console()
    while True:
        display_menu()
        operation = input(colored('\nElija el tipo de operación = ', "green"))
        match operation:
            case '1': addition(results)
            case '2': subtraction(results)
            case '3': division(results)
            case '4': multiplication(results)
            case '5': power(results)
            case '6': history(results)
            case _: break


if __name__ == '__main__':
    main()
