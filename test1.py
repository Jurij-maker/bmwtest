from modellzuordnung import modellzuordnung

import json
import numpy as np
from matplotlib import pyplot as plt
bmw300251= open('m3comp.json',)
bmw30025 = json.load(bmw300251)
data1 = bmw30025


for i in data1:
    print(modellzuordnung(i))