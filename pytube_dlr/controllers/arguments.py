from pytube_dlr.models.abstracts import IApplicatinArgumentsStorage
from pytube_dlr.models.types import TUserArguments

from argparse import Namespace as ArgPaarse_Namespace, ArgumentParser
from sys import argv
from os import getcwd, cpu_count


class ApplicationArgs(IApplicatinArgumentsStorage):
    # todo: write tests
    # todo: make it create the correct attributes based on the arguments
    def fill_arguments(self, dict_args: TUserArguments):
        print(dict_args)


# todo: write tests
def get_user_command_args() -> ArgPaarse_Namespace:
    """Use the ``argparse`` library to get the command line option and return
    a object with that arguments parsed.
    """
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
