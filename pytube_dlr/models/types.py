from typing import TypedDict, List, Literal


#: Available factories types that can be created
TUserFactoryOptions = Literal[
    'linux_cli',  # CLI app compatible with the Linux filesystem
    'win_cli'     # CLI app compatible with the Windows filesystem
]


class TYoutubeVideo(TypedDict):
    """Type of a dict that store the information of one single YouTube video"""

    name: str
    url: str


class TYoutubePlaylist(TypedDict):
    """Type of a dict that can store an entire playlist with its videos"""

    name: str
    url: str
    videos: List[TYoutubeVideo]


class TUserArguments(TypedDict):
    """Dict type of the arguments that the user can provide and modify"""

    links: List[str]
    target: str
    whatif: bool
    cpu: int
