from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

path = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(path)

driver.get("http://idm.internal.ericsson.com/")

user_name = driver.find_element_by_id("USER")
user_name.send_keys("EVSAIRN")
pwd = driver.find_element_by_id("PASSWORD")
pwd.send_keys("")

login_button = driver.find_element_by_name("login")
login_button.click()


