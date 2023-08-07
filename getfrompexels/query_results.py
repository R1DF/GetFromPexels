"""Module containing the PexelsQueryResults dataclass."""

# Imports
from dataclasses import dataclass
from .photo import PexelsPhoto
from .video import PexelsVideo
from .collection import PexelsCollection


# Type aliases
PexelsContent = list[PexelsPhoto | PexelsVideo | PexelsCollection]  # unable to fit in type_hints.py (circular import)


# Class
@dataclass
class PexelsQueryResults:
    """Dataclass that contains the results of a query made by a PexelsSession object.

    :param _content: A list that contains PexelsPhoto, PexelsVideo, or PexelsCollection objects. Can be mixed
    :type _content: list
    :param _url: The URl of the query
    :type _url: str
    :param _total_results: The total amount of media that was returned from the query
    :type _total_results: int
    :param _page: The page number of the query
    :type _page: int
    :param _per_page: The number of content returned per page
    :type _per_page: int
    """

    _content: list
    _url: str
    _total_results: int
    _page: int
    _per_page: int

    # Properties
    @property
    def content(self) -> PexelsContent:
        """A list that contains PexelsPhoto, PexelsVideo, or PexelsCollection objects. Can be mixed."""
        return self._content

    @property
    def url(self) -> str:
        """The URL of the query."""
        return self._url

    @property
    def total_results(self) -> int:
        """The total amount of results received from the query."""
        return self._total_results

    @property
    def page(self) -> int:
        """The page number of the query."""
        return self._page

    @property
    def per_page(self) -> int:
        """The amount of content returned per page."""
        return self._per_page
