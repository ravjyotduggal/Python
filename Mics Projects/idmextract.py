from selenium import webdriver as wb
import time
import pandas as pd
from tkinter import *
from tkinter import ttk
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import messagebox
from tkinter import filedialog


def login():
    user = str(mtext1.get().strip())
    psd = str(mtext2.get().strip())
    if not user:
        messagebox.showerror('Error', 'Please Enter Username')
    elif not psd:
        messagebox.showerror('Error', 'Please enter password')
    else:
        browser = wb.Chrome(r'C:\chdriver\chromedriver.exe')
        try:
            browser.get(r'https://idm.internal.ericsson.com/itim/ssui/')
            time.sleep(120)

            #username = browser.find_element_by_id('USER')
            #username.send_keys(user)
            #password = browser.find_element_by_id('PASSWORD')
            #password.send_keys(psd)
            #time.sleep(2)
            #logbutton = browser.find_element_by_name('login')
            #logbutton.click()
            #time.sleep(30)
            try:
                myreport = browser.find_element_by_xpath(
                    '/html/body/div[1]/div[1]/div[2]/div[1]/div/table/tbody/tr/td[1]/div/div[2]/div[2]/ul/li[4]/a[2]/em/span/span')
                myreport.click()
                time.sleep(5)
                icon = browser.find_element_by_xpath(
                    '/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[2]/div[1]/div/div/div[2]/div/div/img[2]')
                icon.click()
                nodetext = browser.find_elements_by_class_name('x-tree3-node-text')
                dict = {}
                lis2 = []
                for i in range(2, len(browser.find_elements_by_class_name('x-tree3-el'))):
                    lis = []
                    element =browser.find_elements_by_class_name('x-tree3-el')[i]
                    element.click()
                    node = element.text
                    # node = nodetext[i].get_attribute('innerHTML')
                    time.sleep(5)
                    if node == 'SecureStorage HRMS HC Reporting Low':
                        time.sleep(150)
                    try:
                        grid = WebDriverWait(browser, 30).until(
                            EC.presence_of_element_located((By.CLASS_NAME, "x-grid3-body")))
                        grid = browser.find_element_by_class_name('x-grid3-body')
                        gridtext = grid.text
                        gridtextn = gridtext.replace('\n', ',')
                        lis = gridtextn.split(",")
                        dict['Role'] = node
                        for elem in range(0, len(lis) - 1, 2):
                            dict['Signum'] = lis[elem]
                            dict['Full Name'] = lis[elem + 1]
                            lis2.append(dict.copy())
                    except:
                        dict['Role'] = node
                        dict['Signum'] = 'No Member'
                        dict['Full Name'] = 'No Member'
                        lis2.append(dict.copy())
                        continue
                df = pd.DataFrame(lis2)
                df = df.fillna('')
                df.to_csv(r'C:\IDM_Extract_Data\Idmextract.csv')
                dict.clear()
                time.sleep(5)
                browser.close()
                mtext1.delete(0, 'end')
                mtext2.delete(0, 'end')
            except Exception as exc:
                browser.close()
                print(exc)
        except Exception as e:
            browser.close()
            print(e)


if __name__ == '__main__':
    root = Tk()
    root.configure(background='white')
    root.title("IDM Role Extraction")
    icon = PhotoImage(file=r'C:\chdriver\icon.png')
    root.iconphoto(False, icon)
    root.geometry("360x200")
    mlable = Label(root, bg="white", text="signum:", fg='Black', font=("Helvetica", 10))
    mlable.place(x=20, y=30)
    mtext1=Entry(root, bg="white", width=30)
    mtext1.place(x=90, y=30)
    mlable2 = Label(root, bg="white", text="Password:", fg='Black', font=("Helvetica", 10))
    mlable2.place(x=20, y=80)
    mtext2 = Entry(root, bg="white", width=30, show="*")
    mtext2.place(x=90, y=80)
    bbutton = Button(root, text="Run", width='7', height='1', command=login)
    bbutton.place(x=130, y=120)

    blablel = Label(fg="Red", bg="white",
                    text="please contact Rohit Gandhi if issue/support required for the tool.")
    blablel.place(x=5, y=150)
    root.mainloop()