import json
import numpy as np
from matplotlib import pyplot as plt


luxuryline = open('luxuryline.json')
luxuryline1 = json.load(luxuryline)


#"attributes": {
#    "Vehicle condition": "Used vehicle, Accident-free",



def isdamaged(i):
    if "Vehicle condition" in i["attributes"]:
        condition = i["attributes"]["Vehicle condition"]
        if "damage" in condition:
            return True
        else:
            return False
    else:
        return False


#for auto in luxuryline1:
#    if "Vehicle condition" in auto["attributes"]:
 #       print (auto["attributes"]["Vehicle condition"])
  #  else: print("fehlt")