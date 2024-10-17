from models.base_model import Base
from config import constants


class Conversor(Base):
    filename = constants.CONVERSOR_PATH

    def __init__(self, number1, result: float, convert):
        self.number1 = number1
        self.convert = convert
        self._result = result

    def convert_temperature(number1: float, from_unit: str, convert: str) -> float:
        if from_unit == 'Fahrenheit':
            if convert == 'Celsius':
                result = (number1 - 32) * 5 / 9
                return result
            elif convert == 'Kelvin':
                result = (number1 - 32) * 5 / 9 + 273.15
                return result
        elif from_unit == 'Celsius':
            if convert == 'Fahrenheit':
                result = (number1 * 9 / 5) + 32
                return result
            elif convert == 'Kelvin':
                result = number1 + 273.15
                return result
        elif from_unit == 'Kelvin':
            if convert == 'Celsius':
                result = number1 - 273.15
                return result
            elif convert == 'Fahrenheit':
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
    