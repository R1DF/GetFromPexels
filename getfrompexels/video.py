# Imports
from user import User

# Video class
class PexelsVideo:
    def __init__(self, json_content):
        # Initialization of read-only attributes
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
