
import json
import numpy as np
from matplotlib import pyplot as plt
bmw300251= open('m3comp.json',)
bmw30025 = json.load(bmw300251)
data1 = bmw30025

bmw3er=open("bmw30025.json")
bmw3er1=json.load(bmw3er)
data=bmw3er1


def is318i(i):
    if "Fuel" in i["attributes"] and "model" in i:
        if i["attributes"]["Fuel"] == "Petrol" or i["attributes"]["Fuel"] == "Petrol, E10-enabled":
            if i["model"]=="318":
                return True
    else:
        return False

def is318d(d):
    if "Fuel" in i["attributes"] and "model" in i:
        if i["attributes"]["Fuel"] == "Diesel":
            if i["model"]=="318":
                return True
    else:
        return False


def is320i(i):
    if "Fuel" in i["attributes"] and "model" in i:
        if i["attributes"]["Fuel"] == "Petrol" or i["attributes"]["Fuel"] == "Petrol, E10-enabled":
            if i["model"]=="320":
                return True
    else:
        return False

def is320d(d):
    if "Fuel" in i["attributes"] and "model" in i:
        if i["attributes"]["Fuel"] == "Diesel":
            if i["model"]=="320":
                return True
    else:
        return False

def is320e(d):
    if "Fuel" in i["attributes"] and "model" in i:
        if "Hybrid" in i["attributes"]["Fuel"]:
            if i["model"]=="320":
                return True
    else:
        return False

def is330i(i):
    if "Fuel" in i["attributes"] and "model" in i:
        if i["attributes"]["Fuel"] == "Petrol" or i["attributes"]["Fuel"] == "Petrol, E10-enabled":
            if i["model"]=="330":
                return True
    else:
        return False

def is320i(i):
    if "Fuel" in i["attributes"] and "model" in i:
        if i["attributes"]["Fuel"] == "Petrol" or i["attributes"]["Fuel"] == "Petrol, E10-enabled":
            if i["model"]=="320":
                return True
    else:
        return False

def is320d(d):
    if "Fuel" in i["attributes"] and "model" in i:
        if i["attributes"]["Fuel"] == "Diesel":
            if i["model"]=="320":
                return True
    else:
        return False

def is320e(d):
    if "Fuel" in i["attributes"] and "model" in i:
        if "Hybrid" in i["attributes"]["Fuel"]:
            if i["model"]=="320":
                return True
    else:
        return False

def is330i(i):
    if "Fuel" in i["attributes"] and "model" in i:
        if i["attributes"]["Fuel"] == "Petrol" or i["attributes"]["Fuel"] == "Petrol, E10-enabled":
            if i["model"]=="330":
                return True
    else:
        return False

def is330d(d):
    if "Fuel" in i["attributes"] and "model" in i:
        if i["attributes"]["Fuel"] == "Diesel":
            if i["model"]=="330":
                return True
    else:
        return False

def is330e(d):
    if "Fuel" in i["attributes"] and "model" in i:
        if "Hybrid" in i["attributes"]["Fuel"]:
            if i["model"]=="330":
                return True
    else:
        return False



def isM340d(i):

    if "Power" in i["attributes"]:
        if "340" in i["attributes"]["Power"]:
            return True

def isM340i(i):

    if "Power" in i["attributes"]:
        if "374" in i["attributes"]["Power"]:
            return True

    else :
        return False

def isM3(i):
    if "Power" in i["attributes"]:
        if "480" in i["attributes"]["Power"] or "550" in i["attributes"]["Power"]:
            return True
    else:
        return False

def isM3Competition(i):
    if "Power" in i["attributes"]:
        if "510" in i["attributes"]["Power"] or "530" in i["attributes"]["Power"]:
            return True
    else:
        return False

def modellzuordnung(auto):
    if isM340i(auto):
        return 5
    elif isM340d(auto):
        return 4
    else:
        return 0


def modellzuordnung(auto):
    if is320i(auto):
        return 6
    elif is320d(auto):
        return 7
    else:
        return 0

def modellzuordnung(auto):
    if is318i(auto):
        return "318i"
    elif is318d(auto):
        return "318d"
    elif is320i(auto):
        return "320i"
    elif is320d(auto):
        return "320d"
    elif is320e(auto):
        return "320e"
    elif is330i(auto):
        return "330i"
    elif is330d(auto):
        return "303d"
    elif is330e(auto):
        return "330e"
    elif isM340i(auto):
        return "M340i"
    elif isM340d(auto):
        return "M340d"
    elif isM3(auto):
        return "M3"
    elif isM3Competition(auto):
        return"M3Competition"
    else:
        return ("")


for i in data1:
    print(modellzuordnung(i))