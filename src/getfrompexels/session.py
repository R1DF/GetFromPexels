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
import re


# Non-class function
def ensure_lower(*values):
    return list(map(lambda x: x.lower() if isinstance(x, str) else x, values))


def check_query_arguments(query, orientation, size, color, locale):
    # Type annotations above are not needed, for the if-statements below do not use their class' methods.
    orientation, size, color, locale = ensure_lower(orientation, size, color, locale)

    if not query:
        raise PexelsSearchError("query parameter must be entered")

    if (orientation is not None) and (orientation not in ["landscape", "portrait", "square"]):
        raise PexelsSearchError("unsupported or invalid orientation parameter, must either not be set or "
                                "landscape, portrait or square")

    if (size is not None) and (size not in ["small", "medium", "large"]):
        raise PexelsSearchError("unsupported or invalid size parameter, must either not be set or small, "
                                "medium or large")

    if (color is not None) and (color not in SUPPORTED_PHOTO_COLORS) and \
            (not re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$',
                           color)):  # Thanks to teoreda StackOverflow for hex col detection
        raise PexelsSearchError("unsupported or invalid color parameter")

    if (locale is not None) and (locale not in SUPPORTED_LOCATIONS):
        raise PexelsSearchError("unsupported or invalid locale parameter")


def get_query_parameters(**parameters):
    # Returns an incomplete part of a URL for an endpoint with parameters for making requests with specific values
    if parameters:
        return "?" + "&".join([f"{key}={value}" for key, value in parameters.items() if value is not None])
    return ""


# Constants
SUPPORTED_PHOTO_COLORS = (
    "red",
    "orange",
    "yellow",
    "green",
    "turquoise",
    "blue",
    "violet",
    "pink",
    "brown",
    "black",
    "gray",
    "white"
)

SUPPORTED_LOCATIONS = (
    "en-US",
    "pt-BR",
    "es-ES",
    "it-it",
    "fr-FR",
    "sv-SE",
    "id-ID",
    "pl=PL",
    "ja-JP",
    "zh-TW",
    "zh-CN",
    "ko-KR",
    "th-TH",
    "nl-NL",
    "hu-HU",
    "vi-VN",
    "cs-CZ",
    "da-DK",
    "fi-FI",
    "uk-UA",
    "el-GR",
    "ro-RO",
    "nb-NO",
    "sk-SK",
    "tr-TR",
    "ru-RU"
)


