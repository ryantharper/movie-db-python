import urllib2 as u
import urllib
import json, sys, os

def main():

  path = '/home/ryan/python/movies_folder'

  movieList = os.listdir(path)

  dbHeaders = ['Title', 'Year', 'Genre', 'Plot', 'imdbRating']

  f = open("/home/ryan/movies.txt", "w")   

  def searchMovie(film):
      film = film.replace(" ", "+")
      url = "http://www.omdbapi.com/?t=%s&plot=full&r=json" % film
      resp = u.urlopen(url)
      resp = json.loads(str(resp.read()))
      imgName = "/var/www/html/images/" + resp["Title"] + ".jpg"    
      for e in dbHeaders:
          f.write(resp[e] + "\t")

      urllib.urlretrieve(resp["Poster"], imgName)    


  for xy, movie in enumerate(movieList):
      f.write("\N \t" + str(xy)+ "\t")
      searchMovie(movie)
      f.write("\n")
  f.close()
main()

