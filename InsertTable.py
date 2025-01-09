import csv
import sqlite3

#Input: csv files
conn = sqlite3.connect("LLM_Education.db")
cursor = conn.cursor()

with open("Papers.csv", 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    columns = next(reader)
    query = f'INSERT INTO Papers ({", ".join(columns)}) VALUES ({", ".join(["?"]*len(columns))})'

    for data in reader:
        cursor.execute(query, data)

with open("LLMInfo.csv", 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    columns = next(reader)
    query = f'INSERT INTO LLMInfo ({", ".join(columns)}) VALUES ({", ".join(["?"]*len(columns))})'

    for data in reader:
        cursor.execute(query, data)

with open("ObjectResult.csv", 'r', encoding='utf-8', errors="ignore") as file:
    reader = csv.reader(file)
    columns = next(reader)
    query = f'INSERT INTO ObjectResult ({", ".join(columns)}) VALUES ({", ".join(["?"]*len(columns))})'

    for data in reader:
        cursor.execute(query, data)

with open("Methods.csv", 'r', encoding='utf-8', errors="ignore") as file:
    reader = csv.reader(file)
    columns = next(reader)
    query = f'INSERT INTO Methods ({", ".join(columns)}) VALUES ({", ".join(["?"]*len(columns))})'

    for data in reader:
        cursor.execute(query, data)

with open("Assignments.csv", 'r', encoding='utf-8', errors="ignore") as file:
    reader = csv.reader(file)
    columns = next(reader)
    query = f'INSERT INTO Assignments ({", ".join(columns)}) VALUES ({", ".join(["?"]*len(columns))})'

    for data in reader:
        cursor.execute(query, data)

with open("Classes.csv", 'r', encoding='utf-8', errors="ignore") as file:
    reader = csv.reader(file)
    columns = next(reader)
    query = f'INSERT INTO Classes ({", ".join(columns)}) VALUES ({", ".join(["?"]*len(columns))})'

    for data in reader:
        cursor.execute(query, data)

with open("Exams.csv", 'r', encoding='utf-8', errors="ignore") as file:
    reader = csv.reader(file)
    columns = next(reader)
    query = f'INSERT INTO Exams ({", ".join(columns)}) VALUES ({", ".join(["?"]*len(columns))})'

    for data in reader:
        cursor.execute(query, data)

with open("Surveys.csv", 'r', encoding='utf-8', errors="ignore") as file:
    reader = csv.reader(file)
    columns = next(reader)
    query = f'INSERT INTO Surveys ({", ".join(columns)}) VALUES ({", ".join(["?"]*len(columns))})'

    for data in reader:
        cursor.execute(query, data)

with open("Students.csv", 'r', encoding='utf-8', errors="ignore") as file:
    reader = csv.reader(file)
    columns = next(reader)
    query = f'INSERT INTO Students ({", ".join(columns)}) VALUES ({", ".join(["?"]*len(columns))})'

    for data in reader:
        cursor.execute(query, data)

conn.commit()
conn.close()
print("Inserted into all tables.\n")