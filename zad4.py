import pandas as pd

dane = {
    "Numer identyfikacyjny pracownika": [1, 2, 3, 4, 5],
    "Imię": ["Anna", "Jan", "Katarzyna", "Tomasz", "Michał"],
    "Nazwisko": ["Kowalska", "Nowak", "Wiśniewska", "Kaczmarek", "Zieliński"],
    "Stanowisko": ["Manager", "Programista", "Konsultant", "Programista", "Manager"],
    "Wiek": [35, 28, 40, 30, 45],
    "Pensja": [8000, 4500, 6000, 5500, 7000]
}

df = pd.DataFrame(dane)
#a)
pracownicy_pensja_plus_5000 = df[df["Pensja"] > 5000]
print(pracownicy_pensja_plus_5000)

#b)
df_sorted_by_age = df.sort_values(by="Wiek")
print("Workers sorted by age:")
print(df_sorted_by_age)

#c)
avg_salary_by_position = df.groupby("Stanowisko")["Pensja"].mean()
print("average salary by position:")
print(avg_salary_by_position)

#d)
updated_positions = pd.DataFrame({
    "Numer identyfikacyjny pracownika": [2, 3],
    "Nowe stanowisko": ["Senior Programista", "Manager"]
})
merged_df = df.merge(updated_positions, on="Numer identyfikacyjny pracownika", how="left")
print("Table with new positions:")
print(merged_df)

#e)
merged_df.to_csv("pracownicy.csv", index=False)
print("Data saved in pracownicy.csv")


#f)
loaded_df = pd.read_csv("pracownicy.csv")
print("Data from pracownicy.csv:")
print(loaded_df)