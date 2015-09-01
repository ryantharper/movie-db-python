import urllib2 as u
import urllib
import json, sys, os
from subprocess import call

os.remove("/home/ryan/python/tvtext/tvshows.txt")
os.remove("/home/ryan/python/tvtext/episodes.txt")

def fullTv():
  path= '/home/ryan/python/tv/'
  tvList = os.listdir(path)
  print tvList

  dbHd = ['Title', 'Plot', 'imdbRating', 'imdbID']

  f = open("/home/ryan/python/tvtext/tvshows.txt", "a")

  def searchTvFull(tv):
    tv = tv.replace(" ", "+")
    url = "http://www.omdbapi.com/?t=%s&plot=full&r=json" % tv
    res = u.urlopen(url)
    res = json.loads(str(res.read()))
    imgN = "/var/www/html/images/" + res["Title"] + ".jpg"
    for e in dbHd:
      f.write(res[e] + "\t")
    urllib.urlretrieve(res["Poster"], imgN)
  	

  for zy, yz in enumerate(tvList):
    f.write("\N \t" + str(zy) + "\t")
    searchTvFull(yz)
    f.write("\n")
    seTv(yz)
  f.close()

def seTv(show):
  pat = '/home/ryan/python/tv/'
  pat = pat + show
  epList = os.listdir(pat)
  fileP = "/home/ryan/python/tvtext/episodes.txt"
  f = open(fileP, "a")
  print epList
  hdrs = ['Title', 'Plot', 'imdbRating', 'Season', 'Episode', 'seriesID']
  def searchTvSe(ep):
    ep = str(ep)
    seq = ep.replace(".mp4", "")
    print seq
    seq = seq.split(";")
    print seq
    tit = seq[0]
    seq[0] = seq[0].replace(" ", "+")
    url = "http://www.omdbapi.com/?t=%s&Season=%s&Episode=%s&plot=full&r=json" % (seq[0], seq[1], seq[2])
    respo = u.urlopen(url)
    respo = json.loads(str(respo.read()))
    if not os.path.exists("/var/www/html/images/"+tit):
      os.makedirs("/var/www/html/images/"+tit)
    imgNa = "/var/www/html/images/" + tit + "/" + respo["Title"] + ".jpg";
    for af in hdrs:
      print respo[af]
      f.write(respo[af] + "\t")
      urllib.urlretrieve(respo["Poster"], imgNa)
    xa = "/home/ryan/python/tv/" + tit + "/" + tit + ";" + respo["Season"] + ";" + respo["Episode"] + ".mp4"
    xb = "/var/www/html/vids/" + tit + ";" + respo["Season"] + ";" + respo["Episode"] + ".mp4"
    call(["mv", xa, xb])
  for co, tt in enumerate(epList):
    f.write("\N \t" + str(co) + "\t")
    searchTvSe(tt)
    f.write("\n")
  #f.close()

fullTv()
