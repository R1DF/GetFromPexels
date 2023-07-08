# PexelsSession
This document provides a small outline of the structure of the `PexelsSession` class.

# Attributes
## `key`
The Pexels API key that is being used in the requests made by the object.

## `request_limit`
The maximum amount of requests given to a user for month. Unless it's been negotiated with the Pexels team, this should be equal to 20,000.

## `requests_left`
The amount of requests left for the month for the user.

## `requests_rollback_timestamp`
The UNIX timestamp of the time when the amount of requests left for the user will be replenished.


# Methods
## set_key(key)

### Parameters
`key: str`: The new key that should be set as the API key used with the session object.

## find_photo(photo_id)
Returns a `PexelsPhoto` object containing data about a specific photo by its ID.
### Parameters
`photo_id: int`: The ID of the photo that you're looking for.

## find_video(video_id)
Returns a `PexelsVideo` object containing data about a specific video by its ID.
### Parameters
`video_id: int`: The ID of the video that you're looking for.

## search_curated_photos(page, per_page)
Returns a `PexelsQueryResults` object containing curated Pexels photos.
### Parameters
`page: int [optional, default: 1]`: The page number that is being requested.<br>
`per_page: int [optional, default: 15]`: The amount of photos to return from the query. There is a maximum of 80.

## search_popular_videos(min_width, min_height, min_duration, max_duration, page, per_page)
Returns a `PexelsQueryResults` object containing popular videos. This method allows filters that are passed as optional arguments.
### Parameters
`min_width: int [optional]`: The minimum width for each video in pixels.<br>
`max_width: int [optional]`: The maximum width for each video in pixels.<br>
`min_duration: int [optional]`: The minimum duration for each video in seconds.<br>
`max_duration: int [optional]`: The maximum duration for each video in seconds.<br>
`page: int [optional, default: 1]`: The page number that is being requested.<br>
`per_page: int [optional, default: 15]`: The amount of photos to return from the query. There is a maximum of 80.

## search_featured_collections(page, per_page)
Returns a `PexelsQueryResults` object containing featured collections.
### Parameters
`page: int [optional, default: 1]`: The page number that is being requested.<br>
`per_page: int [optional, default: 15]`: The amount of photos to return from the query. There is a maximum of 80.

## find_user_collections(page, per_page)
Returns a `PexelsQueryResults` object containing collections owned by the user whose API key is used.
### Parameters
`page: int [optional, default: 1]`: The page number that is being requested.<br>
`per_page: int [optional, default: 15]`: The amount of photos to return from the query. There is a maximum of 80.

## find_collection_contents(collection_id, media_type, page, per_page)
Returns a `PexelsQueryResults` object containing media inside a specific collection. This method allows the query to return only photos or videos, or both.
### Parameters
`media_type: str [optional]`: The type of media that is strictly wanted. Can either be `"photos"` or `"videos"`. If left empty, then the filter will not be applied.<br>
`page: int [optional, default: 1]`: The page number that is being requested.<br>
`per_page: int [optional, default: 15]`: The amount of photos to return from the query. There is a maximum of 80.

## search_for_photos(query, orientation, size, color, locale, page, per_page)
Submits a query for photos given the text for it and any optional filters, and then returns the photos that appear in a `PexelsQueryResults` object.
### Parameters
`query: str`: The query given for the search. Think of it as what you would type in the search bar.<br>
`orientation: str [optional]`: The desired orientation for the photos. Can be `"landscape"`, `"portrait"`, `"square"` or simply not given to allow any.<br>
`size: str [optional]`: The desired size of the photo. Can be `"large"` (24MP), `"medium"` (12MP), `"small"` (4MP), or simply not given to allow any.<br>
`color: str [optional]`: The desired color of the photo. Can either be a hex value (with the # symbol at the start), or part of the following list:
- `"red"`
- `"orange"`
- `"yellow"`
- `"green"`
- `"turquoise"`
- `"blue"`
- `"violet"`
- `"pink"`
- `"black"`
- `"gray"`
- `"white"`

`locale: str [optional]`: The locale of the search that you wish to be performed. Specifying it is optional. The supported locale praameters can be viewed [here](https://www.pexels.com/api/documentation/#photos-search__parameters__locale).<br>
`page: int [optional, default: 1]`: The page number that is being requested.<br>
`per_page: int [optional, default: 15]`: The amount of photos to return from the query. There is a maximum of 80.

## search_for_videos(query, orientation, size, locale, page, per_page)
Submits a query for videos given the text for it and any optional filters, and then returns the videos that appear in a `PexelsQueryResults` object.
### Parameters
`query: str`: The query given for the search. Think of it as what you would type in the search bar.<br>
`orientation: str [optional]`: The desired orientation for the photos. Can be `"landscape"`, `"portrait"`, `"square"` or simply not given to allow any.<br>
`size: str [optional]`: The desired size of the photo. Can be `"large"` (4K), `"medium"` (Full HD), `"small"` (HD), or simply not given to allow any.<br>
`color: str [optional]`: The desired color of the photo. Can either be a hex value (with the # symbol at the start), or part of the list given under the method above.
`locale: str [optional]`: The locale of the search that you wish to be performed. Specifying it is optional. The supported locale praameters can be viewed [here](https://www.pexels.com/api/documentation/#photos-search__parameters__locale).<br>
`page: int [optional, default: 1]`: The page number that is being requested.<br>
`per_page: int [optional, default: 15]`: The amount of photos to return from the query. There is a maximum of 80.
