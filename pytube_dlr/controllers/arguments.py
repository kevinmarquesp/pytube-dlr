from pytube_dlr.models.abstracts import IApplicationArgs
from pytube_dlr.models.types import TDictArguments

from typing import NoReturn
from argparse import Namespace, ArgumentParser
from sys import argv
from os import getcwd, cpu_count


class ApplicationArgs(IApplicationArgs):
    # todo: add documentation
    # todo: write tests
    # todo: make it create the correct attributes based on the arguments
    def fill_arguments(self, dict_args: TDictArguments) -> NoReturn:
        print(dict_args)


# todo: add documentation
# todo: write tests
def get_user_command_args() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        description='YouTube downloader with a friendly UI'
    )

    parser.add_argument('links', type=str,
                        help='List of YouTube video links')

    parser.add_argument('--target', '-t', type=str, default=getcwd(),
                        help='Target directory to save all the files')

    parser.add_argument('--cpu', '-c', type=int, default=cpu_count(),
                        help='How many process will be running to download')

    parser.add_argument('--whatif', '-w', type=bool, default=False,
                        help='Flag to simulate the execution without download')

    return parser.parse_args(argv)
