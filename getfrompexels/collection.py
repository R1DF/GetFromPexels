"""Module containing the PexelsCollection dataclass."""

# Imports
from dataclasses import dataclass


# Collection class
@dataclass
class PexelsCollection:
    """The dataclass that stores information of a collection on Pexels. PexelsCollection objects contain properties that
    are meant to be used, specifically to avoid modifying attributes which are not meant to be modified.

    :param _pexels_id: The ID of the collection
    :type _pexels_id: str
    :param _title: The name of the collection
    :type _title: str
    :param _description: The description of the collection
    :type _description: str
    :param _is_private: Boolean value that shows whether the collection is marked as private or not
    :type _is_private: bool
    :param _media_count: Total amount of media in the collection
    :type _media_count: int
    :param _photos_count: Total amount of photos in the collection
    :type _photos_count: int
    :param _videos_count: Total amount of videos in the collection
    :type _videos_count: int
    """

    _pexels_id: str
    _title: str
    _description: str
    _is_private: bool
    _media_count: int
    _photos_count: int
    _videos_count: int

    # Properties
    @property
    def pexels_id(self) -> str:
        """The ID of the collection."""
        return self._pexels_id

    @property
    def title(self) -> str:
        """The name of the collection."""
        return self._title

    @property
    def description(self) -> str:
        """The description of the collection."""
        return self._description

    @property
    def is_private(self) -> bool:
        """Boolean value that shows whether the collection is marked as private or not."""
        return self._is_private

    @property
    def media_count(self) -> int:
        """Total amount of media in the collection."""
        return self._media_count

    @property
    def photos_count(self) -> int:
        """Total amount of photos in the collection."""
        return self._photos_count

    @property
    def videos_count(self) -> int:
        """Total amount of videos in the collection."""
        return self._videos_count
