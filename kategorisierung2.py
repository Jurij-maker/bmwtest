#from kategorisierung1 import modellzuordnung
import json
import numpy as np
from matplotlib import pyplot as plt
bmw300251= open('m3comp.json',)
bmw30025 = json.load(bmw300251)
data1 = bmw30025

bmw3er=open("bmw30025.json")
bmw3er1=json.load(bmw3er)
data=bmw3er1


def is320i(i):
    if "Fuel" in i["attributes"] and "model" in i:
        if i["attributes"]["Fuel"] == "Petrol" or i["attributes"]["Fuel"] == "Petrol, E10-enabled":
            if i["model"]=="320":
                return True
    else:
        return False


def is320d(i):
    if "Fuel" in i["attributes"] and "model" in i:
        if i["attributes"]["Fuel"] == "Diesel":
            if i["model"]=="320":
                return True
    else:
        return False


def modellzuordnung(auto):
    if is320i(auto):
        return 6
    elif is320d(auto):
        return 7
    else:
        return 0
