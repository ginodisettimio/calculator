from termcolor import cprint, colored

from helpers.console_helpers import clear_console
from helpers.file_helpers import write_json_file
from config import constants


def addition(results):
    clear_console()
    try:
        number1 = float(input(colored('Ingrese primer operando = ', "blue")))
        number2 = float(
            input(colored('Ingrese segundo operando = ', "light_red")))
        result = (f'{number1} + {number2} = {number1*number2}')
        results.append(result)
        write_json_file(constants.OPERATIONS_PATH, results)
        return cprint(f'{result}', "magenta")
    except ValueError:
        print('Numero invalido')


def subtraction(results):
    clear_console()
    try:
        number1 = float(input(colored('Ingrese primer operando = ', "blue")))
        number2 = float(
            input(colored('Ingrese segundo operando = ', "light_red")))
        result = (f'{number1} - {number2} = {number1-number2}')
        results.append(result)
        write_json_file(constants.OPERATIONS_PATH, results)
        return cprint(f'{result}', "magenta")
    except ValueError:
        print('Numero invalido')


def division(results):
    clear_console()
    try:
        number1 = float(input(colored('Ingrese primer operando = ', "blue")))
        number2 = float(
            input(colored('Ingrese segundo operando = ', "light_red")))
        result = (f'{number1} / {number2} = {number1/number2}')
        results.append(result)
        write_json_file(constants.OPERATIONS_PATH, results)
        return cprint(f'{result}', "magenta")
    except ValueError:
        print('Numero invalido')


def multiplication(results):
    clear_console()
    try:
        number1 = float(input(colored('Ingrese primer operando = ', "blue")))
        number2 = float(
            input(colored('Ingrese segundo operando = ', "light_red")))
        result = (f'{number1} * {number2} = {number1*number2}')
        results.append(result)
        write_json_file(constants.OPERATIONS_PATH, results)
        return cprint(f'{result}', "magenta")
    except ValueError:
        print('Numero invalido')


def power(results):
    clear_console()
    try:
        number1 = float(input(colored('Ingrese primer operando = ', "blue")))
        number2 = float(
            input(colored('Ingrese segundo operando = ', "light_red")))
        result = (f'{number1} ^ {number2} = {number1**number2}')
        results.append(result)
        write_json_file(constants.OPERATIONS_PATH, results)
        return cprint(f'{result}', "magenta")
    except ValueError:
        print('Numero invalido')
    except OverflowError:
        print('Entrada invalida')


def history(results):
    clear_console()
    if not results:
        return (print('No se han realizado operaciones'))
    else:
        cprint('Operaciones realizadas:', "black", "on_yellow")
        for result in results:
            print(result)


_all__ = [addition, subtraction, division, multiplication, power, history]
