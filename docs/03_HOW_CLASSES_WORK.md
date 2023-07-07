# How are classes used and structured?
Now that you have been informed on how to use a `PexelsSession` class, you are already basically already set to do whatever you want, free to explore the methods provided by the wrapper.<br>
However, it is also useful to learn how the wrapper's classes themselves are structured. GetFromPexels code follows the Object-Oriented-Programming paradigm, so classes are a vital element of the code.<br>
Note that this documentation assumes you are aware of what classes and objects are. If you are not, then it's strongly advised you research them before reading further into this file.<br><br>
All classes are structured simply, and they can also be understood simply by viewing their code.

## Classes
### Photos
Every photo returned by the wrapper's methods is structured as a `PexelsPhoto` class, which stores the following attributes:
- `pexels_id`: The ID of the photo.
- `size`: A list containing the width and height of the photo in pixels.
- `pexels_url`: The URL to the photo on Pexels.
- `average_color`: The average color of the photo. This can be useful as a placeholder, solid color that replaces the image as it loads.
- `photographer`: A User object which stores information about the photographer of the image.
- `links`: A dictionary containing direct links to the files of the photo in various sizes.
- `is_liked`: Whether the photo is liked by the user whose API key is being used. Sometimes this variable is None depending on the method that retrieves the photo.
- `alt_text`: Alt text of the image (useful for people with disabilities).

To download a photo, the `download()` method can be used in a `PexelsPhoto` object.

### Videos (incl. video pictures and files)
Every video returned by the wrapper's methods is structured as a `PexelsVideo` class, which stores the following attributes:
- `pexels_id`: The ID of the video.
- `size`: A list containing the width and height of the video in pixels.
- `pexels_url`: The URL to the video on Pexels.
- `screenshot_url`: A URL to a screenshot of the video, which can be used as a thumbnail.
- `duration`: The duration of the video in seconds.
- `owner`: A User object which stores information about the uploader of the video.
- `video_files`: A list containing `PexelsVideoFile` objects.
- `video_pictures`: A list containing `PexelsPicture` objects.

Notice that this class contains some attributes that are different to the ones in the photo class. Additionally, there are 2 extra classes: `PexelsVideoFile` and `PexelsPicture`.
The extra classes both contain less information than the main `PexelsVideo` class itself.<br><br>
`PexelsVideoFile` objects contain the following attributes:
- `pexels_id`: The ID of the video file.
- `quality`: Either "sd" (Standaard Definition) or "hd" (High Definition).
- `file_type`: The type of the file.
- `file_extension`: The extension of the file derived from the type.
- `size`: A list containing the width and height of the video in pixels.
- `fps`: The number of frames per second in the video file.
- `url`: A URL to the video file hosted on Vimeo.

Video files can be downloaded with the `download()` method, just like `PexelsPhoto` objects. This means that to download a video, you must download one of its video files instead.<br><br>
Pexels video pictures, on the other hand, are just pictures that offer a preview of the video. The `PexelsVideoPicture` class is a dataclass with only 2 attributes: `pexels_id`, the ID
of the preview picture, and `picture_url`, the direct link to the picture.

### Collections
Collections are represented with a `PexelsCollection` dataclass object. These contain the following attributes:
- `pexels_id`: The ID of the collection.
- `title`: The collection's title.
- `description`: The collection's description.
- `is_private`: Whether the collection is private or not.
- `media_count`: The total amount of media in the collection, photos and videos, in other words.
- `photo_count` The total amount of photos included in the collection.
- `video_count` :The total amount of videos included in the collection.

### Users
A Pexels user is represented with a dataclass object like a collection too, with the `PexelsUser` dataclass. Note that a `PexelsUser` object is not returned by a method from `PexelsSession`,
and instead the user object is an attribute for a photo, video, or collection. `PexelsUser` contains the following attributes:
- `name`: The name of the user.
- `url`: The URL for the user's profile.
- `pexels_id`: The ID of the user.
- `username`: The user's username, which starts with an @ symbol.

## Query results
Specific methods of session objects that search for several media always return a `PexelsQueryResults` dataclass object which acts as an extended container, similar to a list. They contain
the following attributes:
- `content`: A list containing `PexelsPhoto`, `PexelsVideo`, or `PexelsCollection` objects that were retrieved from the query.
- `url`: The URL of the query made from the method and its arguments.
- `total_results`: The total amount of results received from the query.
- `page`: The page number of the query.
- `per_page`: The amount of media that was retrieved.

## Further details?
If you wish to find further details on the classes and their methods, it is strongly recommended to browse the specific markdown documents in the directory that serve as additional
documentation, or you can look in the code yourself.

# Where do I go from this?
Look at the next numbered `.md` file that comes after this one if you wish to continue reading about how to use this project.<br>
Alternatively, you can look at the `.md` files that aren't numbered. They will contain documentation for their respective classes instead.
