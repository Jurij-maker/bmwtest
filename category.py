import json
import numpy as np
from matplotlib import pyplot as plt


luxuryline = open('luxuryline.json')
luxuryline1 = json.load(luxuryline)

m3 = open('m3.json')
m31 = json.load(m3)

def printcategory(autos):
    for auto in autos:
        if "Category" in auto["attributes"]:
            print(auto["attributes"]["Category"])


def category(auto):
    if "Category" in auto["attributes"]:
        category = auto["attributes"]["Category"]
        if "Saloon" in category or "Limousine" in category:
            return "limousine"
        elif "Estate car" in category:
            return "estatecar"

        else:
            return ""
    else:
        return ""

#printcategory(luxuryline1)
#printcategory(m31)
for i in m31:
    print(category(i))