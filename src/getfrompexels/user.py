# Imports
from dataclasses import dataclass


# User class
@dataclass
class User:
    _name: str
    _url: str
    _pexels_id: int

    # Properties
    @property
    def name(self):
        return self._name

    @property
    def url(self):
        return self._url

    @property
    def pexels_id(self):
        return self._pexels_id

    @property
    def username(self):
        return "@" + self.url.split("@")[1]
