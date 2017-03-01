"""
  Name: entertainment_center.py
  Description: The main program to populate movies and tv series data.
  Modify History:
"""

import media
import fresh_tomatoes

# Avatar movie trailer
avatar = media.Movie("Avatar", "Future Marine on alien world",
                     "http://avatarblog.typepad.com/.a/6a0120a6b2c140970c012876c79e1a970c-800wi",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# The third Toy Story movie trailer
toy_story = media.Movie("Toy Story 3", "Toys become life!",
                        "http://www.movienewz.com/img/films/toy-story-4-poster.jpg",
                        "https://www.youtube.com/watch?v=2BlMNH1QTeE")

# The first Independence Day movie trailer
independence_day = media.Movie("Independence Day (1996)",
                               "Alien come to earth to conqur",
                               "https://upload.wikimedia.org/wikipedia/en/5/58/Independence-Day-2-poster.jpg",
                               "https://www.youtube.com/watch?v=B1E7h3SeMDk")

# Ratatouille movie trailer (my favorite!)
ratatouille = media.Movie("Ratatouille", "If mouse can cook, I can cook too.",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=niD-jahFURU")

# Tansformers (2017) movie trailer
transformers_last_knight = media.Movie("Transformers: The Last Knight (2017)",
                                       "Michael Bay Movie 2017",
                                       "https://i0.wp.com/media2.slashfilm.com/slashfilm/wp/wp-content/images/transformers-the-last-knight-poster.jpg",
                                       "https://www.youtube.com/watch?v=AntcyqJ6brc")

# Power Ranger (2017) movie trailer
power_ranger = media.Movie("Power Rangers (2017)", "Power Rangers (2017)",
                           "http://dailydead.com/wp-content/uploads/2016/06/Power-Rangers-2017-poster.jpg",
                           "https://www.youtube.com/watch?v=5kIe6UZHSXw")

# Iron Fist TV series from Netflex movie trailer
iron_fist = media.TvClips("Iron Fist Season 1 Trailer (NETFLIX)", "ONE Media",
                          "http://cdn3-www.comingsoon.net/assets/uploads/2016/10/ironfistposterheader1.png",
                          "https://www.youtube.com/watch?v=nQR828clIAc")

# video clip list
movies = [avatar, toy_story, independence_day, ratatouille,
          transformers_last_knight, power_ranger, iron_fist]

# Generate HTML with supplied movies list
# Thank you adarsh0806!
fresh_tomatoes.open_movies_page(movies)
