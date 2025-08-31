
import json
import numpy as np
from matplotlib import pyplot as plt
bmw300251= open('m3comp.json',)

bmw30025 = json.load(bmw300251)
data = bmw30025

def isM340d(i):
    if "Fuel" in i["attributes"] and "Trim line" in i["attributes"]:
        if i["attributes"]["Fuel"] == "Diesel":
            if "Competition" in i["attributes"]["Trim line"]:
                return True

    else:
        return False

def isM340i(i):
    if "Fuel" in i["attributes"] and "Trim line" in i["attributes"]:
        if i["attributes"]["Fuel"]=="Petrol" or i["attributes"]["Fuel"]=="Petrol, E10-enabled":
            if "Competition" in i["attributes"]["Trim line"]:
                return True
    else :
        return False

def modellzuordnung(auto):
    if isM340i(auto):
        return 5
    elif isM340d(auto):
        return 4
    else:
        return 0

for i in data:
    print(modellzuordnung(i))