import json
import numpy as np
from matplotlib import pyplot as plt

bmw300251= open('m3.json',)

bmw30025 = json.load(bmw300251)
data = bmw30025

for i in data:
    if "Power" in i["attributes"]:
        if "480" in i["attributes"]["Power"]:
            print(i["attributes"]["Power"])
