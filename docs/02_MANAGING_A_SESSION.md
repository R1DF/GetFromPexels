# Using GetFromPexels
Now that you have GetFromPexels installed, you are now ready to use the library and use the Pexels API easily! ... Well, if you have an API key that is.

## API key? What's that and how do I get one?
To interact with an API, you need to have a key that is provided you. This is like a security measure to ensure people who are allowed to use the API can use it, while bad actors are
left without the ability to do so. Some services restrict API access completely or allow it only after application processes, but thankfully, Pexels allows anyone with an account to use
its API!<br><br>
This means you must create a Pexels acccount, and you will be able to make your API key right in their website.

# Creating a PexelsSession object
GetFromPexels provides a `PexelsSession` class which will be used to access the API, having methods which do so. To create a `PexelsSession` instance, you must also add one argument to
the constructor - The API key that you're using. This is not actually mandatory, but without a key, the instance will be useless. You can set or change the key with the `set_key()` method at
any time.

```py
from getfrompexels import PexelsSession

# Option 1
session_1 = PexelsSession("[INSERT RANDOM API KEY HERE]")

# Option 2
session_2 = PexelsSession()
session_2.set_key("[INSERT ANOTHER API KEY]")
```

The code below shows you how to create a session with the 2 ways. Neither will change your experience, but option 1 is recommended.

# Using methods provided by the methods
Now with your session object, you can now use the Pexels API. The Pexels API provides a variety of endpoints (think of them as links that are used to get specific data) in this [link](https://www.pexels.com/api/documentation/), and
GetFromPexels allows them all to be used. Basic methods will be shown below, and the rest can be seen by going in the docstrings of the session.py file or in the specific markdown file `PexelsSession.md`.

## Finding a photo and printing out direct links to it
```py
from getfrompexels import PexelsSession

# Creating session
session = PexelsSession("[INSERT API KEY]")

# Getting photo
photo = session.find_photo(7403820)
print(photo.links["original"])
```

The code snippet above shows you how easy it is to find the link to a photo file stored by Pexels with its ID. The Pexels API provides a lot of sizes for hosted photos, returning them as a
dictionary. The snippet will print out the direct link to the file at its original size.

Output:
`https://images.pexels.com/photos/7403820/pexels-photo-7403820.jpeg`

## Finding a video and printing its URL on Pexels
```py
from getfrompexels import PexelsSession

# Creating session
session = PexelsSession(os.getenv("PEXELS_API_KEY"))

# Getting video
video = session.find_video(4463164)
print(video.pexels_url)
```

This code snippet finds a video, given its ID, just like the snippet above (but for a photo instead). However, the output is different because `pexels_url` it printed out instead, which
is the URL to the photo hosted on Pexels rather than a direct link to it.

Output:
`https://www.pexels.com/video/woman-painting-on-her-canvas-4463164/`

## Browsing and displaying curated photos
```py
from getfrompexels import PexelsSession

# Creating session
session = PexelsSession(os.getenv("PEXELS_API_KEY"))

# Getting photos
curated_photos = session.search_curated_photos(per_page=3)

for photo in curated_photos.content:
    print(photo.pexels_url)
```

This code snippet will search for photos curated by the Pexels team, and get 3 of them, the Pexels URLs of which will all be printed.<br>
Once again, the code isn't complicated at all. First,
the `search_curated_photos()` function will return a special `PexelsQueryResults` object which will contain all the photo objects needed in its `content` attribite. After that, a for loop is made
to cycle through all of these photo objects and links to them on Pexels get printed out.

Output (likely to be different, but 3 links to Pexels will be sent regardless):
```
https://www.pexels.com/photo/man-walking-and-posing-at-night-17412689/
https://www.pexels.com/photo/street-in-taipei-at-night-17349973/
https://www.pexels.com/photo/a-man-walking-in-snowy-mountains-17404194/
```


## Downloading photos and videos
```py
from getfrompexels import PexelsSession

# Creating session
session = PexelsSession(os.getenv("PEXELS_API_KEY"))

# Downloading specific photo
photo = session.find_photo(615306)
photo.download("photo_file")

# Downloading specific video
video = session.find_video(854982)
video.video_files[0].download("video_file")
```

This code snipped will not return anything to the terminal. However, it will save a photo and a video to your computer! Both photos and videos can be downloaded with the use of just
one single function, where its path is given (the extension must not be given, a default is applied). Notice that the video object has several `video_files` that can be downloaded. For now,
we can just download any of them. Video files are delved into more detail in `PexelsVideoFile.md`.

## Other functions?
As previously said, there are other methods. Here is a list of some others as of v1.0.0:
- `search_for_photos()`
- `search_for_videos()`
- `find_user_collections()`
- `find_collection_contents()`
This short list only provides some functions, and the full list can be seen in the code itself.

## Handling the rate limit
While using the Pexels API and the GetFromPexels wrapper may sound like a doorway to endless possibilities for projects that use Pexels, one factor must be considered, and that is the rate
limit. A rate limit controls how many requests are being sent, and when it is exceeded, forbids you from making any more requests for a certain amount of time.<br>
## What rate lmit does Pexels have?
Pexels sets a rate limit of 20,000 requests for a normal user per month, being constantly reset as each month passes. This means that you'd be able to consistently make 645 requests per day in a 31-day month.<br>
Note that you can also hit a limit if you make too many requests for a short period of time - This means you'll have to make your code wait longer between requests or simply decrease how many requests you make for a specific time.

## How many requests does one `PexelsSession` make?
The answer is a simple 1. One method - one request used. Every method will get one endpoint, add additional data that was supplied in the code, and make a request.

## How can I keep track of the rate limit in the code?
Every `PexelsSession` object has 3 attributes:
- `request_limit`: The maximum amount of requests you can make for a month. If you're a normal user, this should be equal to 20000.
- `requests_left`: How many requests you have left. Updates with each request.
- `requests_rollback_timestamp`: A UNIX timestamp that shows the date and time when your amount of requests left to make will be fully replenished.

## What if I exceed it in my code?
An exception will be raised as the Pexels API will return a `429` HTTP error.

# Where do I go from this?
Look at the next numbered `.md` file that comes after this one if you wish to continue reading about how to use this project.<br>
Alternatively, you can look at the `.md` files that aren't numbered. They will contain documentation for their respective classes instead.
