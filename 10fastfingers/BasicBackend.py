from os import initgroups
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
    # This function gets called 
    AutoWriterCode()

def FindWaitTimeWord(DesiredSpeed:int)->float:
    # This function's goal is to find the wait time after each word so that  the program will be able to regulate speed
    m = 552
    delay = 1
    d  = DesiredSpeed 
    timewait = (((1-d/m)/d)*60) -6.6/100
    return float(timewait)


def AutoWriterCode():
    # This is the function performs the essential prominant part of the code 
    driver = webdriver.Chrome(executable_path=ExecutablePath)
    driver.get(TargetWebpage)
    time.sleep(2)
    # Allowing Cookie Collection
    CookieButton  = driver.find_element(By.ID,CookieButtonId)
    CookieButton.click()

    InputField = driver.find_element(By.ID,MainInputFieldID)
    # for i in range(282):
    time.sleep(10)

    timewaitword = FindWaitTimeWord(int(input("Please Enter your desired wpm")))

    StartOffTime = time.time()
    while ((time.time()-StartOffTime)<61):
        A = driver.find_element(By.CLASS_NAME,ClassNameForWords)
        TempWord = (A.text)
        InputField.send_keys(TempWord)
        InputField.send_keys(Keys.SPACE)
        time.sleep(timewaitword)
    time.sleep(10)

while True:

    Main()