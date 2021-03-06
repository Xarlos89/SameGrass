import os
import sys
from Functions import *


def menu():
	menu = {}
	menu['1'] = "Search by Max Population"
	menu['2'] = "Search by Minimum Population"
	menu['3'] = "Search by Population between two numbers"
	menu['4'] = "Search by city name"
	menu['5'] = "Search by State with population between two numbers"
	menu['6'] = "Exit Program"
	
	while True:
		options = menu.keys()
		# options.sort()
		for entry in options:
			print("{}: {}".format(entry,menu[entry]))

		selection = str(input("\nWhat would you like to do?"))
		if selection == '1':
			os.system('clear')
			MaxPop = input('Enter the maximum population: ')
			print('Searching...')
			Max_Population(MaxPop)

		elif selection == '2':
			os.system('clear')
			MinPop = input('Enter the Minimum population: ')
			print('Searching...')
			Minimum_Population(MinPop)

		elif selection == '3':
			os.system('clear')
			MinPop = input('Enter the Minimum population: ')
			MaxPop = input('Enter the maximum population: ')
			radius = int(input('Enter the search radius (in miles): '))
			print('Searching...')
			Find_all_services_between_pops(MinPop,MaxPop,radius)

		elif selection == '4':
			os.system('clear')
			CityName = input('Enter the name of the City: ')
			print('Searching...')
			Search_City(CityName)

		elif selection == '5':
			os.system('clear')
			StateName = input('Enter the name of the State: ')
			MinPop = input('Enter the Minimum population: ')
			MaxPop = input('Enter the maximum population: ')
			print('Searching...')
			Search_State_MinMax(StateName,MinPop,MaxPop)

		elif selection == '6':
			os.system('clear')
			sys.exit()

		else:
			print("\nYou have to choose an option between 1 and 6. \n")
			pass 