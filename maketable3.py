from categoryfunctions import modellzuordnung, sonderausstattunggesamt, fuel, transmission, twoor4wheel, categorizekm, hasACC, haspano, dealer, isdamaged, getprice
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

#auto = bmw30025[35]

dfgesamt = pd.DataFrame(columns=['Modell','Sonderausstattung','Transmission','Wheeldrive', 'km','ACC','Pano','Dealer','Price'])

for auto in bmw30025:

    if isdamaged(auto) == True:
        continue

    modell = modellzuordnung(auto) #12

    if modell == "":
        continue

    sonderausstattung = sonderausstattunggesamt(auto) #5

    transmission1 = transmission(auto) #2

    if transmission =="":
        continue
    wheels = twoor4wheel(auto)   #2

    kmcateogorie = categorizekm(auto) #4 (5)

    ACC= hasACC(auto)              #2

    pano = haspano(auto)           #2

    dealer1 = dealer(auto)               #(2)

    if dealer =="":
        continue

    price = getprice(auto)
    if price == 0:
        continue



    dfgesamt.loc[len(dfgesamt)]=[modell, sonderausstattung, transmission1, wheels, kmcateogorie, ACC, pano, dealer1, price]

print(dfgesamt.to_string())

#for i in bmw3er1:
#    print(isdamaged(i))

