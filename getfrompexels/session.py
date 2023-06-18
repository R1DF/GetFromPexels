"""
PexelsSession class
This is the main class that should be used to get content from the service Pexels.
The API key can be passed as an argument either when a class instance is defined, or set later with
the function set_key().
"""

# Imports
from .custom_exceptions import *
from .photo import PexelsPhoto
from .video import PexelsVideo
from .query_results import PexelsQueryResults
from .endpoints import ENDPOINTS
import requests

# Session class
class PexelsSession:
    def __init__(self, key: str = None):
        # Initialisation
        self._key = key

        # The values below can only be seen after the first successful request is made.
        self._request_limit = None
        self._requests_left = None
        self._requests_rollback_timestamp = None

    # Wrapper function to make sure API key is valid
    # def ensure_valid_key(function):
    #     def inner_function(self, *args, **kwargs):
    #         if self._key is None:
    #             raise PexelsAuthorizationError("API key was not provided")
    #         return function(self, *args, **kwargs)
    #     return inner_function

    # Finding functions
    # @ensure_valid_key

    def get_query_parameters(self, **parameters):
        # Returns an incomplete part of a URL for an endpoint with parameters for making requests with specific values
        if parameters:
            return "?" + "&".join([f"{key}={value}" for key, value in parameters.items() if value is not None])
        return ""

    def find_photo(self, photo_id):
        if self._key is not None:
            targeted_endpoint = ENDPOINTS["FIND_PHOTO"]
            response = requests.get(f"{targeted_endpoint}/{photo_id}", headers={"Authorization": self._key})
            if response.status_code != 200:
                raise PexelsAuthorizationError("invalid API key for authorization")
            self.update_rate_limit_attributes(response)
            return PexelsPhoto(response.json())
        raise PexelsAuthorizationError("API key must be provided for function call")

    def find_video(self, video_id):
        if self._key is not None:
            targeted_endpoint = ENDPOINTS["FIND_VIDEO"]
            response = requests.get(f"{targeted_endpoint}/{video_id}", headers={"Authorization": self._key})

            # TODO improve request status code checking, such as 401/403 and 429 to differentiate them better
            #  and also to shorten code length for functions
            if response.status_code != 200:
                raise PexelsAuthorizationError("invalid API key for authorization")
            self.update_rate_limit_attributes(response)
            return PexelsVideo(response.json())
        raise PexelsAuthorizationError("API key must be provided for function call")

    # Search for curated photos/popular videos
    def search_curated_photos(self, *, page=1, per_page=15):
        if per_page > 80 or per_page < 1:
            return PexelsSearchError("per_page parameter must be in between 1 and 80 inclusive")

        if page < 1:
            PexelsSearchError("page parameter must be at least 1")

        if self._key is not None:
            targeted_endpoint = ENDPOINTS["CURATED_PHOTOS"] + self.get_query_parameters(page=page, per_page=per_page)
            response = requests.get(targeted_endpoint,
                                    headers={"Authorization": self._key})
            if response.status_code != 200:
                raise PexelsAuthorizationError("invalid API key for authorization")
            self.update_rate_limit_attributes(response)

            results = response.json()
            return PexelsQueryResults(
                _content=[PexelsPhoto(x) for x in results["photos"]],
                _url=targeted_endpoint,
                _total_results=results["total_results"],
                _page=results["page"],
                _per_page=results["per_page"]
            )

        raise PexelsAuthorizationError("API key must be provided for function call")

    def search_popular_videos(
            self,
            *,
            min_width=None,
            min_height=None,
            min_duration=None,
            max_duration=None,
            page=1,
            per_page=15
    ):
        if per_page > 80 or per_page < 1:
            return PexelsSearchError("per_page parameter must be in between 1 and 80 inclusive")

        if page < 1:
            PexelsSearchError("page parameter must be at least 1")

        if self._key is not None:
            targeted_endpoint = ENDPOINTS["POPULAR+VIDEOS"] + self.get_query_parameters(
                min_width=min_width,
                min_height=min_height,
                min_duration=min_duration,
                max_duration=max_duration,
                page=page,
                per_page=per_page,
            )
            response = requests.get(targeted_endpoint,
                                    headers={"Authorization": self._key})
            if response.status_code != 200:
                raise PexelsAuthorizationError("invalid API key for authorization")
            self.update_rate_limit_attributes(response)

            results = response.json()
            return PexelsQueryResults(
                _content=[PexelsVideo(x) for x in results["videos"]],
                _url=targeted_endpoint,
                _total_results=results["total_results"],
                _page=results["page"],
                _per_page=results["per_page"]
            )

        raise PexelsAuthorizationError("API key must be provided for function call")


    # Search by keyword functions
    def search_photos(self, query):
        pass

    def search_videos(self, query):
        pass

    # Key setting function
    def set_key(self, key: str):
        self._key = key

    # Updating saved rate limit values
    def update_rate_limit_attributes(self, response):
        self._request_limit = response.headers["X-Ratelimit-Limit"]
        self._requests_left = response.headers["X-Ratelimit-Remaining"]
        self._requests_rollback_timestamp = response.headers["X-Ratelimit-Reset"]

    # Properties
    @property
    def key(self):
        return self._key

    @property
    def request_limit(self):
        return self._request_limit

    @property
    def requests_left(self):
        return self._requests_left

    @property
    def requests_rollback_timestamp(self):
        return self._requests_rollback_timestamp

