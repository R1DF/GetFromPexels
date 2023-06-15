"""
This class contains custom-made exceptions for GetFromPexels.
"""

class PexelsAuthorizationError(Exception):
    pass

class PexelsSearchError(Exception): # For search functions
    pass

class PexelsLookupError(Exception): # For find functions
    pass

