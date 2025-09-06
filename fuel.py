import json
import numpy as np
from matplotlib import pyplot as plt


luxuryline = open('luxuryline.json')
luxuryline1 = json.load(luxuryline)


def printtrimline1(autos):
    for auto in autos:
        if "Fuel" in auto["attributes"]:
            print(auto["attributes"]["Fuel"])


def sonderausstattung1(i):
    trimlinemsport = ["M Sport", "m sport", "M sport", "M Sportpaket", "M-Sport", "msport", "MSport", "MSPORT", "M. Paket"]
    response = "normal"
    if "Trim line" in i["attributes"]:
        trimline = i["attributes"]["Trim line"]
        for a in trimlinemsport:
            if a in trimline:
                response = "msport"

    return response

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
    print(fuel(i))