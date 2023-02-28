from typing import Dict, List

import click

from v2.new_commands import save


'''
В данном файле приведена попытка решить проблему сериализации типовых команд для плагинов будущей программы.

Функция generate_commands позволяет создавать типовые команды по заданному имени (keyword для идентификации команды) и
словарю аргументов, содержащему, как типы данных, так и промты, которые будут выведены пользователю.

С минимальными изменениями в представлении данных (move, rotate и cut претерпели незначительные изменения)
был полностью воспроизведен функционал предыдущей версии.
'''


def generate_command(name: str, args: Dict[str, List[any]]) -> callable:

    def func():
        arguments = {"type": name}
        for arg in args:
            arguments[arg] = click.prompt(args[arg][1], type=args[arg][0])

        save(arguments)

    return func


def setup() -> dict:
    func_args = {"move": {"x": [float, "x-axis shift value"],
                          "y": [float, "y-axis shift value"],
                          "z": [float, "z-axis shift value"]},

                 "rotate": {"deg_rad": [str, "Degree/Radian"],
                            "x": [int, "x-axis rotation angle"],
                            "y": [int, "y-axis rotation angle"],
                            "z": [int, "z-axis rotation angle"]},

                 "cut": {"up-left": [bool, "Cut upper-left corner"],
                         "up-right": [bool, "Cut upper-right corner"],
                         "down-left": [bool, "Cut lower-left corner"],
                         "down-right": [bool, "Cut lower-right corner"]},

                 "patch": {"degree": [int, "Degree of interpolation"]},

                 "remove": {"height": [float, "height value"],
                            "above_below": [str, "Above/below"]},

                 "mount": {"path": [str, "Path to GeoTIFF picture to mount"]}
                 }

    operations = {}

    for func in func_args:
        operations[func] = generate_command(func, func_args[func])

    return operations
