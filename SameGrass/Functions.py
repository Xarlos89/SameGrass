import pandas as pd
import logging

logging.basicConfig(level=logging.WARNING)

df = pd.read_excel('PopulationData.xlsx', header=[0])

def Max_Population(MaxPop):
	logging.info("Max Population set to: {}".format(MaxPop))

	for row in range(0,len(df)):
		city = df.iloc[row]['City']
		state = df.iloc[row]['State']
		currentPop = df.iloc[row][2019]
		if currentPop < int(MaxPop):
			print("City: {}\nState: {}\nPopulation: {}\n".format(city,state,currentPop))

def Minimum_Population(MinPop):
	logging.info("Minimum Population set to: {}".format(MinPop))

	for row in range(0,len(df)):
		city = df.iloc[row]['City']
		state = df.iloc[row]['State']
		currentPop = df.iloc[row][2019]
		if currentPop > int(MinPop):
			print("City: {}\nState: {}\nPopulation: {}\n".format(city,state,currentPop))

def Population_Between(MinPop,MaxPop):
	logging.info("Population set to between {} and {}".format(MinPop,MaxPop))

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


# Max_Population(10)
# Minimum_Population(2000000)
# Population_Between(1000000, 2000000)
# Search_City('Los')
# Search_State_MinMax('California', 1000000, 30000000)






