from core.operations import *


def display_menu():
    print('\nCALCULADORA')
    print('\n1.Suma \n2.Resta \n3.Division \n4.Multiplicación \n5.Potencia \n6.Mostrar historial')


def main():
    results = []
    while True:
        display_menu()
        operation = input('\nElija el tipo de operación = ')
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
