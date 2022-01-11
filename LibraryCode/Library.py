#Importing all the headerfiles that i need 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select as DropDown
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Variables
Dict_Info = []
DefaultName = "Guruprasath Gopal"
DefaultPhone =  "87416283"
DefaultEmail = "guruprasath_gopal@mymail.sutd.edu.sg"
DefaultTime = "1800"
TargetWebsiteUrl = "https://mylibrary.sutd.edu.sg/roombooking"
FinalTargetString = "https://mylibrary.sutd.edu.sg/reservation/add/user/"

#Executable path for the chromedriver 
ExecutablePath = "/Users/speedpowermac/Documents/projects/CODE_MAIN/chromedriver" 

def LoadDefault()->None:
    # Loads the default user info into a dict
    Temp_Dict = {}
    Temp_Dict["Name"] = DefaultName
    Temp_Dict["PhoneNumber"]  = DefaultPhone
    Temp_Dict["Email"] = DefaultEmail
    Temp_Dict["Time"]  = DefaultTime
    Dict_Info.append(Temp_Dict.copy())
    return None

def MainFunction():
    SeatNo = Find_Seat_Number()
    TimeNo = Find_Time()
    Fill_Stuff_In(FinalTargetString + SeatNo +"/" + TimeNo)

def Fill_Stuff_In(Link:str):
    # Fills up the stuff in the main page 

    # calls/Intializes the webdriver ??
    driver= webdriver.Chrome(executable_path=ExecutablePath)
    
    # Gets link from MainFunction() and calls opens it 
    driver.get(Link)
    
    # Sets the name of the user
    Set_Name = driver.find_element(By.NAME,"field_reservation_contact_name[und][0][value]")
    Set_Name.click()
    Set_Name.send_keys("GuruPrasath Gopal")

    # Sets the phone number of the user 
    Set_Number = driver.find_element(By.NAME,"field_reservation_contact_phone[und][0][value]")
    Set_Number.click()
    Set_Number.send_keys("87416283")

    # Sets the email of the user
    Set_Email = driver.find_element(By.NAME,"field_reservation_contact_email[und][0][email]")
    Set_Email.click()
    Set_Email.send_keys("guruprasath_gopal@mymail.sutd.edu.sg")
    
    # Sets the Duration of the slot (currently at 30 mins or 1800 seconds)
    Set_Duration = DropDown(driver.find_element(By.NAME,"duration"))
    Set_Duration.select_by_value("1800")
    
    # Finds the captcha by the class name and gets the digits and performs simple addition and fills it in the field
    element = driver.find_element(By.CLASS_NAME,"field-prefix")
    k = (element.text).split(" ")
    Captcha = int(k[0]) + int(k[2])
    Set_Captcha= driver.find_element(By.NAME,"captcha_response")
    Set_Captcha.send_keys(Captcha)
    
    # Makes the function wait for 10 secs so i can catch my breath
    time.sleep(10)
    
def Find_User_Info():
    # This function allows user to get a preselected data profile (for testing) or enter their own data profile 
    Temp_Dict_Info = {}
    Temp_Dict_Info["UsrPrf"]  = "A"
    Temp_Dict_Info["Name"] = (input("Enter User Name"))
    Temp_Dict_Info["PhoneNumber"] = (input("Enter Phone Number "))
    Temp_Dict_Info["Email"]= (input("Enter Email Id"))
    Temp_Dict_Info["Time"]  = (input("Enter Time in seconds"))
    Dict_Info.append(Temp_Dict_Info.copy())

def Find_Time()->str:
    # Asks the user for input in "dd.mm.yyy" , "hh:mm:ss" format and concatenates them with a space in between and calls the epoch time function
    Date = input("Date in dd.mm.yyyy format")
    Time = input("time hh:mm:ss formats")
    print(Date + " " + Time)
    try:
        TempReturnValue = Epoch_Time(Date+" "+Time)
    except:
        print("\n Oops there seems to be some error , please try again \n")
        Find_Time()

    
    if (TempReturnValue < time.time()):
        print("\n Oops Please Enter again \n")
        Find_Time()
    
    return Epoch_Time(Date+" "+Time)
    # "29.08.2011 11:05:02"

def Epoch_Time(Time_String) ->str:
    # Converts the given time in "dd.mm.yyy hh:mm:ss" into epoch time 
    Converted_Time = time.mktime(time.strptime(Time_String, "%d.%m.%Y %H:%M:%S"))
    return str(int(Converted_Time))

def Find_Seat_Number():
    # Converts Seat input  into Seatnumber

    # This line calls a dummy function currently to convert seat name to seatnumber
    SeatNumber = Get_Seat_Number(Get_Seat())

    return  str(SeatNumber)

def Get_Seat():
    SeatName = input("Give me the seat number")
    return SeatName

def Get_Seat_Number(StName:str)->int:


    # Function to convert seat name to seat number
    if StName !="":
        return 232

print(MainFunction())

