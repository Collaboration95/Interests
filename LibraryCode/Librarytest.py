from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select as DropDown

ExecutablePath = "/Users/speedpowermac/Documents/projects/CODE_MAIN/chromedriver" 

# id = "edit-location"
TargetWebsiteUrl = "https://mylibrary.sutd.edu.sg/"

driver1= webdriver.Chrome(executable_path=ExecutablePath)

driver1.get(TargetWebsiteUrl+"availability/"+"262/"+"2022-01-24")

elems = driver1.find_elements(By.XPATH,"//a[@href]")
elems = [x.get_attribute("href") for x in elems]
temp = elems.copy()

temp = [ int(x[55:]) for x in temp if(x[0:50]=="https://mylibrary.sutd.edu.sg/reservation/add/user")]

for x in temp:
    temp_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(x))
    print(temp_time)