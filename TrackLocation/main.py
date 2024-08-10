import phonenumbers
import opencage
from myphone import number
import folium

from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number, 'IN')
location = geocoder.description_for_number(pepnumber, "en")
print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number, 'IN')
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode

key = '9d5471f7cf5349a0893558f190634c7e'

geocoder = OpenCageGeocode(key)

query = str(location)
results = geocoder.geocode(query)
# print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)
myMap.save("mylocation.html")



# Designed by:- Abhishek Kumar
