import pandas as pd

data = {
    "Nr_albumu": [1, 2, 3, 4, 5],
    "Imię": ["Anna", "Jan", "Katarzyna", "Tomasz", "Michał"],
    "Nazwisko": ["Kowalska", "Nowak", "Wiśniewska", "Kaczmarek", "Zieliński"],
    "Ocena": [4.5, 3.0, 5.0, 4.0, 2.5],
    "Wiek": [22, 21, 24, 23, 25]
}

df = pd.DataFrame(data)

#a)
students_above_4 = df[df["Ocena"] > 4]
print("students_above_4")
print(students_above_4)

#b)
sorted_by_age = df.sort_values(by="Wiek")
print("sorted_by_age:")
print(sorted_by_age)

#c)
grouped_by_grade = df.groupby("Ocena")["Wiek"].mean()
print("grouped_by_grade:")
print(grouped_by_grade)

#d)
improvement_data = {
    "Nr_albumu": [1, 2, 3, 4, 5],
    "Ocena_poprawa": [4.5, 3.5, 5.0, 4.5, 3.0]
}
improvement_df = pd.DataFrame(improvement_data)
merged_df = pd.merge(df, improvement_df, on="Nr_albumu")
print("Changed grades:")
print(merged_df)

#e)
file_path = "students.csv"
merged_df.to_csv(file_path, index=False)

#f)
loaded_df = pd.read_csv(file_path)
print("Data from students.csv")
print(loaded_df)

#g)
new_student = {
    "Nr_albumu": 6,
    "Imię": "Ewa",
    "Nazwisko": "Kowalczyk",
    "Ocena": 4.0,
    "Wiek": 20,
    "Ocena_poprawa": 4.5
}
loaded_df = pd.concat([loaded_df, pd.DataFrame([new_student])], ignore_index=True)
print("Data from students.csv with new student")
print(loaded_df)

#h)
unique_grades = loaded_df["Ocena"].unique()
print("unique_grades:")
print(unique_grades)

#i)
students_with_grade_5 = len(loaded_df[loaded_df["Ocena"] == 5.0])
print("students_with_grade_5:")
print(students_with_grade_5)


