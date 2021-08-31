import pyodbc
import pandas as pd

cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=INNOWIN43169;"
                      "Database=DEV_REPORTING;"
                      "Trusted_Connection=yes;")

df = pd.read_sql(sql="select * from Py_Dumy ", con=cnxn)
df.to_excel(r"C:\Users\evsairn\Desktop\Finance\SQL_Export.xlsx", index=False)
