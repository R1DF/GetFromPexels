# Photo class
class PexelsVideoFile:
    def __init__(self, json_content):
        # Initialization of attributes
        self._pexels_id = json_content["id"]
        self._quality = json_content["quality"]
        self._file_type = json_content["file_type"]
        self._size = [json_content["width"], json_content["height"]]
        self._fps = json_content["fps"]
        self._url = json_content["link"]

    # Properties
    @property
    def pexels_id(self) -> int:
        return self._pexels_id

    @property
    def quality(self) -> str:
        return self._quality

    @property
    def file_type(self) -> str:
        return self._file_type

    @property
    def file_extension(self) -> str:
        return self.file_type.split("/")[-1]

    @property
    def size(self) -> list[int]:
        return self._size

    @property
    def fps(self) -> float:
        return self._fps

    @property
    def url(self) -> str:
        return self._url

