from abc import ABC, abstractmethod
from typing import Dict, List

from click import Choice


'''
В данном файле представлен прототип интерфейса плагинов программы.

Минимальные требования к автору плагина:
1) Бизнес-логика в методе call
2) Уникальные идентификатор плагина, возвращаемый get_name()
3) Словарь аргументов в формате {'Название аргумента': ['Тип аргумента', 'Промт для запроса пользователю']}
возвращаемый методом get_arguments()
'''


class IPlugin(ABC):

    @abstractmethod
    def get_name(self) -> str:
        return "unique name/keyword"

    @abstractmethod
    def get_arguments(self) -> Dict[str, List[any, str]]:
        return {"arg1": [float, "Prompt to ask for arg1"],
                "arg2": [str, "Prompt to ask for arg2"],
                "arg3": [Choice(["first option", "second option"]), "Prompt"]}

    @abstractmethod
    def __call__(self, *args, **kwargs):
        # do something...
        pass
