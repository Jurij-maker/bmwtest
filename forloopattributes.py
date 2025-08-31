import json
import numpy as np
from matplotlib import pyplot as plt

bmw300251= open('m3.json',)

bmw30025 = json.load(bmw300251)
data = bmw30025

for i in data:
    if "Fuel" in i["attributes"]:
        print(i["attributes"]["Fuel"])
    if i["model"]:
        print(i["model"])


for i in data:
    print("Transmission" in i["attributes"])

def isM3(car):
    if "model" in car:
        if car["model"]=="M3":
            return True
    else:
        return False



print("")
print (isM3(data[0]))

def isM340i(car):
    if i["attributtes"]["Fuel"]=="Petrol" or i["attributtes"]["Fuel"]=="Petrol, E10-enabled":
        if i["attributes"]["Trim line"]== "Competition":
            return True

    else :
        return False


def isM340d(car):
    if i["attributtes"]["Fuel"] == "Diesel":
        if i["attributes"]["Trim line"] == "Competition":
            return True

    else:
        return False







