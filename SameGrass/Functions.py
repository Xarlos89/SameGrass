import pandas as pd
import requests

df = pd.read_excel('PopulationData.xlsx', header=[0])

################ DATABASE FUNCTIONS ################

def Max_Population(MaxPop):
	for row in range(0,len(df)):
		city = df.iloc[row]['City']
		state = df.iloc[row]['State']
		currentPop = df.iloc[row][2019]
		if currentPop < int(MaxPop):
			print("City: {}\nState: {}\nPopulation: {}\n".format(city,state,currentPop))

def Minimum_Population(MinPop):
	for row in range(0,len(df)):
		city = df.iloc[row]['City']
		state = df.iloc[row]['State']
		currentPop = df.iloc[row][2019]
		if currentPop > int(MinPop):
			print("City: {}\nState: {}\nPopulation: {}\n".format(city,state,currentPop))

def Population_Between(MinPop,MaxPop):
	for row in range(0,len(df)):
		city = df.iloc[row]['City']
		state = df.iloc[row]['State']
		currentPop = df.iloc[row][2019]
		if int(MinPop) < currentPop < int(MaxPop):
			print("City: {}\nState: {}\nPopulation: {}\n".format(city,state,currentPop))

def Search_City(CityName):
	try:
		print('Searching for: \"{}\"\n'.format(CityName))
		search = df.loc[df['City'].str.contains(CityName,case=False)]
		data = search[['City','State',2019]]
		for ind in data.index:
			place = data.loc[ind, "City"]
			state = data.loc[ind, "State"]
			currentPop = data.loc[ind, 2019]
			print("City: {}\nState: {}\nPopulation: {}\n".format(place,state,currentPop))
	except:
		print("No city containing \"{}\" was found.")

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
				print("City: {}\nState: {}\nPopulation: {}\n".format(place,state,currentPop))
	except:
		print("No city containing \"{}\" was found with a population between {} and {}.".format(place,MinPop,MaxPop))

################ GOOGLE PLACES FUNCTIONS ################
# https://developers.google.com/maps/documentation/places/web-service/search-nearby#maps_http_places_nearbysearch-txt 

# Need Vars "place" and "miles" for these to work. 

def get_place(City):
	global latitude
	global longitude
	global city
	city = City + " USA"
	url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query={}&key={}'.format(city.replace(" ", "%"),apikey)
	response = requests.request("GET", url).json()
	latitude = ((response['results'])[0])['geometry']['location']['lat']
	longitude = ((response['results'])[0])['geometry']['location']['lng']
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

	else:
		print("No airport within {} miles of {}".format(miles,CityReturned))
		has_Airport_near = False

# Max_Population(10)
# Minimum_Population(2000000)
# Population_Between(1000000, 2000000)
# Search_City('Los')
# Search_State_MinMax('California', 1000000, 30000000)

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






