from typing import List
from abc import ABC, abstractmethod

from helpers.file_helpers import read_json_file, del_json_file


class Base(ABC):
    filename = ''
    results: List['Base'] = []

    @abstractmethod
    def add_numbers():
        pass

    @abstractmethod
    def write(cls):
        pass

    @classmethod
    def read(cls):
        cls.results = read_json_file(cls.filename)

    @classmethod
    def delete(cls):
        del_json_file(cls.filename)
