import pyodbc
import pandas as pd

data = pd.read_excel(r"C:\Users\evsairn\Desktop\Py_Demo.xlsx")
conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=INNOWIN43169;"
                      "Database=DEV_REPORTING;"
                      "Trusted_Connection=yes;")
col = []
for columns in data.columns:
    col.append(columns)

print(col)

df = pd.DataFrame(data, columns=col)

cursor = conn.cursor()
for row in df.itertuples():
    cursor.execute("insert into Py_Dumy values(?,?,?,?)", (row.Sno,row.Name, row.Company,row.Position))

conn.commit()
conn.close()
