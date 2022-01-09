from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

# Variables
ExecutablePath = "/Users/speedpowermac/Documents/projects/CODE_MAIN/chromedriver"
CookieButtonId = "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"
MainInputFieldID = "inputfield"
TargetWebpage = "https://10fastfingers.com/typing-test/english"
ClassNameForWords = "highlight"

def Main()->None:
    AutoWriterCode()

def AutoWriterCode():
    # This is the function performs the essential 
    driver = webdriver.Chrome(executable_path=ExecutablePath)
    driver.get(TargetWebpage)
    time.sleep(4)
    # Allowing Cookie Collection
    CookieButton  = driver.find_element(By.ID,CookieButtonId)
    CookieButton.click()

    InputField = driver.find_element(By.ID,MainInputFieldID)
    # for i in range(282):
    time.sleep(2)

    while True:
        try:
            A = driver.find_element(By.CLASS_NAME,ClassNameForWords)
            InputField.send_keys(A.text+Keys.SPACE)
        except:
            timer =  ((driver.find_element(By.ID,"timer")).text)[2:]
            print("Going to sleep for {} seconds".format(timer))
            time.sleep(int(timer))

            wpm = driver.find_element(By.ID,"wpm")
            print(wpm.text)
            accuracy = driver.find_element(By.ID,"accuracy")
            print(accuracy.text)
            driver.close()
            break
            pass
        # K = [x for x in A.text]
        # A = A.text.split("")
        # for j in K:
        #     InputField.send_keys(j)
        
    

        # InputField.send_keys(Keys.SPACE)
        





Main()