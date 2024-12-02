import pandas as pd

pilk = 'demografia.csv'
dane = pd.read_csv(
    pilk,
    decimal=',',
    na_values=['NA', 'n/a', 'NaN']
)
indeks_max = dane['2022'].idxmax(skipna=True)
kraj = dane.loc[indeks_max, 'KRAJE']

print(f"Najwiekszy przyrost ludnosci w 2022 roku odnotowano w kraju: {kraj}")