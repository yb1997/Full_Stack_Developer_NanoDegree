# media.py
import webbrowser
# init initializes or creates space in memory for title, storyline and trailor 
# use """ for witing documentation
      
class Movie():
   """
         title: This contains title of movie.
         storyline: This contains description of movie.
         poster_image_url: This containes url of poster image for a movie.
         trailer_youtube_url: This contains youtube url for trailer of a movie.
    """
   VALID_RATINGS = ["G", "PG","PG-13", "R"]

   def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, rating, release_year):
      #Instance Variables
      self.title = movie_title       
      self.storyline = movie_storyline             
      self.poster_image_url = poster_image
      self.trailer_youtube_url = trailer_youtube
      self.rating = rating
      self.year = release_year

      #Instace Methods
#   def show_trailer(self):
#      webbrowser.open(self.trailer_youtube_url)
# access the variables through access keyword
