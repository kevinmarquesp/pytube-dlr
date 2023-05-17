#!/usr/bin/env python3

from pytube_dlr.models.types import TUserFactoryOptions
from pytube_dlr.models.abstracts import IApplicationFactory
from pytube_dlr.controllers.factories import LinuxCliApplicationFactory

from typing import NoReturn, Dict, Optional
from rich.traceback import install as traceback_install

traceback_install()


# todo: ...
def main(factory: IApplicationFactory) -> NoReturn:
    """Main function that will trigger the events in order to do the entire
    process of download some YouTube video.

    :param IApplicationFactory factory: Factory that has the right methods to
        handle the YouTube API, user arguments and handle with the file system.
    """
    pass


def setup(user_interface: TUserFactoryOptions = 'linux_cli') -> NoReturn:
    """Function responsible for setting up the right factories to generate the
    right tools to the ``main()`` function use it.

    :param Literal['linux_cli', 'win_cli'] interface: Type of user interface to
        factory.
    """
    FACTORIES: Dict[str, Optional[IApplicationFactory]] = {
        'linux_cli': LinuxCliApplicationFactory(),
        'win_cli': None
    }

    if FACTORIES[user_interface] is not None and user_interface in FACTORIES:
        factory: IApplicationFactory = FACTORIES[user_interface]  # type: ignore[assignment]
        main(factory)

    else:
        raise ValueError(f'Cannot work with this value: {user_interface}')
