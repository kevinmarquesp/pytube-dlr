#!/usr/bin/env python3

from pytube_dlr.models.abstracts import IApplicationFactory, IApplicationArgs
from pytube_dlr.controllers.factories import LinuxCliApplicationFactory

from typing import Literal, Dict
from rich.traceback import install as traceback_install

traceback_install()

TInterfaceOptions = Literal['cli', 'linux_ui', 'win_ui']


# todo: add documentation
def main(factory: IApplicationFactory) -> None:
    args: IApplicationArgs = factory.get_arguments()

    print('|> I need to work with this object:')
    print(args)


# todo: add documentation
# todo: write tests
def setup(interface: TInterfaceOptions = 'cli') -> None:
    FACTORIES: Dict[str, IApplicationFactory] = {
        'cli': LinuxCliApplicationFactory(),
        'linux_ui': None,
        'win_ui': None
    }

    if interface in FACTORIES:
        if FACTORIES[interface] is None:
            raise "That interface doesn't exist yet"

        factory: IApplicationFactory = FACTORIES[interface]
        main(factory)
