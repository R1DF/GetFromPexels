# PexelsPhoto
This document provides a small outline of the structure of the `PexelsPhoto` class.

# Attributes
## `pexels_id`
The ID of the photo on Pexels.

## `size`
A list containing the width and height of the photo, both as integers, measured in pixels.

## `pexels_url`
The URL to the photo in the Pexels website.

## `average_color`
The hex code of the average color spread out on the photo.

## `photographer`
A `PexelsUser` object containing information about the photo's photographer on Pexels.

## `links`
A dictionary containing several direct links to the file. The following keys are present, all of which give a specific size of the same photo:
- `original`
- `large`
- `large_2x`
- `medium`
- `small`
- `portrait`
- `landscape`
- `tiny`

## `is_liked`
A boolean variable that shows whether the photo is liked by the user whose API key is being used. **However**, if the photo is returned from a search function, the value is `None` because the API
seems to constantly return `false` in that case.

## `alt_text`
The alt text for the image, useful for those with disabilities.

# Methods
## download(path, size)
Downloads the image as a .JPG file. An optional `size` argument can be passed to indicate a desired size.

### Parameters
`path: str`: The path to the file. Do not add the extension as the method will do it for you.<br>
`size: str [optional, default: "original"]`: The size of the photo you wish to download. The size must be a valid key of the `links` attribute shown above.
