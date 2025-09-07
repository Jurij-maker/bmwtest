from categoryfunctions import modellzuordnung, sonderausstattunggesamt, fuel, transmission, twoor4wheel, categorizekm, hasACC, haspano, dealer

import json

import numpy as np
from matplotlib import pyplot as plt
bmw300251= open('m3.json',)
bmw30025 = json.load(bmw300251)
data1 = bmw30025

bmw3er=open("bmw30025.json")
bmw3er1=json.load(bmw3er)
data=bmw3er1

auto = bmw30025[35]

print("Modellzuordnung")
print(modellzuordnung(auto))
print("Sonderausstattung")
print(sonderausstattunggesamt(auto))
print("Fuel")
print(fuel(auto))
print("Transmission")
print(transmission(auto))
print("2 oder 4 Räder")
print(twoor4wheel(auto))
print("Kilometer")
print(categorizekm(auto))
print("Driveassist")
print(hasACC(auto))
print("Panoramadach")
print(haspano(auto))
print("Verkaufprivathändler")
print(dealer(auto))