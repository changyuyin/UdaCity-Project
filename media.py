"""
  Name: media.py
  Descriptions: The is the custom Class repository.
  Modify History:
"""

class Media():
    """
      Description: 'Media' is the parent Class of Movie() and TvClips()
      Attributes:
           title(str): movie title
           poster_image_url(str): location of the movie poster
           trailer_youtube_rul(str): location of the video clip on Youtube
    """
    def __init__(self,movie_title,poster_img_url,trailer_youtube_url):
        self.title = movie_title
        self.poster_image_url = poster_img_url
        self.trailer_youtube_url = trailer_youtube_url

class Movie(Media):
    """
      Description:
        1. subclass of 'Media'
        2. add attribute of story_line(str): movie description
    """
    def __init__(self,a_movie_title,a_movie_storyline, a_poster_img_url,
                 a_trailer_youtube_url):
        self.storyline = a_movie_storyline
        self.title = a_movie_title
        self.poster_image_url = a_poster_img_url
        self.trailer_youtube_url = a_trailer_youtube_url


class TvClips(Media):
    """
      Description:
        1. subclass of 'Media'
        2. add attribute tv_station(str): name of tv station
    """
    def __init__(self,a_tv_series_name, a_tv_station, a_poster_img_url,
                 a_trailer_youtube_url):
        self.tv_station = a_tv_station
        self.title = a_tv_series_name
        self.poster_image_url = a_poster_img_url
        self.trailer_youtube_url = a_trailer_youtube_url



