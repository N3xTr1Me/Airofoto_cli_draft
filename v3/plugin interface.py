from abc import ABC, abstractmethod
from typing import Dict, List

from click import Choice


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
