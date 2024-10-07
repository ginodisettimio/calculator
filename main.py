from operations import addition, subtraction, division, multiplication, power, history


def display_menu():
    print('\nCALCULADORA')
    print('\n1.Suma \n2.Resta \n3.Division \n4.Multiplicación \n5.Potencia \n6.Mostrar historial')


def main():
    results = [] 
    while True:
        display_menu()
        operation = input('\nElija el tipo de operación = ')
        match operation:
            case '1': addition()
            case '2': subtraction()
            case '3': division()
            case '4': multiplication()
            case '5': power()
            case '6': history()
            case _: break


if __name__ == '__main__':
    main()
