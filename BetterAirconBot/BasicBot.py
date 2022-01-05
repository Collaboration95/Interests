from selenium import webdriver
# from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 
# Variables required
UserName = "20000486"
PassWord = "Aircon0469"
LoginButton = "btnLogin"
LoginIdName = "txtLoginId"
PasswordName = "txtPassword"
Options  = {1:"Login",2:"exit"}

ExecutablePath = "/Users/speedpowermac/Documents/projects/CODE_MAIN/chromedriver"


def ShowAndGetOptions(OptionsDict:dict):
    for key in OptionsDict:
        print("{}. {}".format(key,OptionsDict[key]))
    
    Option = int(input("Please enter your option"))
    if Option in OptionsDict.keys():
        return Option
    else:
        ShowAndGetOptions(Options)

def Routing_function(N:int)->None:
    # This function is to route the functions and the correct options 
    if N==1:
        pass
        Login_Setup()
    elif N==2:
        exit("Thank You for using the bot ")

def Login_Setup():


    if(input("Press Enter if you want to use defualt")!=""):
        UserName = input("Input UserName")
        PassWord = input("Input Password")
    else:
        UserName = "20000486"
        PassWord = "Aircon0469"
    driver= webdriver.Chrome(executable_path=ExecutablePath)
    driver.get("https://nus-utown.evs.com.sg/SUTD/")
    driver.switch_to.frame("leftFrame")

    # Filling in the User Id
    Fill_Name = driver.find_element(By.NAME,LoginIdName)
    Fill_Name.click()
    Fill_Name.send_keys(UserName)

    # Filling in the Password
    Fill_Password = driver.find_element(By.NAME,PasswordName)
    Fill_Password.click()
    Fill_Password.send_keys(PassWord)
    
    # Clicking the login button 
    Button = driver.find_element(By.NAME,LoginButton)
    Button.click()
    
    driver.execute_script("window.open('about:blank','secondtab');")
    driver.switch_to.window("secondtab")
    driver.get("https://nus-utown.evs.com.sg/SUTDMain/viewMeterCreditServlet")
    element = driver.find_element(By.XPATH,"//*[@id='frmViewMeterCredit']/table/tbody/tr[4]/td[3]/font")
    Balance = element.get_attribute('innerHTML')
    IntBalance = float(Balance[18:])
    print("The Remaining Balance is {}".format(IntBalance))
    time.sleep(3)
    driver.close()


# def SecondPage(driver1):
#     # This is the code that runs in the second page/thepage after the login page
#     driver1.find_element(By.LINK_TEXT,"Web Calculator")
#     driver1.switch_to.frame("leftFrame")
#     driver1.click()    
    
#     pass

def MainFunction():
    # This is the first function that is called when the program is executed
    
    
    Routing_function(ShowAndGetOptions(Options))

    pass

MainFunction()