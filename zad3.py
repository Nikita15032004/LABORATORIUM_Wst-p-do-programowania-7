import pandas as pd

plik = "demografia.csv"

dane = pd.read_csv(plik, decimal=",", na_values=["NA", "n/a", "NaN"])
dane_bezkraju = dane.drop(columns=["KRAJE"])
max_przyrost = dane_bezkraju.max().max()
rok_max_przyrost = dane_bezkraju.max().idxmax()
indeks_max_przyrost = dane_bezkraju[rok_max_przyrost].idxmax()
kraj_zmax_przyrostem = dane.loc[indeks_max_przyrost, "KRAJE"]

print("Największy przyrost ludności występuje w kraju:", kraj_zmax_przyrostem,
      "i wyniósł:", max_przyrost, "w roku:", rok_max_przyrost)
