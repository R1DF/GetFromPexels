# PexelsVideoFile
This document contains information on the `PexelsVideoFile` class.

# Attributes
## `pexels_id`
The Pexels ID of the video file.

## `quality`
The quality of the video file, either `"hd"` or `"sd"`.

## `file_type`
The format of the video file. All video files appear to have the `videp/mp4` format.

## `file_extension`
The extension of the video derived from the format. All video files appeaar to have the `.mp4` file extension.

## `size`
A list containing the width and height of the video in pixels.

## `fps`
The amount of frames per second in the video file.

## `url`
A direct link to where the video file is being stored.

# Methods
## download(path)
Downloads the video file as a .MP4 file.

### Parameters
`path: str`: The path to the file. Do not add the extension as the method will do it for you.<br>
