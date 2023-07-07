# More information on downloading files
This is the last numbered markdown file in the `/docs/` directory. There will be nothing but a bit of extra information provided about downloading media with GetFromPexels.

## Downloading a photo
As demonstrated before, downloading a photo is very simple. Simply use the `download(path)` method to download a photo file from a `PexelsPhoto` object. You must supply the path of the
file, and you may also choose an additional size out of the following:
- original
- large
- large_2x
- medium
- small
- portrait
- landscape

For example. the following snippet will download a large version of a specific photo:
```py
from getfrompexels import PexelsSession
session = PexelsSession("[INSERT API KEY]")

photo = session.find_photo(16750660)
photo.download("randomly_found_photo", "large")
```

By default, the size is "original". Notice that the file extension is left out in the path.

## Downloading a video
Because each uploaded video gets a range of video files on Pexels, there is a range of video files available for download. This also means that instead of looking in a `PexelsVideo`
object for a download method, you must instead search inside the video files for that object and download one of them.

```py
from getfrompexels import PexelsSession
session = PexelsSession("[INSERT API KEY]")

video = session.find_video(16750660)
video_files = video.video_files
video_files[0].download("randomly_found_video")
```

The code snippet above finds the first given video file of a specific video and downloads it. Notice that there is no optional "size" option and the path must be supplied, without the
extension again.

### Which video file to choose?
Each video file varies in size, which are specifically with and height in pixels. Also, the quality of video files is not all the same, meaning that a video file can either be of HD or
of SD quality. However, they have a constant FPS rate. It is possible to implement your own function to download the video file of a specific quaality and an optimal size.

# What next?
You are free to experiment or apply GetFromPexels however you wish. Any further documentation will be provided in the code.
