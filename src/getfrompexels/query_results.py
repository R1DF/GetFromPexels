# Imports
from dataclasses import dataclass


# Class
@dataclass
class PexelsQueryResults:
    _content: list
    _url: str
    _total_results: int
    _page: int
    _per_page: int

    # Properties
    @property
    def content(self) -> list:
        return self._content

    @property
    def url(self) -> str:
        return self._url

    @property
    def total_results(self) -> int:
        return self._total_results

    @property
    def page(self) -> int:
        return self._page

    @property
    def per_page(self) -> int:
        return self._per_page