# Session class
class PexelsSession:
    def __init__(self, key: str = None):
        # Initialisation
        self._key = key

        # The values below can only be seen after the first successful request is made.
        self._request_limit = None
        self._requests_left = None
        self._requests_rollback_timestamp = None

    # Functions to shorten code
    def get_https_response(self, endpoint: str, origin_function_type: str | None = None):
        if self._key is None:
            raise PexelsAuthorizationError("an API key must be provided for function call")

        response = requests.get(endpoint, headers={"Authorization": self._key})
        verify_response(response, origin_function_type)
        return response

    # API wrapper functions
    def find_photo(self, photo_id: int):
        # Making request
        targeted_endpoint = ENDPOINTS["FIND_PHOTO"]
        request_url = f"{targeted_endpoint}/{photo_id}"
        response = self.get_https_response(request_url, "find")

        # Returning data and updating rate limit values
        self.update_rate_limit_attributes(response)
        return PexelsPhoto(response.json())

    def find_video(self, video_id: int):
        # Making request
        targeted_endpoint = ENDPOINTS["FIND_VIDEO"]
        request_url = f"{targeted_endpoint}/{video_id}"
        response = self.get_https_response(request_url, "find")

        # Returning data and updating rate limit values
        self.update_rate_limit_attributes(response)
        return PexelsVideo(response.json())

    # Search for curated photos/popular videos
    def search_curated_photos(self, page: int = 1, per_page: int = 15):
        # Checking specific argument validity
        if per_page > 80 or per_page < 1:
            raise PexelsSearchError("per_page parameter must be in between 1 and 80 inclusive")

        if page < 1:
            PexelsSearchError("page parameter must be at least 1")

        # Making request
        targeted_endpoint = ENDPOINTS["FIND_VIDEO"]
        request_url = targeted_endpoint + get_query_parameters(page=page, per_page=per_page)
        response = self.get_https_response(request_url).json()

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
            min_width: int | None = None,
            min_height: int | None = None,
            min_duration: int | None = None,
            max_duration: int | None = None,
            page: int = 1,
            per_page: int = 15
    ):
        # Checking specific argument validity
        if per_page > 80 or per_page < 1:
            raise PexelsSearchError("per_page parameter must be in between 1 and 80 inclusive")

        if page < 1:
            PexelsSearchError("page parameter must be at least 1")

        # Making request
        targeted_endpoint = ENDPOINTS["POPULAR_VIDEOS"]
        response = self.get_https_response(targeted_endpoint + get_query_parameters(
            min_width=min_width,
            min_height=min_height,
            min_duration=min_duration,
            max_duration=max_duration,
            page=page,
            per_page=per_page
        )).json()

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

    def search_featured_collections(self, page: int = 1, per_page: int = 15):
        # Checking specific argument validity
        if per_page > 80 or per_page < 1:
            raise PexelsSearchError("per_page parameter must be in between 1 and 80 inclusive")

        if page < 1:
            raise PexelsSearchError("page parameter must be at least 1")

        # Making request
        request_url = ENDPOINTS["POPULAR_VIDEOS"] + get_query_parameters(
            page=page,
            per_page=per_page
        )
        response = self.get_https_response(request_url).json()
        results = response.json()

        # Returning data and updating rate limit values
        self.update_rate_limit_attributes(response)
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
            _url=request_url,
            _total_results=results["total_results"],
            _page=results["page"],
            _per_page=results["per_page"]
        )

    # Search owned collection function
    def search_user_collections(self, page: int = 1, per_page: int = 15):
        # Checking specific argument validity
        if per_page > 80 or per_page < 1:
            raise PexelsSearchError("per_page parameter must be in between 1 and 80 inclusive")

        if page < 1:
            raise PexelsSearchError("page parameter must be at least 1")

        # Making request
        request_url = ENDPOINTS["USER_COLLECTIONS"] + get_query_parameters(
            page=page,
            per_page=per_page
        )
        response = self.get_https_response(request_url)
        results = response.json()

        # Returning data and updating rate limit values
        self.update_rate_limit_attributes(response)
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
            _url=request_url,
            _total_results=results["total_results"],
            _page=results["page"],
            _per_page=results["per_page"]
        )

    # Search media in collection
    def find_collection_contents(
            self,
            collection_id: int,
            media_type: str | None = None,
            page: int = 1,
            per_page: int = 15
    ):
        # Checking specific argument validity
        if media_type not in ["photo", "video"]:
            media_type = None  # Done to remove from parameters section in request URL

        if per_page > 80 or per_page < 1:
            raise PexelsSearchError("per_page parameter must be in between 1 and 80 inclusive")

        if page < 1:
            raise PexelsSearchError("page parameter must be at least 1")

        # Making request
        request_url = f"{ENDPOINTS['COLLECTION_MEDIA']}/{collection_id}" + get_query_parameters(
            page=page,
            per_page=per_page,
            type=media_type
        )
        response = self.get_https_response(request_url, "find")  # 404 counts as PexelsLookupError here
        results = response.json()

        # Returning data and updating rate limit values
        self.update_rate_limit_attributes(response)
        return PexelsQueryResults(
            _content=results["media"],
            _url=request_url,
            _total_results=results["total_results"],
            _page=results["page"],
            _per_page=results["per_page"]
        )

    # Search by keyword functions
    def search_for_photos(
            self,
            query: str,
            orientation: str | None = None,
            size: str | None = None,
            color: str | None = None,
            locale: str | None = None,
            page: int = 1,
            per_page: int = 15
    ):
        # Checking argument validity
        query = query.strip()
        check_query_arguments(query, orientation, size, color, locale)
        if per_page > 80 or per_page < 1:
            raise PexelsSearchError("per_page parameter must be in between 1 and 80 inclusive")

        if page < 1:
            raise PexelsSearchError("page parameter must be at least 1")

        # Making request
        request_url = ENDPOINTS["SEARCH_PHOTOS"] + get_query_parameters(
            query=query,
            orientation=orientation,
            size=size,
            color=color,
            locale=locale,
            page=page,
            per_page=per_page
        )
        response = self.get_https_response(request_url)
        results = response.json()

        # Returning data and updating rate limit values
        self.update_rate_limit_attributes(response)
        return PexelsQueryResults(
            _content=[PexelsPhoto(x) for x in results["photos"]],
            _url=request_url,
            _total_results=results["total_results"],
            _page=results["page"],
            _per_page=results["per_page"]
        )

    def search_for_videos(
            self,
            query: str,
            orientation: str | None = None,
            size: str | None = None,
            locale: str | None = None,
            page=1,
            per_page=15
    ):
        # Checking argument validity
        query = query.strip()
        check_query_arguments(query, orientation, size, None, locale)  # No such parameter as color for video
        if per_page > 80 or per_page < 1:
            raise PexelsSearchError("per_page parameter must be in between 1 and 80 inclusive")

        if page < 1:
            raise PexelsSearchError("page parameter must be at least 1")

        # Making request
        request_url = ENDPOINTS["SEARCH_VIDEOS"] + get_query_parameters(
            query=query,
            orientation=orientation,
            size=size,
            locale=locale,
            page=page,
            per_page=per_page
        )
        response = self.get_https_response(request_url)
        results = response.json()

        # Returning data and updating rate limit values
        self.update_rate_limit_attributes(response)
        return PexelsQueryResults(
            _content=[PexelsVideo(x) for x in results["videos"]],
            _url=request_url,
            _total_results=results["total_results"],
            _page=results["page"],
            _per_page=results["per_page"]
        )

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

