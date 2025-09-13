import json

import numpy as np
from matplotlib import pyplot as plt
bmw300251= open('m3comp.json',)
bmw30025 = json.load(bmw300251)
data1 = bmw30025

bmw3er=open("bmw30025.json")
bmw3er1=json.load(bmw3er)
data=bmw3er1


def isdamaged(i):
    if "Vehicle condition" in i["attributes"]:
        condition = i["attributes"]["Vehicle condition"]
        if "damage" in condition:
            return True
        else:
            return False
    else:
        return False



def is318i(i):
    if "Fuel" in i["attributes"] and "model" in i:
        if i["attributes"]["Fuel"] == "Petrol" or i["attributes"]["Fuel"] == "Petrol, E10-enabled":
            if i["model"]=="318":
                return True
    else:
        return False

def is318d(i):
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

def is320d(i):
    if "Fuel" in i["attributes"] and "model" in i:
        if i["attributes"]["Fuel"] == "Diesel":
            if i["model"]=="320":
                return True
    else:
        return False

def is320e(i):
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

def is320d(i):
    if "Fuel" in i["attributes"] and "model" in i:
        if i["attributes"]["Fuel"] == "Diesel":
            if i["model"]=="320":
                return True
    else:
        return False

def is320e(i):
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

def is330d(i):
    if "Fuel" in i["attributes"] and "model" in i:
        if i["attributes"]["Fuel"] == "Diesel":
            if i["model"]=="330":
                return True
    else:
        return False

def is330e(i):
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

def sonderausstattung4(i):
    if isM340i(i) or isM340d(i) or isM3(i) or isM3Competition(i):
        return "M"
    else:
        return"normal"

def sonderausstattunggesamt(i):
    if sonderausstattung1(i) == "msport":
        return "msport"
    elif sonderausstattung2(i) == "luxuryline":
        return "luxuryline"
    elif sonderausstattung3(i)== "sportline":
        return "sportline"
    elif sonderausstattung4(i)=="M":
        return"M"
    else:
        return "normal"

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


def transmission(auto):
    if "Transmission" in auto["attributes"]:
        trans = auto["attributes"]["Transmission"]
        if "Automatic" in trans:
            return "automatic"
        elif "Manual gearbox" in trans:
            return "manual"

        else:
            return ""
    else:
        return ""


def twoor4wheel(i):
    response = "2wheeldrive"
    if "features" in i:
        a=i["features"]
        for x in a:
            if "Four" in x:
                response ="4wheeldrive"
    return response


def mileagetoint(auto):
    kmstring="0"

    if "Mileage" in auto["attributes"]:
        mileage = auto["attributes"]["Mileage"]
        for i in mileage:
            if i.isdigit():
                kmstring = kmstring + i

    return int(kmstring)



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

def hasACC(i):
    response ="noACC"
    if "features" in i:
        a=i["features"]
        for x in a:
            if "Adaptive" in x:
                response = "ACC"
    return response



def haspano(i):
    response = "nopano"
    if "features" in i:
        a=i["features"]
        for x in a:
            if "Pano" in x:
                response = "pano"
    return response

def getprice(i):
    price = 0
    if "price" in i:
        price = i['price']['total']['amount']
    elif "price.total.amount" in i:
        price = i["price.total.amount"]

    return price



def dealer(auto):
    if "sellerType" in auto["dealerDetails"]:
        type = auto["dealerDetails"]["sellerType"]
        if "Private" in type:
            return "private"
        elif "Dealer" in type:
            return "dealer"

        else:
            return ""
    else:
        return ""