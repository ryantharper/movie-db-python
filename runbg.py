import os, time
import imdb_for_db

path = '/home/ryan/python/movies_folder'

files = os.listdir(path)
origLength = len(files)


while True:
    files = os.listdir(path)
    newL = len(files)
    if  newL > origLength or newL < origLength:
        print "File has been added"
	imdb_for_db.main()
    else:
        pass
    origLength = newL
    time.sleep(10)
    

