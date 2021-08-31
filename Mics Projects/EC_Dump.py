import pandas as pd
import os

dic = {}
lst = []

for files in os.listdir(r"C:\Users\evsairn\Desktop\New folder (2)"):
    if files == "Dump.csv":
        pass
    else:
        try:
            df = pd.read_csv(r"C:\Users\evsairn\Desktop\New folder (2)\{}".format(files))
            for col in df.head():
                dic["file_name"] = files
                dic["column_name"] = col
                lst.append(dic.copy())
            df2 = pd.DataFrame(lst)
            df2.to_csv(r"C:\Users\evsairn\Desktop\New folder (2)\Dump.csv")
        except:
            try:
                df = pd.read_excel(r"C:\Users\evsairn\Desktop\New folder (2)\{}".format(files))
                for col in df.head():
                    dic["file_name"] = files
                    dic["column_name"] = col
                    lst.append(dic.copy())
                df2 = pd.DataFrame(lst)
                df2.to_csv(r"C:\Users\evsairn\Desktop\New folder (2)\Dump.csv")
            except:
                df = pd.read_excel(r"C:\Users\evsairn\Desktop\New folder (2)\{}".format(files), engine='pyxlsb')
                for col in df.head():
                    dic["file_name"] = files
                    dic["column_name"] = col
                    lst.append(dic.copy())
                df2 = pd.DataFrame(lst)
                df2.to_csv(r"C:\Users\evsairn\Desktop\New folder (2)\Dump.csv")




