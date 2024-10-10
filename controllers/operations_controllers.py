from models.result import Result
import helpers.console_helpers as console
from termcolor import colored, cprint


class Operations_Controllers:

    @staticmethod
    def plus(number1, number2):
        return number1+number2

    @staticmethod
    def minus(number1, number2):
        return number1-number2

    @staticmethod
    def times(number1, number2):
        return number1*number2

    @staticmethod
    def divided(number1, number2):
        return number1/number2

    @staticmethod
    def to_the_power_of(number1, number2):
        return number1**number2

    @classmethod
    def start(cls):
        console.clear()
        Result.read()
        while True:
            console.display_menu()
            choose = input(colored('\nElija el tipo de operación = ', "green"))
            match choose:
                case '1':
                    cls.addition()
                case '2':
                    cls.subtraction()
                case '3':
                    cls.division()
                case '4':
                    cls.multiplication()
                case '5':
                    cls.power()
                case '6':
                    cls.history()
                case '7':
                    cls.delete_history()
                case _:
                    break

    @classmethod
    def get_numbers(cls):
        try:
            number1 = float(
                input(colored('Ingrese primer operando = ', "blue")))
            number2 = float(
                input(colored('Ingrese segundo operando = ', "light_red")))
            return number1, number2
        except ValueError:
            print('Número inválido')

    @classmethod
    def addition(cls):
        console.clear()
        number1, number2 = cls.get_numbers()
        result = Operations_Controllers.plus(number1, number2)
        count = f'{number1} + {number2} = {result}'
        Result.results.append(count)
        Result.add()
        cprint(f'Resultado: {result}', "magenta")

    @classmethod
    def subtraction(cls):
        console.clear()
        number1, number2 = cls.get_numbers()
        result = Operations_Controllers.minus(number1, number2)
        count = f'{number1} - {number2} = {result}'
        Result.results.append(count)
        Result.add()
        cprint(f'Resultado: {result}', "magenta")

    @classmethod
    def division(cls):
        console.clear()
        number1, number2 = cls.get_numbers()
        result = Operations_Controllers.divided(number1, number2)
        count = f'{number1} / {number2} = {result}'
        Result.results.append(count)
        Result.add()
        cprint(f'Resultado: {result}', "magenta")

    @classmethod
    def multiplication(cls):
        console.clear()
        number1, number2 = cls.get_numbers()
        result = Operations_Controllers.times(number1, number2)
        count = f'{number1} * {number2} = {result}'
        Result.results.append(count)
        Result.add()
        cprint(f'Resultado: {result}', "magenta")

    @classmethod
    def power(cls):
        console.clear()
        number1, number2 = cls.get_numbers()
        result = Operations_Controllers.to_the_power_of(number1, number2)
        count = f'{number1} ^ {number2} = {result}'
        Result.results.append(count)
        Result.add()
        cprint(f'Resultado: {result}', "magenta")

    @classmethod
    def history(cls):
        console.clear()
        Result.read()
        if not Result.results:
            print('No se han realizado operaciones')
        else:
            cprint('Operaciones realizadas:', "black", "on_yellow")
            for result in Result.results:
                print(result)

    @classmethod
    def delete_history(cls):
        console.clear()
        Result.delete()
