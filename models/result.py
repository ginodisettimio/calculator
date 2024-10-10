from helpers.file_helpers import write_json_file, read_json_file, del_json_file
from config import constants


class Result:
    results = []

    def __init__(self, operation, number1, number2, result):
        self.operation = operation
        self.number1 = number1
        self.number2 = number2
        self.result = result

    @classmethod
    def add(cls):
        write_json_file(constants.OPERATIONS_PATH, [
                        result for result in cls.results])

    @classmethod
    def read(cls):
        Result.results = read_json_file(constants.OPERATIONS_PATH)

    @classmethod
    def delete(cls):
        del_json_file(constants.OPERATIONS_PATH)
