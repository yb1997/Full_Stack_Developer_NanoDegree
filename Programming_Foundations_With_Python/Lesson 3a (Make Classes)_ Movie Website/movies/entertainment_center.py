"""
list of movies that feed into fresh_tomatoes.py file
"""
import media   #I want to use the contents of previous file media.py
import urllib
import fresh_tomatoes

toy_story = media.Movie( "Toy Story",
000000000000000000000+99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888+9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                         "A story of a boy",
                         "https://goo.gl/RoywlF",
                         "https://youtu.be/KYz2wyBy3kc")

avatar = media.Movie( "Avatar",
                      "A marine on an alien planet",
                      "https://goo.gl/YC21CA",
                      "https://youtu.be/d1_JBMrrYw8")

three_idiots = media.Movie( "3 Idiots",
                            "This movie is Based on Chetan Bhagat's novel, Five Point Someone (though only a miniscule part has been adapted from the book; the rest is all original), here's a story of three friends studying in an engineering college Rancho (Aamir Khan), Farhan (R Madhavan) and Raju (Sharman Joshi).",
                            "https://goo.gl/hPvHWK",
                            "https://youtu.be/XQvcZWCacKE")

internship = media.Movie( "The Internship ",
                          "Two salesmen whose careers have been torpedoed by the digital age find their way into a coveted internship at Google, where they must compete with a group of young, tech-savvy geniuses for a shot at employment.",
                          "https://goo.gl/5Ex35x",
                          "https://youtu.be/NyfSMnMBGiM")

algorithm = media.Movie( " Algorithm: The Hacker Movie ",
                         "The new film Algorithm tracks the travails of Will, who is a freelance computer hacker who breaks into a top-secret government contractor and downloads all their recently developed programs. You can see the full movie below",
                         "https://goo.gl/sEJAIT",
                         "https://youtu.be/tyTUVovCp5s")
SOCIAL_NETWORK = media.Movie("Social Network",
                             "https://upload.wikimedia.org/wikipedia/en/",
                             "https://www.cinematerial.com/media/posters/md/rs/rs1m0mdj.jpg?v=1456719991",
                             
                             "https://www.youtube.com/watch?v=lB95KLmpLR4")

movies = [avatar,toy_story, three_idiots,internship, algorithm,SOCIAL_NETWORK ]
fresh_tomatoes.open_movies_page( movies )

print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)

