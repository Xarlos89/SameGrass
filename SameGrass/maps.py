# https://developers.google.com/maps/documentation/places/web-service/search-nearby#maps_http_places_nearbysearch-txt 
from apikey import apikey
import requests

base = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json'
fields = '?fields=name%2Cformatted_address'
SearchQuery = '&input=hospital&inputtype=textquery'
location =  '&locationbias=circle%3A10000%47.06667%2C15.4395'
apikey = '&key=AIzaSyD0g_nCOzeLRN2psdIqreZ0mkkdJVXQl8w'
url = base+fields+SearchQuery+location+apikey

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

