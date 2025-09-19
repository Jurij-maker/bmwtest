import json
import numpy as np
from matplotlib import pyplot as plt

bmw300251= open('luxuryline.json',)

bmw30025 = json.load(bmw300251)
data = bmw30025
def fuel():
    for i in data:
        if "Fuel" in i["attributes"]:
            print(i["attributes"]["Fuel"])
        if i["model"]:
            print(i["model"])

def transmission():
    for i in data:
        print("Transmission" in i["attributes"])

    def isM3(car):
        if "model" in car:
            if car["model"]=="M3":
                return True
        else:
            return False

def karosserie(cars):
    for i in cars:
        print(i["category"])



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


karosserie(bmw30025)




