from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

# Variables

ExecutablePath = "/Users/speedpowermac/Documents/projects/CODE_MAIN/chromedriver"
CookieButtonId = "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"
MainInputFieldID = "inputfield"

def Main()->None:
    AutoWriterCode()

def AutoWriterCode():
    driver = webdriver.Chrome(executable_path=ExecutablePath)
    driver.get("https://10fastfingers.com/typing-test/english")
    time.sleep(4)
    # Allowing Cookie Collection
    CookieButton  = driver.find_element(By.ID,CookieButtonId)
    CookieButton.click()


    html = driver.page_source
    with open ("k.txt","w") as f:
        f.write(html)

    InputField = driver.find_element(By.ID,MainInputFieldID)
    for i in range(282):
        A = driver.find_element(By.CLASS_NAME,"highlight")
        A = A.text.split()
        for i in range(len(A)):
            time.sleep(.1)
            InputField.send_keys(A[i])
        InputField.send_keys(Keys.SPACE)
        





Main()