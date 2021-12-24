#Importing all the headerfiles that i need 
from typing import Set
from selenium import webdriver
from selenium.webdriver.common.by import By
import os,time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select as DropDown
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
#Variables for idnames 
DateField_name = "search_date[date]"
RoomField_id = "edit-location"
CategoryField_id = "edit-category"
SubmitButton_id ="edit-submit"

driver= webdriver.Chrome(executable_path="/Users/speedpowermac/Documents/projects/CODE_MAIN/chromedriver")

#Getting the target website name 
driver.get("https://mylibrary.sutd.edu.sg/roombooking")

#Code for modifying the date format yyyy-mm-dd
Set_Date = driver.find_element(By.NAME,DateField_name)
# Set_Date.get_attribute("2021-12-22")
Set_Date.click()
Set_Date.send_keys(Keys.COMMAND,"a")
Set_Date.send_keys(Keys.BACKSPACE)
Set_Date.send_keys("2021-12-24")
Set_Date.send_keys(Keys.RETURN)
# Set_Date.clear()

# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME,DateField_name ))).click()
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME,DateField_name))).send_keys("Example")

# print("Gru")
# Set_Date.send_keys("2021-12-26")
# # Set_Date_1 = driver.find_element(By.NAME,DateField_name)
# # Set_Date_1.send_keys("2021-12-26")
# # Set_Room = driver.find_element(By.ID,RoomField_id)


# # Set_Category = driver.find_element(By.ID,CategoryField_id)

#    # e
# SubmitButton_id = driver.find_element(By.ID,"edit-submit")
# SubmitButton_id.click()

#     print("ButtonClick Failure")









