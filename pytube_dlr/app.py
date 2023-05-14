#!/usr/bin/env python3

from pytube_dlr.models.abstracts import IApplicationFactory, IApplicationArgs
from pytube_dlr.controllers.factories import LinuxCliApplicationFactory

from typing import Literal, Dict
from rich.traceback import install as traceback_install

traceback_install()

TInterfaceOptions = Literal['linux_cli', 'win_cli']


# todo: add documentation
def main(factory: IApplicationFactory) -> None:
    args: IApplicationArgs = factory.get_arguments()

    print('|> I need to work with this object:')
    print(args)


# todo: write tests
def setup(user_interface: TInterfaceOptions = 'linux_cli') -> None:
    """Function responsible for setting up the right factories to generate the
    right tools to the ``main()`` function use it.

    :param Literal['linux_cli', 'win_cli'] interface: type of user interface to
        factory.
    """
    FACTORIES: Dict[str, IApplicationFactory] = {
        'linux_cli': LinuxCliApplicationFactory(),
        'win_cli': None
    }

    if user_interface in FACTORIES:
        if FACTORIES[user_interface] is None:
            raise "That interface doesn't"

        factory: IApplicationFactory = FACTORIES[user_interface]
        main(factory)
