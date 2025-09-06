import json
import numpy as np
from matplotlib import pyplot as plt
bmw300251= open('m3comp.json',)
bmw30025 = json.load(bmw300251)

luxuryline = open('luxuryline.json')
luxuryline1 = json.load(luxuryline)

msport = open('msport.json')
msport1 = json.load(msport)

sportline = open('sportline.json')
sportline1 = json.load(sportline)




def is320d(i):
    if "Fuel" in i["attributes"] and "model" in i:
        if i["attributes"]["Fuel"] == "Diesel":
            if i["model"]=="320":
                return True
    else:
        return False
    i["attributes"]["Trim line"]

def printtrimline1(autos):
    for auto in autos:
        if "Trim line" in auto["attributes"]:
            print(auto["attributes"]["Trim line"])



def sonderausstattung(i):
    trimlinemsport=["M Sport", "m sport", "M sport", "M Sportpaket", "M-Sport"]
    if "Trim line" in i["attributes"]:
        if i["attributes"]["Trim line"] in trimlinemsport:
            return "msport" + " " + i["attributes"]["Trim line"]
        else:
            return "normal" + " " + i["attributes"]["Trim line"]


    else:
        return "normal"

def sonderausstattung1(i):
    trimlinemsport = ["M Sport", "m sport", "M sport", "M Sportpaket", "M-Sport", "msport", "MSport", "MSPORT", "M. Paket"]
    response = "normal"
    if "Trim line" in i["attributes"]:
        trimline = i["attributes"]["Trim line"]
        for a in trimlinemsport:
            if a in trimline:
                response = "msport"

    return response

def sonderausstattung2(i):
    trimlinemluxury = ["Luxury Line", "luxury line", "Luxury line", "Luxury-Line"]
    response = "normal"
    if "Trim line" in i["attributes"]:
        trimline = i["attributes"]["Trim line"]
        for a in trimlinemluxury:
            if a in trimline:
                response = "luxuryline"

    return response

def sonderausstattung3(i):
    trimlinesportline = ["Sport-Line", "sport line", "Sport Line", "sportline", "SPORT LINE", "Sportline"]
    response = "normal"
    if "Trim line" in i["attributes"]:
        trimline = i["attributes"]["Trim line"]
        for a in trimlinesportline:
            if a in trimline:
                response = "sportline"

    return response



def sonderausstattunggesamt(i):
    if sonderausstattung1(i) == "msport":
        return "msport"
    elif sonderausstattung2(i) == "luxuryline":
        return "luxuryline"
    elif sonderausstattung3(i)== "sportline":
        return "sportline"
    else:
        return "normal"


#printtrimline1(luxuryline1)
#printtrimline1(sportline1)
#for i in msport1:
#    print(sonderausstattung(i))
#    print(sonderausstattung1(i))

#for i in luxuryline1:
#    if "Trim line" in i["attributes"]:
#        print(i["attributes"]["Trim line"])
#    print("luecke")

#   print(sonderausstattung2(i))

for i in luxuryline1:
    print(sonderausstattunggesamt(i))

for i in sportline1:
    print(sonderausstattunggesamt(i))

for i in msport1:
    print(sonderausstattunggesamt(i))