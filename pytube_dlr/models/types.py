from typing import List, Literal, NoReturn
import dataclasses


#: Available factories types that can be created
TUserFactoryOptions = Literal[
    'linux_cli',  # CLI app compatible with the Linux filesystem
    'win_cli'     # CLI app compatible with the Windows filesystem
]


# todo: add docstring
# todo: add a regex url video verification
@dataclasses.dataclass(kw_only=True, frozen=True)
class InfoYoutubeVideo:
    title: str
    url: str

    def __post_init__(self) -> NoReturn:
        if 'youtube' not in self.url:
            raise ValueError('Invalid youtube url')


# todo: add docstring
# todo: add a regex url playlist verification
@dataclasses.dataclass(kw_only=True, frozen=True)
class InfoYoutubePlaylist:
    name: str
    url: str

    def __post_init__(self) -> NoReturn:
        if 'youtube' not in self.url:
            raise ValueError('Invalid youtube url')


# todo: add docstring
# todo: add a regex url playlist verification
@dataclasses.dataclass(kw_only=True, frozen=True)
class InfoUserArguments:
    links: List[str] = dataclasses.field(default_factory=List)
    whatif: bool = False
    target: str
    cpu: int
