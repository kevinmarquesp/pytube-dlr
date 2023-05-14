from pytube_dlr.models.abstracts import IApplicationFactory, IArguments
from pytube_dlr.controllers.arguments import Arguments, get_parsed_args

from argparse import Namespace


class LinuxCliAppFactory(IApplicationFactory):
    # todo: write tests
    def get_arguments(self) -> IArguments:
        arguments: IArguments = Arguments()
        user_args: Namespace = get_parsed_args()

        arguments.fill_arguments({
            "links": user_args.links,
            "target": user_args.target,
            "what_if": user_args.whatif,
            "cpu": user_args.cpu
        })

        return arguments
