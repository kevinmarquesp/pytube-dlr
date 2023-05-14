#!/usr/bin/env python3

from pytube_dlr.models.abstracts import IApplicationFactory, IApplicationArgs
from pytube_dlr.controllers.factories import LinuxCliApplicationFactory

from typing import Literal, Dict
from rich.traceback import install as traceback_install

traceback_install()

TInterfaceOptions = Literal['linux_cli', 'win_cli']


# todo: ...
def main(factory: IApplicationFactory) -> None:
    """Main function that will trigger the events in order to do the entire
    process of download some YouTube video.

    :param IApplicationFactory factory: Factory that has the right methods to
        handle the YouTube API, user arguments and handle with the file system.

    Need to be done:
    ----------------
    - Make it verify if the user has past cache files to continue wight the
      downloading process;
        - If not, get the user arguments (it doesn't matter where it came from)
          to work with;
    - Using the argumetns, start the download process;

    Developer notes:
    ----------------
    Every event inside this function need to be triggered by the factory
    parammeter.
    """
    args: IApplicationArgs = factory.get_arguments()

    print('|> I need to work with this object:')
    print(args)


def setup(user_interface: TInterfaceOptions = 'linux_cli') -> None:
    """Function responsible for setting up the right factories to generate the
    right tools to the ``main()`` function use it.

    :param Literal['linux_cli', 'win_cli'] interface: Type of user interface to
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
