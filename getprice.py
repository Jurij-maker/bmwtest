import json
import numpy as np
from matplotlib import pyplot as plt


luxuryline = open('luxuryline.json')
luxuryline1 = json.load(luxuryline)


def is320d(i):
    if "Fuel" in i["attributes"] and "model" in i:
        if i["attributes"]["Fuel"] == "Diesel":
            if i["model"]=="320":
                return True
    else:
        return False



for x in data:
    print(x['title'])
    print(x['price']['total']['amount'])

def getprice(i):
    if "amount" in i['price']['total']:
        price = i['price']['total']['amount']
        return price
    else:
        return "0"


