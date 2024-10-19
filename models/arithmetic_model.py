from termcolor import cprint

from models.base_model import Base
from config import constants
from helpers.file_helpers import write_json_file


class Arithmetic(Base):
    filename = constants.OPERATIONS_PATH
    def __init__(self, number1, number2, result: float):
        self.number1 = number1
        self.number2 = number2
        self._result = result
    
    results = []

    @classmethod
    def add_numbers(cls, count, result):
        Arithmetic.results.append(count)
        Arithmetic.write()
        cprint(f'Resultado: {result}', "magenta")
        
    @staticmethod
    def write():
        write_json_file(Arithmetic.filename, Arithmetic.results)

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
        try:
            return number1**number2
        except OverflowError:
            return 'Número demasiado grande'
    
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if value is str or bool:
            raise Exception('Número invalido.')
        self.result = value

    
