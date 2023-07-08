# PexelsVideo
This document provides a small outline of the structure of the `PexelsVideo` class.

# Attributes
## `pexels_id`
The ID of the video on Pexels.

## `size`
A list containing the width and height of the video, both as integers, measured in pixels.

## `pexels_url`
The URL to the photo in the Pexels website.

## `screenshot_url`
A direct link to a screenshot of the video.

## `duration`
The duration of the video in seconds.

## `owner`
A `PexelsUser` object containing information about the video's uploader on Pexels.

## `video_files`
A list of `PexelsVideoFile` objects for the video, **all of which allow the video to be downloaded.**

## `video_pictures`
A list of `PexelsVideoPicture` objects for the video.
