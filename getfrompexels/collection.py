# Imports
from user import User
from dataclasses import dataclass

# Collection class
@dataclass
class Collection:
    _pexels_id: int
    _title: str
    _description: str
    _is_private: bool
    _media_count: int
    _photos_count: int
    _videos_count: int

    # Properties
    @property
    def pexels_id(self) -> int:
        return self._pexels_id

    @property
    def title(self) -> str:
        return self._title

    @property
    def description(self) -> str:
        return self._description

    @property
    def is_private(self) -> bool:
        return self._is_private

    @property
    def media_count(self) -> int:
        return self._media_count

    @property
    def photos_count(self) -> int:
        return self._photos_count

    @property
    def videos_count(self) -> int:
        return self._videos_count

