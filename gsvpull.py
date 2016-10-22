import urllib, os
import numpy as np

myloc = r"" # location for your files here
key = "&key=" + "" # you can get a special API key from Google if you want, otherwise, play easy or google will get mad

def GetStreet(Add,SaveLoc):
  base = "https://maps.googleapis.com/maps/api/streetview?fov=110&size=640x400&location=" ## google maps API doesn't allow sizes over 640x640
  MyUrl = base + Add + key
  fi = Add + ".jpg"
  urllib.urlretrieve(MyUrl, os.path.join(SaveLoc,fi))

## You can load addresses into an array manually if you like, but I prefer to put them in a line seperated text file
addresses = open("addresses.dat","r")

## define the array
addressArray=[]

## go through each line of the datafile and build the array
for line in addresses.readlines():
	addressArray.append(line.rstrip('\n')) ## strips line break character

### I leave this on for debugging
# print addressArray

#### this iterates the array and snags images for each one, saves it to myloc
for i in addressArray:
  GetStreet(Add=i,SaveLoc=myloc)
