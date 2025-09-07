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



#for x in data:
#    print(x['title'])
 #   print(x['price']['total']['amount'])

def getprice(i):
    price = 0
    if "price" in i:
        price = i['price']['total']['amount']
    elif "price.total.amount" in i:
        price = i["price.total.amount"]

    return price






for i in luxuryline1:
    print(getprice(i))


