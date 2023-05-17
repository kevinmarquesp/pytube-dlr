from pytube_dlr.models.types import TUserArguments

from typing import NoReturn
from abc import ABC, abstractmethod


class IApplicatinArgumentsStorage(ABC):
    """Interface responsable to create the objects that saves all the user
    information needed to start the download and read/write in the cash files.
    It doesn't read but it only stores the data of the application
    """

    @abstractmethod
    def fill_arguments(self, dict_args: TUserArguments) -> NoReturn:
        """Function responsible to use an arguments dict and store all the usser
        information in this class (self), allowing to handle that information
        and start the features after with other methods

        :param TDictArguments IApplicationFactory: That's the dict type element
            that will be "converted" to a python object
        """


# todo: add documentation
class IApplicationFactory(ABC):
    """Model that a factory should have to be used in the ``app.py:main()```
    function.
    """

    @abstractmethod
    def get_arguments(self) -> IApplicatinArgumentsStorage:
        """Get the user arguments, I. E. the command options, and return a object
        with that information.
        """
