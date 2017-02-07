"""
list of movies that feed into fresh_tomatoes.py file
"""
import media   #I want to use the contents of previous file media.py
import urllib
import ast  
import fresh_tomatoes

def get_movie_info( id ):
    connection = urllib.urlopen("http://www.omdbapi.com/?i=" + id +"&plot=short&r=json")  #Open the url
    output = connection.read()    
    values = ast.literal_eval(output)
    return values

# Passing Id the movie to the funtion which return it's details

values = get_movie_info("tt0435761")
toy_story = media.Movie( values.get('Title'),
                         values.get('Plot'),
                         values.get('Poster'),
                         "https://youtu.be/KYz2wyBy3kc",
                         values.get('imdbRating'),
                         values.get('Year') )

values = get_movie_info("tt0499549")
avatar = media.Movie(values.get('Title'),
                     values.get('Plot'),
                     values.get('Poster'),
                     "https://youtu.be/5PSNL1qE6VY",
                     values.get('imdbRating'),
                     values.get('Year') )    


values = get_movie_info("tt0295701")
xxx = media.Movie( values.get('Title'),
                   values.get('Plot'),
                   values.get('Poster'),
                   "https://youtu.be/Spx-Mx3xhYY",
                   values.get('imdbRating'),
                   values.get('Year')
                  )    


values = get_movie_info("tt1187043")
three_idiots = media.Movie( values.get('Title'),
                            values.get('Plot'),
                            values.get('Poster'),
                            "https://youtu.be/XQvcZWCacKE",
                            values.get('imdbRating'),
                            values.get('Year')
                          )    

values = get_movie_info("tt3405236")
raees = media.Movie(values.get('Title'),
                    values.get('Plot'),
                    values.get('Poster'),
                    "https://youtu.be/J7_1MU3gDk0",
                    values.get('imdbRating'),
                    values.get('Year')
                    )    

values = get_movie_info("tt1293847")
xxx_return = media.Movie(values.get('Title'),
                         values.get('Plot'),
                         values.get('Poster'),
                         "https://youtu.be/MQEFmHsseaU",
                         values.get('imdbRating'),
                         values.get('Year') )    

values = get_movie_info("tt4217392")
kung_fu_yoga = media.Movie(values.get('Title'),
                           values.get('Plot'),
                           values.get('Poster'),
                           "https://youtu.be/5KcwjfPdFC0",
                           values.get('imdbRating'),
                           values.get('Year') )    

values = get_movie_info("tt5460276")
kaabil = media.Movie( values.get('Title'),
                      values.get('Plot'),
                      values.get('Poster'),
                      "https://youtu.be/nubDFeiUAsI",
                      values.get('imdbRating'),
                      values.get('Year')
                     )    


values = get_movie_info("tt2234155")
internship = media.Movie(values.get('Title'),
                         values.get('Plot'),
                         values.get('Poster'),
                         "https://youtu.be/NyfSMnMBGiM",
                         values.get('imdbRating'),
                         values.get('Year')
                         )    

values = get_movie_info("tt3293462")
algorithm = media.Movie(values.get('Title'),
                        values.get('Plot'),
                        values.get('Poster'),
                        "https://youtu.be/tyTUVovCp5s",
                        values.get('imdbRating'),
                        values.get('Year') )    

values = get_movie_info("tt5074352")
dangal = media.Movie(values.get('Title'),
                     values.get('Plot'),
                     values.get('Poster'),
                     "https://youtu.be/x_7YlGv9u1g",
                     values.get('imdbRating'),
                     values.get('Year') )    

values = get_movie_info("tt1285016")
social_network = media.Movie(values.get('Title'),
                             values.get('Plot'),
                             values.get('Poster'),
                             "https://www.youtube.com/watch?v=lB95KLmpLR4",
                             values.get('imdbRating'),
                             values.get('Year')
                             )    

movies = [avatar,toy_story, xxx_return, dangal, kaabil, three_idiots, xxx, kung_fu_yoga, internship, raees, algorithm, social_network]
fresh_tomatoes.open_movies_page( movies )

#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
#print(media.Movie.__name__)
#print(media.Movie.__module__)

