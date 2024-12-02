import pandas as pd

demografic_data = pd.read_csv('demografia.csv', decimal=',', na_values=['NA', 'n/a', 'NaN'])
print(demografic_data)