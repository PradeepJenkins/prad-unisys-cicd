#we're only importing webdriver from entire selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
#Initilizing web driver
chrome_driver = webdriver.Chrome()
#Opening a web url
chrome_driver.get("https://rahulshettyacademy.com/angularpractice/")

#Selenium can find elements by no of things
# name, class, id, css selector, xpath
chrome_driver.find_element(By.NAME, "name").send_keys("ashuuser")
chrome_driver.find_element(By.NAME, "email").send_keys("ashutoshh@linux.com")
chrome_driver.find_element(By.ID, "exampleInputPassword1").send_keys("HelloCloudT@12345")
chrome_driver.find_element(By.ID, "exampleCheck1").click()
my_select = Select(chrome_driver.find_element(By.ID, "exampleFormControlSelect1"))
my_select.select_by_index(1)
#my_select.select_by_visible_text("Female")
#using CSS selector for radio button
chrome_driver.find_element(By.CSS_SELECTOR, "#inlineRadio2").click()
time.sleep(3)
#submit_button = chrome_driver.find_element(By.XPATH, "//input[@class='btn-success' and @type='submit' and @value='Submit']")
#submit_button = chrome_driver.find_element(By.CLASS_NAME, "btn-success")
#submit_button = chrome_driver.find_element(By.CSS_SELECTOR, "btn-success[type='submit'][value='Submit']")
chrome_driver.find_element(By.XPATH, "//input[@type='submit']").click()
#submit_button.click();

time.sleep(3)
#find the success data
message = success_msg = chrome_driver.find_element(By.CLASS_NAME, "alert-success").text
time.sleep(5)

#printing message
print(message)
#message validation using assertion in python
assert "The Form has been submitted successfully!." in message

#printing title
print("Page Title: " ,chrome_driver.title)
#printing current URL
print("Current URL: " ,chrome_driver.current_url)
#saving screenshot
chrome_driver.save_screenshot("pagehome1.png")
print("current page screenshot saved")
#closing my driver/stopping
chrome_driver.quit()