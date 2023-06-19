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
from .collection import PexelsCollection
from .query_results import PexelsQueryResults
from .endpoints import ENDPOINTS
from .verifier import verify_response
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

    def get_query_parameters(self, **parameters):
        # Returns an incomplete part of a URL for an endpoint with parameters for making requests with specific values
        if parameters:
            return "?" + "&".join([f"{key}={value}" for key, value in parameters.items() if value is not None])
        return ""

    def get_http_response(self, endpoint):
        if self._key is None:
            raise PexelsAuthorizationError("an API key must be provided for function call")

        response = requests.get(endpoint, headers={"Authorization": self._key})
        verify_response(response)
        return response

    def find_photo(self, photo_id):
        # Making request
        targeted_endpoint = ENDPOINTS["FIND_PHOTO"]
        request_url = self.get_http_response(f"{targeted_endpoint}/{photo_id}")
        response = self.get_http_response(request_url).json()

        # Returning data and updating rate limit values
        self.update_rate_limit_attributes(response)
        return PexelsPhoto(response.json())

    def find_video(self, video_id):
        # Making request
        targeted_endpoint = ENDPOINTS["FIND_VIDEO"]
        request_url = self.get_http_response(f"{targeted_endpoint}/{video_id}")
        response = self.get_http_response(request_url).json()

        # Returning data and updating rate limit values
        self.update_rate_limit_attributes(response)
        return PexelsVideo(response.json())

    # Search for curated photos/popular videos
    def search_curated_photos(self, *, page=1, per_page=15):
        # Checking specific argument validity
        if per_page > 80 or per_page < 1:
            raise PexelsSearchError("per_page parameter must be in between 1 and 80 inclusive")

        if page < 1:
            PexelsSearchError("page parameter must be at least 1")

        # Making request
        targeted_endpoint = ENDPOINTS["FIND_VIDEO"]
        request_url = self.get_http_response(targeted_endpoint + self.get_query_parameters(page=page, per_page=per_page))
        response = self.get_http_response(request_url).json()

        # Returning data and updating rate limit values
        self.update_rate_limit_attributes(response)
        results = response.json()
        return PexelsQueryResults(
            _content=[PexelsPhoto(x) for x in results["photos"]],
            _url=targeted_endpoint,
            _total_results=results["total_results"],
            _page=results["page"],
            _per_page=results["per_page"]
        )

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
        # Checking specific argument validity
        if per_page > 80 or per_page < 1:
            raise PexelsSearchError("per_page parameter must be in between 1 and 80 inclusive")

        if page < 1:
            PexelsSearchError("page parameter must be at least 1")

        # Making request
        targeted_endpoint = ENDPOINTS["POPULAR_VIDEOS"]
        request_url = self.get_http_response(targeted_endpoint + self.get_query_parameters(
            min_width=min_width,
            min_height=min_height,
            min_duration=min_duration,
            max_duration=max_duration,
            page=page,
            per_page=per_page
        ))
        response = self.get_http_response(request_url).json()

        # Returning data and updating rate limit values
        self.update_rate_limit_attributes(response)
        results = response.json()
        return PexelsQueryResults(
            _content=[PexelsVideo(x) for x in results["videos"]],
            _url=targeted_endpoint,
            _total_results=results["total_results"],
            _page=results["page"],
            _per_page=results["per_page"]
        )

    def search_featured_collections(self, *, page=1, per_page=15):
        # Checking specific argument validity
        if per_page > 80 or per_page < 1:
            raise PexelsSearchError("per_page parameter must be in between 1 and 80 inclusive")

        if page < 1:
            raise PexelsSearchError("page parameter must be at least 1")

        # Making request
        targeted_endpoint = ENDPOINTS["POPULAR_VIDEOS"] + self.get_query_parameters(
            page=page,
            per_page=per_page
        )
        response = requests.get(targeted_endpoint,
                                headers={"Authorization": self._key})

        # Returning data and updating rate limit values
        self.update_rate_limit_attributes(response)
        results = response.json()
        return PexelsQueryResults(
            _content=[PexelsCollection(
                _pexels_id=x["id"],
                _title=x["title"],
                _description=x["description"],
                _is_private=x["private"],
                _media_count=x["media_count"],
                _photos_count=x["photos_count"],
                _videos_count=x["videos_count"]

            ) for x in results["collections"]],
            _url=targeted_endpoint,
            _total_results=results["total_results"],
            _page=results["page"],
            _per_page=results["per_page"]
        )


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

