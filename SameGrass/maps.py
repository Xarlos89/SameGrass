# https://developers.google.com/maps/documentation/places/web-service/search-nearby#maps_http_places_nearbysearch-txt 

# Need Vars "place" and "miles" for these to work. 
import requests
from apikey import *


def get_place(City):
	global latitude
	global longitude
	global city
	city = City + " USA"
	url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query={}&key={}'.format(city.replace(" ", "%"),apikey)
	response = requests.request("GET", url).json()
	latitude = ((response['results'])[0])['geometry']['location']['lat']
	longitude = ((response['results'])[0])['geometry']['location']['lng']
	# print("Latitude: {}".format(latitude))
	# print("Longitude: {}".format(longitude))
	CityReturned = city
	return latitude,longitude,CityReturned

def nearby_search_HOSPITAL(latitude,longitude,distance):
	global has_Hospital_near
	distance = int(distance)*1609.344
	url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=Hospital&location={}%2C{}&radius={}&type=HOSPITAL&key={}'.format(str(latitude),str(longitude),str(distance),apikey)
	response = requests.request("GET", url).json()
	if len(response['results']) >= 1:
		# print(("{} has a Hospital within {} miles.").format(CityReturned,miles))
		for i in response['results']:
			if 'Hospital' in i['name']:
				has_Hospital_near = True
				# print(i['name'])
				# print(i['vicinity'])
				# print('\n')
	else:
		print("No hospital within {} miles of {}".format(miles,CityReturned))
		has_Hospital_near = False

def nearby_search_AIRPORT(latitude,longitude,distance):
	global has_Airport_near
	distance = int(distance)*1609.344
	url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=Airport&location={}%2C{}&radius={}&type=AIRPORT&key={}'.format(str(latitude),str(longitude),str(distance),apikey)
	response = requests.request("GET", url).json()
	if len(response['results']) >= 1:
		# print(("{} has an Airport within {} miles.").format(CityReturned,miles))
		for i in response['results']:
			if 'Airport' in i['name']:
				has_Airport_near = True
				# print(i['name'])
				# print(i['vicinity'])
				# print('\n')
	else:
		print("No airport within {} miles of {}".format(miles,CityReturned))
		has_Airport_near = False


###################### FOR TESTING ##############################

# City = input("What city? : ")
# miles = input("How far from the city center (In miles)? : ")

# get_place(City)
# nearby_search_HOSPITAL(latitude,longitude,miles)
# nearby_search_AIRPORT(latitude,longitude,miles)

# if has_Airport_near is True:
# 	print("Airport is True")
# else:
# 	print("Airport is False")

# if has_Hospital_near is True:
# 	print("Hospital is True")
# else: 
# 	print("Hospital is False")


		







