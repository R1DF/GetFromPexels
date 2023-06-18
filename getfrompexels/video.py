# Imports
from .user import User
from .video_file import PexelsVideoFile
from .video_picture import PexelsVideoPicture


# Video class
class PexelsVideo:
    def __init__(self, json_content):
        # Initialization of all read-only attributes
        self._pexels_id = json_content["id"]
        self._size = [json_content["width"], json_content["height"]]
        self._pexels_url = json_content["url"]
        self._screenshot_url = json_content["image"]
        self._duration = json_content["duration"]
        self._owner = User(
            json_content["user"]["id"],
            json_content["user"]["name"],
            json_content["user"]["url"]
        )

        # Initialization continued; creation of lists with child classes
        video_files = json_content["video_files"]
        video_pictures = json_content["video_pictures"]
        self._video_files = [PexelsVideoFile(x) for x in video_files]  # PexelsVideoArray per element of array
        self._video_pictures = [PexelsVideoPicture(x["id"], x["picture"]) for x in video_pictures]  # PexelsVideoPicture per element of array

    # Properties
    @property
    def pexels_id(self) -> int:
        return self._pexels_id

    @property
    def size(self) -> list[int]:
        return self._size

    @property
    def pexels_url(self) -> str:
        return self._pexels_url

    @property
    def screenshot_url(self) -> str:
        return self._screenshot_url

    @property
    def duration(self) -> int:
        return self._duration

    @property
    def owner(self) -> User:
        return self._owner

    @property
    def video_files(self) -> list[PexelsVideoFile]:
        return self._video_files

    @property
    def video_pictures(self) -> list[PexelsVideoPicture]:
        return self._video_pictures

