"""
  Name: media.py
  Descriptions: The is the custom Class repository.
  Modify History:
"""

"""
  Description: 'Media' is the parent Class of Movie() and TvClips()
    It contains the 3 basic attributes of objects that will be used in
    fresh_tomatoes -> open_movies_page(movies) function
"""
class Media():
    def __init__(self,movie_title,poster_img_url,trailer_youtube_url):
        self.title = movie_title
        self.poster_image_url = poster_img_url
        self.trailer_youtube_url = trailer_youtube_url

"""
  Description:
    1. subclass of 'Media'
    2. add attribute of 'story_line'
"""
class Movie(Media):
    def __init__(self,a_movie_title,a_movie_storyline, a_poster_img_url,
                 a_trailer_youtube_url):
        self.storyline = a_movie_storyline
        self.title = a_movie_title
        self.poster_image_url = a_poster_img_url
        self.trailer_youtube_url = a_trailer_youtube_url

"""
  Description:
    1. subclass of 'Media'
    2. add attribute tv_station
"""
class TvClips(Media):
    def __init__(self,a_tv_series_name, a_tv_station, a_poster_img_url,
                 a_trailer_youtube_url):
        self.tv_station = a_tv_station
        self.title = a_tv_series_name
        self.poster_image_url = a_poster_img_url
        self.trailer_youtube_url = a_trailer_youtube_url




