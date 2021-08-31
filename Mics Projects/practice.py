from selenium import webdriver
import pyodbc

path = r"C:\Users\evsairn\Downloads\chromedriver_win32_1\chromedriver.exe"

conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=INNOWIN43169;"
                      "Database=DEV_REPORTING;"
                      "Trusted_Connection=yes;")

driver = webdriver.Chrome(path)

driver.get(r"https://www.amazon.in/s?k=baby+powder&crid=3HR6R5JBXLOGA&sprefix=baby+powd%2Caps%2C325&ref=nb_sb_ss_ts-a-p_1_9")

#elems = driver.find_elements_by_xpath(r"//*[@id='search']/div[1]/div[2]/div")

elems = driver.find_elements_by_class_name("sg-col-inner")

#driver.find_elements_by_xpath(r"//*[@id='search']/div[1]/div[2]/div/span[3]/div[2]/div[4]")
#For Sponsoerd - driver.find_elements_by_class_name(r"s-label-popover-default")
#For Price - driver.find_elements_by_class_name(r"a-row")
#For Rating - driver.find_elements_by_class_name(r"a-icon-alt")
#For Rating - driver.find_element_by_tag_name("h2").find_element_by_tag_name("span")

cursor = conn.cursor()

#driver.find_elements_by_class_name(r"s-main-slot s-result-list s-search-results sg-row")#
#elems = driver.find_elements_by_xpath(r"//*[@id='search']/div[1]/div[2]/div/span[3]/div[2]")

#elem1 = driver.find_elements_by_xpath(r"//*[@id='search']/div[1]/div[2]/div/span[3]/div[2]/div[2]/div/span/div/div/div/div")

# for item in elem1:
#     print(item.text)
#     rating1 = item.find_element_by_xpath(r"//*[@id='search']/div[1]/div[2]/div/span[3]/div[2]/div[2]/div/span/div/div/div/div/div[3]/div/span[1]/span/a/i[1]/span").get_attribute('innerHTML')
#     #rating = item.find_element_by_xpath(r"//*[@id='search']/div[1]/div[2]/div/span[3]/div[2]/div[2]/div/span/div/div/div/div/div[3]/div/span[1]/span/a").get_attribute('innerHTML')
#     print(rating1)
    #ratings = driver.find_element_by_xpath(r"//*[@id='search']/div[1]/div[2]/div/span[3]/div[2]/div[2]")
    # print(ratings.text)
i = 2
for item in elems:
    try:
        sponsored = item.find_element_by_class_name(r"s-label-popover-default")
        print(sponsored.text)
    except:
        sponsored = ""
    try:
        name = item.find_element_by_tag_name("h2").find_element_by_tag_name("span")
        print(name.text)
    except:
        name = ""
    try:
        price = item.find_element_by_class_name(r"a-price-whole")
        print(price.text)
    except:
        price = ""
    try:
        rating = item.find_element_by_class_name(r"a-icon-alt").get_attribute("innerHTML")
        print(rating)
    except:
        rating = ""
    try:
        asin = driver.find_element_by_xpath(r"//*[@id='search']/div[1]/div[2]/div/span[3]/div[2]/div[{}]".format(i)).get_attribute("data-asin")
        print(asin)
    except:
        asin = ""
    # try:
    #     if sponsored != "" and name != "" and name != "" and name != "" and name != "":
    #         cursor.execute("insert into dummy1 values(?,?,?,?,?)", (sponsored.text, name.text, price.text, rating, asin))
    #         conn.commit()
    #     elif name != "" and name != "" and name != "" and name != "":
    #         cursor.execute("insert into dummy1 values(?,?,?,?,?)", ("", name.text, price.text, rating, asin))
    #         conn.commit()
    #     else:
    #         continue
    # except AttributeError:
    #     continue
    i += 1
    print("*" * 80)

conn.close()
driver.quit()

