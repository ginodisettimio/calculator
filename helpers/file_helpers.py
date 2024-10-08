import json
import config.constants


def write_json_file(path: list, content: list) -> None:
    with open(path, 'w') as file:
        return json.dump(content, file, indent=4)


def read_json_file(path: str) -> list:
    try:
        with open(path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        write_json_file(path, [])
        return []
