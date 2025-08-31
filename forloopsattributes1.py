import json
import numpy as np
from matplotlib import pyplot as plt

bmwm3= open('m3.json',)

data = json.load(bmwm3)


def category(car):
    if "category" in car:
        print(car["category"])


for i in data:
    category(i)




