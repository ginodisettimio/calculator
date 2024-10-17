from helpers.file_helpers import write_json_file, read_json_file, del_json_file
from typing import List
from abc import ABC
from termcolor import cprint


class Base(ABC):
    filename = ''
    results: List['Base'] = []

    @classmethod
    def write(cls):
        write_json_file(cls.filename, [result for result in cls.results])

    @classmethod
    def read(cls):
        cls.results = read_json_file(cls.filename)

    @classmethod
    def delete(cls):
        del_json_file(cls.filename)
        
    @classmethod
    def add_numbers(cls, count, result):
        if count not in cls.results:
            cls.results.append(count)
            cls.write()
            cprint(f'Resultado: {result}', "magenta")
        else:
            cprint('Resultado ya existe en el historial.', 'yellow')
