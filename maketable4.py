import pandas as pd
import json

import numpy as np
from matplotlib import pyplot as plt
from maketable32 import listpandasfromjsonsorted


bmw300251= open('m3.json',)
bmw30025 = json.load(bmw300251)
data1 = bmw30025

bmw3er=open("bmw30025.json")
bmw3er1=json.load(bmw3er)
data=bmw3er1

luxuryline = open('luxuryline.json')
luxuryline1 = json.load(luxuryline)

def preisevondf(df):
    preisliste=[]
    for row in df.itertuples():
        preisliste.insert(len(preisliste),df(row.price))

    return preisliste

def test1(df):
    for row in df.itertuples():
        print(row)

def preiseprivathaendler(df, category):
    preislisteprivat = []
    preislistehaendler = []
    df1 = pd.DataFrame(
        columns=['Modell', 'Sonderausstattung', 'Transmission', 'Wheeldrive', 'km', 'ACC', 'Pano', 'Karosserie', 'Dealer', 'Price',
                 'Category'])
    for row in df.itertuples():
        #print(row.Category == category)
        if row.Category == category:
            print(row)
            if row.Dealer == "private":
                print(row)
                preislisteprivat.insert(len(preislisteprivat), row.Price)
            else:
                print(row)
                preislistehaendler.insert(len(preislistehaendler), row.Price)

    #print(df1.tostring())


    return preislistehaendler, preislisteprivat


def schaubildprivathaendler(listepreisprivat, listepreishaendler):

    privat = np.array(listepreisprivat)
    haendler = np.array(listepreishaendler)
    print(len(privat))
    print(len(haendler))

    plt.title("Vergleich Preise Privat-Haendler")
    plt.xlabel("Preis in Euro")
    plt.ylabel("Anzahl der Fahrzeuge")


    #plt.hist(privat, bins =5,alpha = 0.5, label = "privat")
    #plt.hist(haendler, bins = 5,alpha = 0.5, label ="haendler")
    plt.hist([privat, haendler], stacked=True, color=['cyan', 'Purple'], edgecolor='black')

    plt.legend(['privat', 'haendler'], loc='upper right')
    plt.show()

listepandas = listpandasfromjsonsorted(data)
#pandas = listpandasfromjsonsorted(data1)
#pandas.sort_values(by='Category')
liste=listepandas.sort_values(by='Category')
print(liste.to_string())


#test1(listepandas)

haendlerliste, privatliste = preiseprivathaendler(listepandas, 363219)
print(len(haendlerliste))
print(len(privatliste))
schaubildprivathaendler(privatliste, haendlerliste)
