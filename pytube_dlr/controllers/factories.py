from pytube_dlr.models.abstracts import IApplicationFactory, IApplicationArgs
from pytube_dlr.controllers.arguments import ApplicationArgs
from pytube_dlr.controllers.arguments import get_user_command_args

from argparse import Namespace


class LinuxCliApplicationFactory(IApplicationFactory):
    # todo: write tests
    def get_arguments(self) -> IApplicationArgs:
        arguments_class: IApplicationArgs = ApplicationArgs()
        user_args: Namespace = get_user_command_args()

        arguments_class.fill_arguments({
            "links":  user_args.links,
            "target": user_args.target,
            "whatif": user_args.whatif,
            "cpu":    user_args.cpu
        })

        return arguments_class
