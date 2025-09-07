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

#printtransmission(luxuryline1)
#printtransmission(m31)
#for i in luxuryline1:
#    print(transmission(i))

for i in luxuryline1:
    print(dealer(i))