
import json
import numpy as np
from matplotlib import pyplot as plt


luxuryline = open('luxuryline.json')
luxuryline1 = json.load(luxuryline)

m3 = open('m3.json')
m31 = json.load(m3)




def haspano(i):
    response = "nopano"
    if "features" in i:
        a=i["features"]
        for x in a:
            if "Pano" in x:
                response = "pano"
    return response
#print(m31[0]["features"])

#for i in m31[0]["features"]:
#   print(i)
#haspano(luxuryline1[1])
#print(luxuryline[1]['features'])
for i in luxuryline1:
    print(haspano(i))

