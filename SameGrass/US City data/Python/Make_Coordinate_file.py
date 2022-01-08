from geocoords import GeoCoordList

with open("Latitudes.txt", "w") as latFile:
	for index in range(0,len(GeoCoordList)):
		lats = GeoCoordList[index][1]
		latFile.write(str(lats)+ "\n")

with open("Longitudes.txt", "w") as longFile:
	for index in range(0,len(GeoCoordList)):
		longs = GeoCoordList[index][2]
		longFile.write(str(longs)+ "\n")