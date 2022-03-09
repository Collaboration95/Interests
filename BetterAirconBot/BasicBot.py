from selenium import webdriver
import re,time , hashlib
# from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By

# Variables required
UserName = "20000486"
PassWord = "Aircon0469"
LoginButton = "btnLogin"
LoginIdName = "txtLoginId"
PasswordName = "txtPassword"
Options  = {1:"Login",2:"DummyFunction",3:"exit"}

ExecutablePath = "/Users/speedpowermac/Documents/projects/CODE_MAIN/chromedriver"

def ShowAndGetOptions(OptionsDict:dict)->int:
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
        Login_Setup()
    elif N==2:
        IamWastingTime()
    elif N==3:
        exit("Thank You for using the bot ")

def IamWastingTime():
    # I am wasting time 
    password = 0

    while True:
        password = input("Please Input password :")
        if password ==95141:
            break
        else:
            continue
        
    with open ("Balance.txt","r") as f:
        TempContent = f.readlines()
    
    TempContent = [x.strip("\n") for x in TempContent ]
    Content = {}
    FinalContent = []
    for i in range(len(TempContent)):
        TempContent1 =  TempContent[i].split(" ")
        Content["UnixTime"] = TempContent1[0]
        Content["NormalTime"] = TempContent1[1] 
        Content["Balance"] = TempContent1[2]
        Content["Hashed"] = TempContent1[3]
        FinalContent.append(Content.copy())


def Login_Setup():
    #this function is used to setup Userinfo and enter it
    if(input("Press Enter if you want to use default")!=""):
        UserName = input("Input UserName :")
        PassWord = input("Input Password :")
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
    
    # Getting XPATH for balance
    element = driver.find_element(By.XPATH,"//*[@id='frmViewMeterCredit']/table/tbody/tr[4]/td[3]/font")
    Balance = element.get_attribute('innerHTML')

    # Getting Last Recorded TimeStamp
    element1 = driver.find_element(By.XPATH,"/html/body/table/tbody/tr[1]/td[2]/form/table/tbody/tr[9]/td[2]/font")
    UnixTime = Epoch_Time(element1.text)

    FloatBalance = float(Balance[18:])
    print("The Remaining Balance is ${}".format(FloatBalance))
    NormalTime = re.sub(' ','|',element1.text)
    
    WriteData(UnixTime,NormalTime,FloatBalance,Sha256Hashing(UserName)) 
    #Calls a function to write info into a text file      
    
    time.sleep(3)
    driver.close()

def WriteData(UnixTime,NormalTime,Balance:float,HashedName):
    # This function writes the current time and 
    with open ("Balance.txt","a") as f:
        f.write("{} {} {} {}".format(UnixTime,NormalTime,Balance,HashedName))
        f.write("\n")

def Sha256Hashing(CurrentUserName:str):
    # This function is here because i just learnt Sha256 function 
    return hashlib.sha256(CurrentUserName.encode()).hexdigest()

def Epoch_Time(Time_String) ->str:
    # Converts the given time in "dd.mm.yyy hh:mm:ss" into epoch time 
    Converted_Time = time.mktime(time.strptime(Time_String, "%d/%m/%Y %H:%M:%S"))
    return str(int(Converted_Time))

def MainFunction()->None:
    # This is the first function that is called when the program is executed
    Routing_function(ShowAndGetOptions(Options))

MainFunction()
