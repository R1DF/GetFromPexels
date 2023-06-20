# Getting exceptions
from .custom_exceptions import PexelsAuthorizationError, PexelsAPIRequestError

# Response verifier (called by PexelsSession before returning anything)
def verify_response(response):
    status_code = response.status_code

    # Making sure the response is valid first
    if status_code == 200:
        return

    # Generating message for every request
    message = f"response returned HTTP {status_code} status code"
    match status_code:
        case 401:
            raise PexelsAuthorizationError("a valid API key must be provided for function call")

        case 403:
            message = "response returned HTTP 403 \"Forbidden\" status code"

        case 404:
            message = "response returned HTTP 404 \"Not Found\" status code"

        case 429:
            message = "response returned HTTP 429 \"Too Many Requests\" status code"

    if 500 <= response.status_code <= 599:
        raise PexelsAPIRequestError(f"response returned HTTP {status_code}, this is a server error")
    raise PexelsAPIRequestError(message)
