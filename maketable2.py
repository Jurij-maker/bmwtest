from categoryfunctions import modellzuordnung, sonderausstattunggesamt, fuel, transmission, twoor4wheel, categorizekm, hasACC, haspano, dealer, isdamaged
import pandas as pd
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


damaged=isdamaged(auto)

modell = modellzuordnung(auto) #12

sonderausstattung = sonderausstattunggesamt(auto) #5

transmission = transmission(auto)  #2

wheels = twoor4wheel(auto)   #2

kmcateogorie = categorizekm(auto) #4 (5)

ACC= hasACC(auto)              #2

pano = haspano(auto)           #2

dealer = dealer(auto)               #(2)

dfgesamt = pd.DataFrame(columns=['Modell','Sonderausstattung','Transmission','Wheeldrive', 'km','ACC','Pano','Dealer'])

dfgesamt.loc[len(dfgesamt)]=[modell, sonderausstattung, transmission, wheels, kmcateogorie, ACC, pano, dealer]

print(dfgesamt)

