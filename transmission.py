import json
import numpy as np
from matplotlib import pyplot as plt


luxuryline = open('luxuryline.json')
luxuryline1 = json.load(luxuryline)

m3 = open('m3.json')
m31 = json.load(m3)

def printtransmission(autos):
    for auto in autos:
        if "Transmission" in auto["attributes"]:
            print(auto["attributes"]["Transmission"])


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

printtransmission(luxuryline1)
printtransmission(m31)
#for i in luxuryline1:
#    print(transmission(i))