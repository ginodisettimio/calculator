from models.base_model import Base
from config import constants


class Arithmetic(Base):
    filename = constants.OPERATIONS_PATH

    def __init__(self, number1, number2, result: float):
        self.number1 = number1
        self.number2 = number2
        self._result = result

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

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if value is str or bool:
            raise Exception('Número invalido.')
        self.result = value

    
