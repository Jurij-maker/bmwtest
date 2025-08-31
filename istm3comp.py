import json
import numpy as np
from matplotlib import pyplot as plt

bmw300251= open('m3comp.json',)

bmw30025 = json.load(bmw300251)
data = bmw30025




def isM340i(i):
    if "Fuel" in i["attributes"] and "Trim line" in i["attributes"]:
        if i["attributtes"]["Fuel"]=="Petrol" or i["attributtes"]["Fuel"]=="Petrol, E10-enabled":
            if i["attributes"]["Trim line"]== "Competition":
                return True

    else :
        return False


def isM340d(i):
    if "Fuel" in i["attributes"] and "Trim line" in i["attributes"]:
        if i["attributtes"]["Fuel"] == "Diesel":
            if i["attributes"]["Trim line"] == "Competition":
                return True

    else:
        return False


for i in data:
    if "Trim line" in i["attributes"]:
        if "Competition" in i["attributes"]["Trim line"]:
            print(i["attributes"]["Trim line"])


def ismodell(angebot):
    if isM340d(angebot):
        return 1
    if isM340i(angebot):
        return 2
