import pandas as pd
import json
import numpy as np
from matplotlib import pyplot as plt





def preisevondf(df):
    preisliste=[]
    for row in df.itertuples:
        preisliste.insert(len(preisliste),df(row.price))

    return preisliste

def schaubildprivathaendler(listepreisprivat, listepreishaendler):

    privat = np.array(listepreisprivat)
    haendler = np.array(listepreishaendler)

    plt.title("Vergleich Preise Privat-Haendler")
    plt.xlabel("Preis in Euro")
    plt.ylabel("Anzahl der Fahrzeuge")

    plt.hist(haendler)
    plt.hist(privat)
    plt.legend(["haendler", "privat"], loc="upper right")
    plt.show()