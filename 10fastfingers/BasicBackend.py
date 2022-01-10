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

def Choose_Options():
    # Returns user choice 
    return input("Enter 1 to Start the program , 0 to exit")


def Main()->None:
    # This function gets called 
    if (Choose_Options()):
        AutoWriterCode()
    else:
        print("Have a non-consequential day !")


def FindWaitTimeWord(DesiredSpeed:int)->float:
    # This function's goal is to find the wait time after each word so that  the program will be able to regulate speed
    m = 552 #The max speed that the code can generate without any time delay is 552wpm 
    d  = DesiredSpeed
    timewait = (((1-d/m)/d)*60) -6.6/100 #Calculating time wait per word
    return float(timewait)


def AutoWriterCode():
    # This is the function performs the essential prominant part of the code 
    driver = webdriver.Chrome(executable_path=ExecutablePath)
    driver.get(TargetWebpage)
    time.sleep(2) #Waiting for the cookie thing to load
    # Allowing Cookie Collection
    try: 
        CookieButton  = driver.find_element(By.ID,CookieButtonId)
        CookieButton.click()
    except:
        print("Cookie thing did not load / some genius put the window in fullscreen that somehow messes with the cookie button id")
        print("\n Oh Well !")
    InputField = driver.find_element(By.ID,MainInputFieldID)
    
    time.sleep(10) #Waiting for the add stuff to load in , this wastes time since my hotfix methods ask for the word each time 

    timewaitword = FindWaitTimeWord(int(input("Please Enter your desired wpm")))

    StartOffTime = time.time()
    while ((time.time()-StartOffTime)<61): #Checks if 60 seconds has passed before cutting out the code
        A = driver.find_element(By.CLASS_NAME,ClassNameForWords)
        TempWord = (A.text)
        InputField.send_keys(TempWord)
        InputField.send_keys(Keys.SPACE)
        time.sleep(timewaitword)
    time.sleep(10)


Main()