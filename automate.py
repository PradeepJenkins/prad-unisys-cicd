#we're only importing webdriver from entire selenium
from selenium import webdriver
import time
#Initilizing web driver
chrome_driver = webdriver.Chrome()
#Opening a web url
chrome_driver.get("http://portal.adhocnet.org/login")
time.sleep(4)
#closing my driver/stopping
chrome_driver.quit()
