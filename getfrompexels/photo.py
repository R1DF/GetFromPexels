# Imports
from user import User

# Photo class
class PexelsPhoto:
    def __init__(self, json_content):
        # Initialization of read-only attributes
        self._pexels_id = json_content["id"]
        self._size = [json_content["width"], json_content["height"]]
        self._pexels_url = json_content["url"]
        self._average_color = json_content["avg_color"]
        self._photographer = User(
            json_content["photographer"],
            json_content["photographer_url"],
            json_content["photographer_id"]
        )
        self._links = {
            "original": json_content["src"]["original"],
            "large": json_content["src"]["large"],
            "large_2x": json_content["src"]["large2x"],
            "medium": json_content["src"]["medium"],
            "small": json_content["src"]["small"],
            "portrait": json_content["src"]["portrait"],
            "landscape": json_content["src"]["landscape"],
            "tiny": json_content["src"]["tiny"]
        }
        self._liked_by_user = json_content["liked"]
        self._alt_text = json_content["alt"]

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
    def average_color(self) -> str:
        return self._average_color

    @property
    def photographer(self) -> User:
        return self._photographer

    @property
    def links(self) -> dict:
        return self._links

    @property
    def liked_by_user(self) -> bool:
        return self._liked_by_user

    @property
    def alt_text(self) -> str:
        return self._alt_text

