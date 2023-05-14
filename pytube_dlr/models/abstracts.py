from pytube_dlr.models.types import TDictArguments

from typing import NoReturn
from abc import ABC, abstractmethod


# todo: add documentation
class IApplicationArgs(ABC):
    """
    """

    @abstractmethod
    def fill_arguments(self, dict_args: TDictArguments) -> NoReturn:
        """
        """


# todo: add documentation
class IApplicationFactory(ABC):
    """
    """

    @abstractmethod
    def get_arguments(self) -> IApplicationArgs:
        """
        """
