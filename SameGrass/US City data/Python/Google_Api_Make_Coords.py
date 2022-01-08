# This script was terrible. Gave me a ton of strings that I made into a list using Sublime and some handy "find and replace" tweaks. 


import requests
from apikey import apikey
from citylist import CityList

# pip install requests
# Google API Key: https://console.cloud.google.com/google/maps-apis/credentials
# CityList - A python list of City names and states. 

lats = []
longs = []
errors =[]

def get_GeoCoordinates(city):
	city = city + " USA" # Making sure Google searches properly. 
	# Link to google API. You will need your own API key for this. 
	url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query={}&key={}'.format(city.replace(" ", "%"),apikey)
	#Just in case, throw this in a try-except
	try:
		response = requests.request("GET", url).json() # Grab JSON from API. 
		print("Looking for: {}".format(city))
		try: # Try grabbing the Geolocation. A few cities do not have coordinates, so we except them with 0
			latitude = ((response['results'])[0])['geometry']['location']['lat']
			longitude = ((response['results'])[0])['geometry']['location']['lng']
			print("Latitude:{} --- Longitude: {}".format(latitude,longitude))
			lats.append(latitude)
			longs.append(longitude)
		except:
			latitude = 0
			longitude = 0
			print("Latitude:{} --- Longitude: {}".format(latitude,longitude))
			lats.append(latitude)
			longs.append(longitude)
	except:
		print('Error getting {}'.format(city))
		errors.append(city)


for city in CityList: # That's 19,400 something cities. Will take a while.
	get_GeoCoordinates(city)
zippedList = zip(CityList,lats,longs) # Make nested lists with info. 
print(errors)


with open("geocoords.txt", "w") as file: # Save that nested list. 
		for line in zippedList:
			file.write(str(line)+'\n')
	