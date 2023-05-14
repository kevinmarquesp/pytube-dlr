from typing import TypedDict, List, Literal


TUserFactoryOptions = Literal['linux_cli', 'win_cli']


# todo: add documentation
class TPlaylist(TypedDict):
    name: str
    url: str


# todo: add documentation
class TDictArguments(TypedDict):
    links: List[str]
    target: str
    whatif: bool
    cpu: int
