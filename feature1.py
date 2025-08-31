import json
import numpy as np
from matplotlib import pyplot as plt

bmw300251= open('bmw30025.json',)

bmw30025 = json.load(bmw300251)
data = bmw30025
#haendler = open('haendler.json')

#data1 = json.load(haendler)

#print(bmw30025[5])
print(type(data))
#print(data[0])
print(data[0]['title'])
#print(data[0]['previewImage'])
print(data[0]['price.total.amount'])
#print(data[0]['features'])
#print(data[0]['features'][0])

#kombi / limousine
print(data[0]['category'])
#model
print(data[0]['model'])

print(data[0]['attributes']['Mileage'])

print(data[0]['attributes']['Vehicle condition'])

print(data[0]['attributes']['Fuel'])

print(data[0]['attributes']['Transmission'])

print(data[0]['attributes']['Parking sensors'])
print(len(data[0]['features']))

for i in range(0,len(data[0]['features'])):
    print(data[0]['features'][i])



"attributes:"



"Category"
"Saloon""EstateCar""Limousine"


"Trim line"
"M Sport"
"m sport"
"Luxury Line"
"M Sportpaket"
"320 e M Sport"
"M-Sport "


"Mileage"
"19,428 km"

"Fuel"
"Diesel"
"Hybrid (petrol/electric), Plug-in hybrid"
"Petrol"


"Transmission"
"Automatic"
"Manual gearbox"


"Parking sensors"
"Self-steering systems, Camera, Front, Rear"

"Number of Seats" \
"5"





"features:"
"Adaptive Cruise Control"
"Distance warning system"
"Emergency brake assist"
"Speed limit control system"
"Traffic sign recognition"
"Blind spot assist"
"Lane change assist"

"Panoramic roof"

"Four-wheel drive"
"Rear wheel drive"





x= {"attributes": {
    "Vehicle condition": "Used vehicle",
    "Category": "Saloon",
    "Trim line": "M Sport"}}









#print(len(data))

#for i in range(0,len(data)):
#    print(data[i]['model'])