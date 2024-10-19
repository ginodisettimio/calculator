from termcolor import cprint

from models.base_model import Base
from config import constants
from helpers.file_helpers import write_json_file

class Conversor(Base):
    filename = constants.CONVERSOR_PATH

    def __init__(self, number1, result: float, convert):
        self.number1 = number1
        self.convert = convert
        self._result = result

    results = []

    @classmethod
    def add_numbers(cls, count, result):
        Conversor.results.append(count)
        Conversor.write()
        cprint(f'Resultado: {result}', "magenta")

    @staticmethod
    def write():
        write_json_file(Conversor.filename, Conversor.results)

    def convert_temperature(number1: float, from_unit: str, convert: str) -> float:
        if from_unit == 'F':
            if convert == 'C':
                result = (number1 - 32) * 5 / 9
                return result
            elif convert == 'K':
                result = (number1 - 32) * 5 / 9 + 273.15
                return result
        elif from_unit == 'C':
            if convert == 'F':
                result = (number1 * 9 / 5) + 32
                return result
            elif convert == 'K':
                result = number1 + 273.15
                return result
        elif from_unit == 'K':
            if convert == 'C':
                result = number1 - 273.15
                return result
            elif convert == 'F':
                result = (number1 - 273.15) * 9 / 5 + 32
                return result
        return None
    
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if value is str or bool:
            raise Exception('Número invalido.')
        self.result = value
    