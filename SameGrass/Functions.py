from apikey import apikey
import pandas as pd
import requests

df = pd.read_excel('PopulationData.xlsx', header=[0])

################ DATABASE FUNCTIONS ################

# Find ALL cities with a max population of...
def Max_Population(MaxPop):
	for row in range(0,len(df)):
		city = df.iloc[row]['City']
		state = df.iloc[row]['State']
		currentPop = df.iloc[row][2019]
		if currentPop < int(MaxPop):
			
			print("City: {}\nState: {}\nPopulation: {}\n".format(city,state,currentPop))

# Find ALL cities with a min population of...
def Minimum_Population(MinPop):
	for row in range(0,len(df)):
		city = df.iloc[row]['City']
		state = df.iloc[row]['State']
		currentPop = df.iloc[row][2019]
		if currentPop > int(MinPop):
			list_to_search.append(city)
			print("City: {}\nState: {}\nPopulation: {}\n".format(city,state,currentPop))

# Find ALL cities with population between...
def Population_Between(MinPop,MaxPop):
	global output
	for row in range(0,len(df)):
		city = df.iloc[row]['City']
		state = df.iloc[row]['State']
		currentPop = df.iloc[row][2019]
		if int(MinPop) < currentPop < int(MaxPop):
			# list_to_search.append(city)
			output = "City: {}\nState: {}\nPopulation: {}\n".format(city,state,currentPop)
			return output
			# print("City: {}\nState: {}\nPopulation: {}\n".format(city,state,currentPop))

# Search by name of city.
def Search_City(CityName):
	try:
		print('Searching for: \"{}\"\n'.format(CityName))
		search = df.loc[df['City'].str.contains(CityName,case=False)]
		data = search[['City','State',2019]]
		for ind in data.index:
			place = data.loc[ind, "City"]
			state = data.loc[ind, "State"]
			currentPop = data.loc[ind, 2019]
			list_to_search.append(city)
			print("City: {}\nState: {}\nPopulation: {}\n".format(place,state,currentPop))
	except:
		print("No city containing \"{}\" was found.")

# Search by state with population between min and max. 
def Search_State_MinMax(StateName,MinPop,MaxPop):
	try:
		print('Searching for: \"{}\" with a population between {} and {}\n'.format(StateName,MinPop,MaxPop))
		search = df.loc[df['State'].str.contains(StateName,case=False)]
		data = search[['City','State',2019]]
		for ind in data.index:
			currentPop = data.loc[ind, 2019]
			if int(MinPop) < currentPop < int(MaxPop):
				place = data.loc[ind, "City"]
				state = data.loc[ind, "State"]
				list_to_search.append(city)
				print("City: {}\nState: {}\nPopulation: {}\n".format(place,state,currentPop))
	except:
		print("No city containing \"{}\" was found with a population between {} and {}.".format(place,MinPop,MaxPop))

################ GOOGLE PLACES FUNCTIONS ################
# https://developers.google.com/maps/documentation/places/web-service/search-nearby#maps_http_places_nearbysearch-txt 

# Need Vars "place" and "miles" for these to work. 

# def get_GeoCoordinates(City):
# 	city = City + " USA"
# 	url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query={}&key={}'.format(city.replace(" ", "%"),apikey)
# 	response = requests.request("GET", url).json()
# 	latitude = ((response['results'])[0])['geometry']['location']['lat']
# 	longitude = ((response['results'])[0])['geometry']['location']['lng']
# 	CityReturned = city
# 	lats.append(latitude)
# 	longs.append(longitude)

# def nearby_search_HOSPITAL(latitude,longitude,distance):
# 	global has_Hospital_near
# 	distance = int(distance)*1609.344
# 	url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=Hospital&location={}%2C{}&radius={}&type=HOSPITAL&key={}'.format(str(latitude),str(longitude),str(distance),apikey)
# 	response = requests.request("GET", url).json()
# 	if len(response['results']) >= 1:
# 		# print(("{} has a Hospital within {} miles.").format(CityReturned,miles))
# 		for i in response['results']:
# 			if 'Hospital' in i['name']:
# 				has_Hospital_near = True
# 	else:
# 		print("No hospital within {} miles of {}".format(miles,CityReturned))
# 		has_Hospital_near = False

# def nearby_search_AIRPORT(latitude,longitude,distance):
# 	global has_Airport_near
# 	distance = int(distance)*1609.344
# 	url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=Airport&location={}%2C{}&radius={}&type=AIRPORT&key={}'.format(str(latitude),str(longitude),str(distance),apikey)
# 	response = requests.request("GET", url).json()
# 	if len(response['results']) >= 1:
# 		# print(("{} has an Airport within {} miles.").format(CityReturned,miles))
# 		for i in response['results']:
# 			if 'Airport' in i['name']:
# 				has_Airport_near = True
# 	else:
# 		print("No airport within {} miles of {}".format(miles,CityReturned))
# 		has_Airport_near = False

def Find_all_services_between_pops(MinPop,MaxPop,distance):
	list_to_search = []	# Make a list of palces to search.
	for row in range(0,len(df)): # Search ENTIRE excel doc.
		city = df.iloc[row]['City']
		state = df.iloc[row]['State']
		currentPop = df.iloc[row][2019]
		if int(MinPop) <= currentPop <= int(MaxPop): # if the current pop is between min and max...
			new_place = [] # Set up data for google API
			new_place.append(city)
			new_place.append(state)
			new_place.append(currentPop)
			
			list_to_search.append(new_place) # Send a list into a list. 

	meters = int(distance)*1609.344 # Quickmaths
	dist_in_miles = meters/1609.344 # Quickmaths
	for i in enumerate(list_to_search):
		# Get latitude and Longitude
		url_LatLong = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query={}&key={}'.format(i[1][0].replace(" ", "%"),apikey)
		response = requests.request("GET", url_LatLong).json()
		latitude = ((response['results'])[0])['geometry']['location']['lat']
		longitude = ((response['results'])[0])['geometry']['location']['lng']

		# Search lat and long for hospitals, airports... within the radius.
		url_hospital = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=Hospital&location={}%2C{}&radius={}&type=HOSPITAL&key={}'.format(str(latitude),str(longitude),str(meters),apikey)
		url_airport = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=Airport&location={}%2C{}&radius={}&type=AIRPORT&key={}'.format(str(latitude),str(longitude),str(meters),apikey)
		response_hospital = requests.request("GET", url_hospital).json()
		response_airport = requests.request("GET", url_airport).json()

		# If the hospitals, airports are found, say they are...
		if len(response_hospital['results']) >= 1:
			has_Hospital_near = 'Yes'
		else:
			has_Hospital_near = 'No'

		if len(response_airport['results']) >= 1:
			has_airport_near = 'Yes'
		else:
			has_airport_near = 'No'
		
		# Make it pretty and print that shit. 
		print("City: {}\nState: {}\nPopulation: {}\n\nWithin {} miles...\nHospital: {}\nAirport: {}\n".format(i[1][0],i[1][1],i[1][2],dist_in_miles,has_Hospital_near,has_airport_near))
		return output





