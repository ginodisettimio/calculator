from utils import clear_console

results = []

def addition():
    clear_console()
    try:
        number1 = float(input('Ingrese primer operando = '))
        number2 = float(input('Ingrese segundo operando = '))
        result = (f'{number1} + {number2} = {number1*number2}')
        results.append(result)
        return print(f'{result}')
    except ValueError:
        print('Numero invalido')


def subtraction():
    clear_console()
    try:
        number1 = float(input('Ingrese primer operando = '))
        number2 = float(input('Ingrese segundo operando = '))
        result = (f'{number1} - {number2} = {number1-number2}')
        results.append(result)
        return print(f'{result}')
    except ValueError:
        print('Numero invalido')


def division():
    clear_console()
    try:
        number1 = float(input('Ingrese primer operando = '))
        number2 = float(input('Ingrese segundo operando = '))
        result = (f'{number1} / {number2} = {number1/number2}')
        results.append(result)
        return print(f'{result}')
    except ValueError:
        print('Numero invalido')


def multiplication():
    clear_console()
    try:
        number1 = float(input('Ingrese primer operando = '))
        number2 = float(input('Ingrese segundo operando = '))
        result = (f'{number1} * {number2} = {number1*number2}')
        results.append(result)
        return print(f'{result}')
    except ValueError:
        print('Numero invalido')


def power():
    clear_console()
    try:
        number1 = float(input('Ingrese primer operando = '))
        number2 = float(input('Ingrese segundo operando = '))
        result = (f'{number1} ^ {number2} = {number1**number2}')
        results.append(result)
        return print(f'{result}')
    except ValueError:
        print('Numero invalido')


def history():
    clear_console()
    if not results:
        return (print('No se han realizado operaciones'))
    else:
        print('Operaciones realizadas:')
        for result in results:
            print(result)
