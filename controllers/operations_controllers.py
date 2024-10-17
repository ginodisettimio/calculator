from typing import List

from termcolor import colored, cprint

from models.arithmetic_model import Arithmetic
from models.conversor_model import Conversor
from models.base_model import Base
import helpers.console_helpers as console


class Operations_Controllers:

    @staticmethod
    def get_all_results() -> List[Base]:
        return Conversor.results + Arithmetic.results

    @staticmethod
    def get_numbers():
        try:
            number1 = float(
                input(colored('Ingrese primer operando = ', "blue")))
            number2 = float(
                input(colored('Ingrese segundo operando = ', "light_red")))
            return number1, number2
        except ValueError:
            cprint('Número inválido', 'white', 'on_red')

    @classmethod
    def start(cls):
        console.clear()
        while True:
            console.display_menu()
            choose = input(colored('\nElija una opción = ', "white"))
            match choose:
                case '1':
                    cls.arithmetics_operations()
                case '2':
                    cls.unity_conversor()
                case '3':
                    cls.history()
                case '4':
                    cls.delete_history()
                case '5':
                    cls.update_value()
                case '0':
                    break
                case _:
                    cprint('Opción inválida', 'light_red')

    @classmethod
    def history(cls):
        console.clear()
        Arithmetic.read()
        Conversor.read()
        all_results = cls.get_all_results()
        if not all_results:
            cprint('No se han realizado operaciones', 'black', 'on_yellow')
        else:
            cprint('Operaciones realizadas:', "black", "on_yellow")
            for index, result in enumerate(all_results, start=1):
                print(f'{index}. {result}')

    @classmethod
    def delete_history(cls):
        console.clear()
        Conversor.results.clear()
        Conversor.delete()
        Arithmetic.results.clear()
        Arithmetic.delete()

    @classmethod
    def arithmetics_operations(cls):
        console.clear()
        while True:
            console.display_arithmetics()
            choose = input(colored('\nElija el tipo de operación = ', 'white'))
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
                case '0':
                    console.clear()
                    break
                case _:
                    cprint('Opción inválida', 'light_red')

    @classmethod
    def addition(cls):
        console.clear()
        try:
            number1, number2 = cls.get_numbers()
            result = Arithmetic.plus(number1, number2)
            count = f'{number1} + {number2} = {result}'
            Arithmetic.add_numbers(count, result)
        except TypeError:
            return

    @classmethod
    def subtraction(cls):
        console.clear()
        try:
            number1, number2 = cls.get_numbers()
            result = Arithmetic.minus(number1, number2)
            count = f'{number1} - {number2} = {result}'
            Arithmetic.add_numbers(count, result)
        except TypeError:
            return

    @classmethod
    def division(cls):
        console.clear()
        try:
            number1, number2 = cls.get_numbers()
            result = Arithmetic.divided(number1, number2)
            count = f'{number1} / {number2} = {result}'
            Arithmetic.add_numbers(count, result)
        except TypeError:
            return
        except ZeroDivisionError:
            return cprint('No se puede dividir entre 0 ', 'white', 'on_red')

    @classmethod
    def multiplication(cls):
        console.clear()
        try:
            number1, number2 = cls.get_numbers()
            result = Arithmetic.times(number1, number2)
            count = f'{number1} * {number2} = {result}'
            Arithmetic.add_numbers(count, result)
        except TypeError:
            return

    @classmethod
    def power(cls):
        console.clear()
        try:
            number1, number2 = cls.get_numbers()
            result = Arithmetic.to_the_power_of(number1, number2)
            count = f'{number1} ^ {number2} = {result}'
            Arithmetic.add_numbers(count, result)
        except TypeError:
            return

    @classmethod
    def unity_conversor(cls):
        console.clear()
        while True:
            console.display_conversor()
            choose = input(
                colored('\nElija el tipo de conversión = ', "white"))
            match choose:
                case '1':
                    cls.fahrenheit()
                case '2':
                    cls.celsius()
                case '3':
                    cls.kelvin()
                case '0':
                    console.clear()
                    break
                case _:
                    cprint('Opción inválida', 'light_red')

    @classmethod
    def fahrenheit(cls):
        try:
            number1 = float(input(colored('Ingrese temperatura en Fahrenheit = ', 'light_yellow')))
            convert = input(colored('Elija unidad a convertir: Celsius o Kelvin: ', 'light_blue'))
            result = Conversor.convert_temperature(number1, 'Fahrenheit', convert.title())
            if result is not None:
                count = f'{number1}°Fahrenheit equivale a {result}°{convert.title()}'
                Conversor.add_numbers(count, result)
            else:
                cprint("Unidad no válida. Por favor elija Celsius o Kelvin.", 'white', 'on_light_red')
        except ValueError:
            cprint('Número inválido', 'white', 'on_red')

    @classmethod
    def celsius(cls):
        try:
            number1 = float(input(colored('Ingrese temperatura en Celsius = ', 'light_yellow')))
            convert = input(colored('Elija unidad a convertir: Fahrenheit o Kelvin: ', 'light_blue'))
            result = Conversor.convert_temperature(
                number1, 'Celsius', convert.title())
            if result is not None:
                count = f'{number1}°Celsius equivale a {result}°{convert.title()}'
                Conversor.add_numbers(count, result)
            else:
                cprint("Unidad no válida. Por favor elija Fahrenheit o Kelvin.", 'white', 'on_light_red')
        except ValueError:
            cprint('Número inválido', 'white', 'on_red')

    @classmethod
    def kelvin(cls):
        try:
            number1 = float(input(colored('Ingrese temperatura en Kelvin = ', 'light_yellow')))
            convert = input(colored('Elija unidad a convertir: Celsius o Fahrenheit: ', 'light_blue'))
            result = Conversor.convert_temperature(number1, 'Kelvin', convert.title())
            if result is not None:
                count = f'{number1}°Kelvin equivale a {result}°{convert.title()}'
                Conversor.add_numbers(count, result)
            else:
                cprint("Unidad no válida. Por favor elija Celsius o Fahrenheit.", 'white', 'on_light_red')
        except ValueError:
            cprint('Número inválido', 'white', 'on_red', 'white', 'on_red')

    @staticmethod
    def round_value(result_string, decimal) -> str:
        if "equivale a" in result_string:
            result_value = float(result_string.split('equivale a')[1].strip().split('°')[0])
            rounded_result = round(result_value, decimal)
            return result_string.split('equivale a')[0] + f'equivale a {rounded_result}°'
        else:
            result_value = float(result_string.split('=')[-1].strip())
            rounded_result = round(result_value, decimal)
            return result_string.split('=')[0] + f' = {rounded_result}'

    @classmethod
    def update_value(cls):
        console.clear()
        all_results = cls.get_all_results()
        cls.history()
        try:
            index = int(input(colored('Ingrese cual desea actualizar = ', 'light_yellow'))) - 1
            if index < 0 or index >= len(all_results):
                cprint('Número invalido.', 'white', 'on_red')
                return

            decimal = int(input(colored('Ingrese cuantos decimales desea ver = ', 'cyan')))
            result_string = all_results[index]
            new_result_string = cls.round_value(result_string, decimal)
            if "equivale a" in new_result_string:
                Conversor.results[index] = new_result_string
                Conversor.write()

            else:
                arithmetic_index = index - len(Conversor.results)
                if arithmetic_index >= 0 and arithmetic_index < len(Arithmetic.results):
                    Arithmetic.results[arithmetic_index] = new_result_string
                    Arithmetic.write()

            cprint(f'Resultado actualizado: {new_result_string}', 'light_green')
        except ValueError:
            cprint('Número invalido', 'red')
        except IndexError:
            cprint('Índice fuera de rango.', 'red')
