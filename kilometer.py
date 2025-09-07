import json
import numpy as np
from matplotlib import pyplot as plt


luxuryline = open('luxuryline.json')
luxuryline1 = json.load(luxuryline)


def fuel(auto):
    if "Fuel" in auto["attributes"]:
        fuel = auto["attributes"]["Fuel"]
        if "Diesel" in fuel:
            return "Diesel"
        elif "Hybrid" in fuel:
            return "Hybrid"
        elif "Petrol" in fuel:
            return "Petrol"
        else:
            return ""
    else:
        return ""


for i in luxuryline1:
    print(i["attributes"]["Mileage"])


def mileagetoint(auto):
    kmstring="0"

    if "Mileage" in auto["attributes"]:
        mileage = auto["attributes"]["Mileage"]
        for i in mileage:
            if i.isdigit():
                kmstring = kmstring + i

    return int(kmstring)

for i in luxuryline1:
    print(mileagetoint(i))


def categorizekm(auto):
    km = mileagetoint(auto)
    if km <= 25000:
        return "<25"
    elif km <=50000:
        return "<50"
    elif km <=75000:
        return "<75"
    elif km <=100000:
        return "<100"
    else:
        return ">100"


for i in luxuryline1:
    print(categorizekm(i))