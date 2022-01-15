#Importing all the headerfiles that i need 
import time
from typing import Dict, List
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select as DropDown

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
Options = {1:"Make a Slot Booking", 2:"exit"}

def LoadDefault()->None:
    # Loads the default user info into a dict
    Temp_Dict = {}
    Temp_Dict["Name"] = DefaultName
    Temp_Dict["PhoneNumber"]  = DefaultPhone
    Temp_Dict["Email"] = DefaultEmail
    Temp_Dict["Time"]  = DefaultTime
    Dict_Info.append(Temp_Dict.copy())
    return None

def ShowAndGetOptions(OptionsDict:dict):
    for key in OptionsDict:
        print("{}. {}".format(key,OptionsDict[key]))
    
    Option = int(input("Please enter your option"))
    if Option in OptionsDict.keys():
        return Option
    else:
        ShowAndGetOptions(Options)

def ShowAndGetOptionsList(ListyList:list):
    
    for i in range(len(ListyList)):
        print("\n--User Profile {} ------".format(i))
        for key in ListyList[i]:
            print("{}. {}".format(key,ListyList[i]))

    Option = int(input("Please enter your option"))
    if Option in    ListyList[0].keys():
        return Option
    else:
        ShowAndGetOptions(Options)
def Routing_function(N:int)->None:
    # This function is to route the functions and the correct options 
    if N==1:
        MainFunction()
    # elif N==3:
        # IamWastingTime()
    elif N==2:
        exit("Thank You for using the bot ")

def MainFunction():
    # Shows the options available and gets input and gets time 
    # and seat info and calls the function to fill up userinfo in the website
    ShowAndGetOptions(Options)
    SeatNo = Find_Seat_Number()
    TimeNo = Find_Time()
    LoadDefault()
    Fill_Stuff_In(FinalTargetString + SeatNo +"/" + TimeNo)



def UserProfile()->int:
    ShowAndGetOptions(Dict_Info)
    pass

def Fill_Stuff_In(Link:str,default = 0):
    # Fills up the stuff in the main page 
    # calls/Intializes the webdriver ??
    driver= webdriver.Chrome(executable_path=ExecutablePath)
    
    # Gets link from MainFunction() and calls opens it 
    driver.get(Link)
    
    # Sets the name of the user
    Set_Name = driver.find_element(By.NAME,"field_reservation_contact_name[und][0][value]")
    Set_Name.click()
    Set_Name.send_keys(Dict_Info[default]["Name"])

    # Sets the phone number of the user 
    Set_Number = driver.find_element(By.NAME,"field_reservation_contact_phone[und][0][value]")
    Set_Number.click()
    Set_Number.send_keys(Dict_Info[default]["PhoneNumber"])

    # Sets the email of the user
    Set_Email = driver.find_element(By.NAME,"field_reservation_contact_email[und][0][email]")
    Set_Email.click()
    Set_Email.send_keys(Dict_Info[default]["Email"])
    
    # Sets the Duration of the slot (currently at 30 mins or 1800 seconds)
    Set_Duration = DropDown(driver.find_element(By.NAME,"duration"))
    Set_Duration.select_by_value(Dict_Info[default]["Time"])
    
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
    # Asks the user for input in "dd.mm.yyy" , "hh:mm:ss" format and concatenates 
    # them with a space in between and calls the epoch time function
    Date = input("Date in dd.mm.yyyy format")
    Time = input("time hh:mm:ss formats")
    print(Date + " " + Time)
    TempReturnValue = Epoch_Time(Date+" "+Time)

    if (float(TempReturnValue) < time.time()):
        print("\n Oops Please Enter again \n")
        Find_Time()
    
    return Epoch_Time(Date+" "+Time)
    # "29.08.2011 11:05:02"

def Epoch_Time(Time_String) ->str:
    # Converts the given time in "dd.mm.yyy hh:mm:ss" into epoch time 
    Converted_Time = time.mktime(time.strptime(Time_String, "%d.%m.%Y %H:%M:%S"))

    
    if (CheckTime(Time_String,Converted_Time)):
        return str(int(Converted_Time))
    else:
        print(Converted_Time)
        print(CorrectConvertedTime(Converted_Time))
        return CorrectConvertedTime(Converted_Time)
        
def CorrectConvertedTime(Converted_Time):
    # Approximates time to nearest 30minute slot
    if (Converted_Time-(Converted_Time//1800)*1800)>900:
        return((Converted_Time//1800)*1800 + 1800)
        
    return (Converted_Time//1800)*1800
        
def CheckTime(Time_String:str,Converted_Time):
    # Checks if the time slot is in %1800
    TempTime_String =Time_String.split(" ")[0] # This and the next line might not be necessary 
    Converted_Time_Check = time.mktime(time.strptime(TempTime_String, "%d.%m.%Y"))
    if ((Converted_Time-Converted_Time_Check)%1800 ==0):
        return True
    return False

def Find_Seat_Number():
    # Converts Seat input  into Seatnumber
    # This line calls a dummy function currently to convert seat name to seatnumber
    SeatNumber = Get_Seat_Number(Get_Seat())

    return  str(SeatNumber)

def Get_Seat():
    SeatName = input("Give me the seat number")
    return SeatName

def Get_Seat_Number(StName:str)->int:
    # Compares a txt file and converts seat name into seat number
    with open ("throwaway3.txt","r") as f:
        TempContent = f.readlines()
    TempContent = [x.strip("\n") for x in TempContent]
    
    # Runs through the txt file if a reference is found  , it prints that
    for i in range(len(TempContent)):
        TempSeatString = TempContent[i][:len(TempContent[i])-4]
        TempSeatNumber = TempContent[i][len(TempContent[i])-3:]

        if (TempSeatString == StName):
            return TempSeatNumber

    print("Looks Like the inputed string is wrong")    
    Find_Seat_Number()

MainFunction()
 