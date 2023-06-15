# Imports
from dataclasses import dataclass

# Class
@dataclass
class PexelsVideoPicture:
    _pexels_id: int
    _picture_url: str

    # Properties
    @property
    def pexels_id(self) -> int:
        return self._pexels_id

    @property
    def picture_url(self) -> str:
        return self._picture_url

