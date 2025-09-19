from categoryfunctions import modellzuordnung, sonderausstattunggesamt, fuel, transmission, twoor4wheel, categorizekm, hasACC, haspano, dealer, isdamaged, getprice, getkarosserie
from categorytonumber import categorynumber
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

dfgesamt = pd.DataFrame(columns=['Modell','Sonderausstattung','Transmission','Wheeldrive', 'km','ACC','Pano','Karosserie','Dealer','Price','Category'])

for auto in bmw30025:
    catnumber=0

    if isdamaged(auto) == True:
        continue

    modell = modellzuordnung(auto) #12

    if modell == "":
        continue

    catnumber = catnumber + categorynumber[modell]


    sonderausstattung = sonderausstattunggesamt(auto) #5
    catnumber = catnumber + categorynumber[sonderausstattung]

    transmission1 = transmission(auto) #2

    if transmission1 =="":
        continue

    catnumber = catnumber + categorynumber[transmission1]


    wheels = twoor4wheel(auto)   #2
    catnumber = catnumber + categorynumber[wheels]

    kmcategorie = categorizekm(auto) #4 (5)
    catnumber = catnumber + categorynumber[kmcategorie]

    ACC= hasACC(auto)              #2
    catnumber = catnumber + categorynumber[ACC]


    pano = haspano(auto)           #2
    catnumber = catnumber + categorynumber[pano]

    karosserie = getkarosserie(auto)
    if karosserie=="":
        continue
    catnumber = catnumber + categorynumber[karosserie]



    dealer1 = dealer(auto)               #(2)

    if dealer =="":
        continue

    price = getprice(auto)
    if price == 0:
        continue



    dfgesamt.loc[len(dfgesamt)]=[modell, sonderausstattung, transmission1, wheels, kmcategorie, ACC, pano, karosserie, dealer1, price, catnumber]

#print(dfgesamt.to_string())


sorted_dfgesamt = dfgesamt.sort_values(by='Category')

print(sorted_dfgesamt.to_string())
