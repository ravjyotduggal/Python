import zipfile
import os
import pandas as pd

ls = []
dic = {}
try:
    for folder in os.listdir(r'\\eapac.ericsson.se\EINGRDFS01\COE_ANALYTICS\HRGO_COE_ANALYTICS\01 Projects\2019\008 Employee Central Project\SF Queries Export'):
        print(folder)
        try:
            for files in os.listdir(r'\\eapac.ericsson.se\EINGRDFS01\COE_ANALYTICS\HRGO_COE_ANALYTICS\01 Projects\2019\008 Employee Central Project\SF Queries Export\{}'.format(folder)):
                print(files)
                with zipfile.ZipFile(r'\\eapac.ericsson.se\EINGRDFS01\COE_ANALYTICS\HRGO_COE_ANALYTICS\01 Projects\2019\008 Employee Central Project\SF Queries Export\{}\{}'.format(folder, files),'r') as f:
                    for names in f.namelist():
                        dic['Folder Name'] = folder
                        dic['Dump Name'] = files
                        dic['Query Name'] = names
                        ls.append(dic.copy())
        except: continue
except(NotADirectoryError):
    pass



df = pd.DataFrame(ls)
df.to_csv(r'C:\Users\evsairn\Desktop\EC_Queries_Reporsitory.csv')
ls.clear()
