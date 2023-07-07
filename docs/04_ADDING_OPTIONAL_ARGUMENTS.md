# Adding arguments to methods
The second file explained how a `PexelsSession` object is used to make requests tot he API, and the third documentation file went in more depth about how GetFromPexels represents
information, using OOP. This file will go back to the methods provided by the `PexelsSession` class, but also give more detail into the arguments that can be passed into functions.

## "Find" functions
Find functions are those which will retrieve data when given an ID. For example `find_photo()` and `find_video()` are both find functions because they require the ID of the media in
question to retrieve data. `find_collection_contents()`, despite returning several pieces of information, also count as find functions because they need
a specific ID of a collection. `find_user_collections` is also a find function.<br>

`find_photo()` and `find_video()` take no arguments other than the ID of the content that is to be found. However, the find functions below accept some (albeit small amount of) optional
arguments:
- `find_user_collections(page, per_page)`: `page` is which page to retrieve, and `per_page` is how many collections to show.
- `find_collection_contents(collection_id, media_type=None, page=1, per_page=15)`: `media_type` is either "photos" or "videos" and it filters out the media (can be left empty to have no
filter), `page` is which page to retrieve, and `per_page` is the amount of media to show.

## "Search" functions
Search functions retrieve data when they're given a specific query. Instead of focusing on one photo, image, or collection, they instead fetch several media (or collections) for the user
to handle. Most search functions accept a wide range of optional arguments.
- `search_curated_photos(page, per_page)`: `page` is which page to retrieve, and `per_page` is how many photos to show.
- `search_popular_videos(min_width, min_height, min_duration, max_duration, page, per_page)` `min_width` and `min_height` are the minimum width and height required for the videos
respectively in pixels, meanwhile `min_duration` and `max_duration` set the boundaries for how long the video should be in seconds. `page` is which page to retrieve, and `per_page` is
how many videos to show.
- `search_featured_collections(page, per_page)`: `page` is which page to retrieve, and `per_page` is how many collections to show.
- `search_for_photos(query, orientation, size, color, locale, page, per_page)`: `orientation` can either be "landscape", "portrait", or "square" (or left unassigned); `size` can either
be "small", "medium", "square" (or left unassigned; `color` can be a hex value or a specific one (depending on the name); `locale` is the optionally specified locale of the query; `page`
is which page to retrieve, and `per_page` is the amount of photos to show.
- `search_for_videos(query, orientation, size, locale, page, per_page)`: `orientation` can either be "landscape", "portrait", or "square" (or left unassigned); `size` can either
be "small", "medium", "square" (or left unassigned; `locale` is the optionally specified locale of the query; `page` is which page to retrieve, and `per_page` is the amount of videos
to show.

# Where do I go from this?
Look at the next numbered `.md` file that comes after this one if you wish to continue reading about how to use this project.<br>
Alternatively, you can look at the `.md` files that aren't numbered. They will contain documentation for their respective classes instead.
