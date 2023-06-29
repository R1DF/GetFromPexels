"""
This class contains custom-made exceptions for GetFromPexels.
"""


class PexelsAuthorizationError(Exception):
    pass


class PexelsSearchError(Exception):  # For search functions
    pass


class PexelsLookupError(Exception):  # For find functions
    pass


class PexelsAPIRequestError(Exception):
    # Will be called when an HTTPS response does not return 200 (PexelsLookupError sometimes can substitute for 404).
    pass
