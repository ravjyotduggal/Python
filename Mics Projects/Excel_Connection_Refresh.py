import win32com.client

xlapp = win32com.client.DispatchEx("Excel.Application")
wb = xlapp.Workbooks.Open(r"C:\Users\evsairn\Desktop\Dumy_Refresh.xlsx")
wb.RefreshAll()
xlapp.CalculateUntilAsyncQueriesDone()
xlapp.DisplayAlerts = False
wb.Save()
xlapp.Quit()
