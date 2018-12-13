from time import sleep
import geopy
from geopy.geocoders import Nominatim
from sklearn.cluster import KMeans
import pygmaps.pygmaps

def geoGrab(address):
    geolocator = Nominatim(timeout=None, user_agent="my-application")
    location = geolocator.geocode(address)
    if location:
        loc = {}
        loc['latitude'] = location.latitude
        loc['longitude'] = location.longitude
        return loc
    else:
        return None

def placeFind(fileName):
    fw = open('places.txt', 'w')
    for line in open(fileName).readlines():
        place = line.split('\t')
        coord = geoGrab(place[1])
        if type(coord) is dict:
            fw.write(str(coord["latitude"]) + " " + str(coord["longitude"]) + "\n")
        else:
            fw.write("Error"+"\n")
        sleep(2)
    fw.close()

placeFind('almatyPlaces.txt')

def locationList():
    location = []
    for line in open("places.txt").readlines():
        line = line.replace("\n","")
        coord = line.split(' ')
        if(coord=='Error'):
            continue
        location.append([float(coord[0]), float(coord[1])])
    return location

def openGoogleMap(numberclust, labels):
    colors = ['#000000', '#555555', '#ffffff']
    openGoogleMap = pygmaps.maps(43.2294993,76.889709, a=12)
    for i in range(len(labels)):
        coord = location[i]
        openGoogleMap.addpoint(float(coord[0]), float(coord[1]), colors[labels[i]])
    openGoogleMap.draw('googlemap.html')


def clusterPlaces(numClust):
    kmeans = KMeans(n_clusters=numClust, random_state=123).fit(locationList())
    labels = kmeans.labels_
    openGoogleMap(numClust, labels)
clusterPlaces(3)