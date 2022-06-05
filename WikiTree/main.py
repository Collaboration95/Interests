from multiprocessing.sharedctypes import Array
from typing import List
import requests 

# x = requests.get("https://en.wikipedia.org/wiki/Silicon_Valley_(TV_series)")

# def MainFunction():
# # This is the main function where everything happens 
#     if x.status_code==200:
#         print("Lets Go Ahead")
#     else:
#         print("There is a problem")

# Appending text to a textfile
    # with open ("Balance.txt","a") as f:
    #     f.write("{} {} {} {}".format(UnixTime,NormalTime,Balance,HashedName))
    #     f.write("\n")

# Reading text from a textfile
    # with open("Balance.txt","r") as f:
    #     TempContent = f.readlines()

    # TempContent = [x.strip("\n") for x in TempContent ]
    # temp2 = []
    # for i in range(len(TempContent)):
    #     A  = TempContent[i].split(" ")

def CLI():
    # This is a temporary commandline interface until i get the react app working 
    pass

def Brains(Title:str)->None:
    # Credits to Bill The Lizard https://stackoverflow.com/users/1288/bill-the-lizard
    session = requests.Session()

    url = "https://en.wikipedia.org/w/api.php"
    params = {
    "action": "query",
    "format": "json",
    2: Title,
    "prop": "links",
    "pllimit": "max"
    }

    response = session.get(url=url, params=params)
    data = response.json()
    pages = data["query"]["pages"] 

    pg_count = 1
    page_titles = []


    for key, val in pages.items():
        for link in val["links"]:
            page_titles.append(link["title"])

    while "continue" in data:
        plcontinue = data["continue"]["plcontinue"]
        params["plcontinue"] = plcontinue

        response = session.get(url=url, params=params)
        data = response.json()
        pages = data["query"]["pages"]

# Credits to Bill The Lizard https://stackoverflow.com/users/1288/bill-the-lizard
    print("This is the data")
    print(page_titles)
    with open ("CurrentLinks.txt","w") as f:

        for i in range(len(page_titles)):
            f.write("{}".format(page_titles[i]))
            f.write("\n")

def Routing_function(N:int)->None:
    # This function is to route the functions and the correct options \
    # Code copied from my previous project ( Threat_Level_Midnight )
    if N==1:
        Brains(Get_Input("Please Enter Root Node"))
    elif N==2:
        exit("Bye")

    elif N==4:
        pass
    elif N==3:
        pass
def Show_And_Get_Options(Current_Options:dict)->int:
    # Code from ThreatLevelMidnight project
    # This functions accepts a dictionary of the available options and returns the integer (Key) of the option
    # This shows the different options and returns the "Chosen one"
    while True:
        # This loops until the user selects a valid option or throws his system off a cliff
        for key in Current_Options:
            print("{} : {}".format(key , Current_Options[key]))
        print("\n")
        # For loop to loop through the dictionary and display options
        A = int(input("Please choose an option") )
        # Takes an input for option

        # checks if option is valid
        if A in Current_Options:
            return A
        else:
            print("Well looks like you are one of those dumb users we have to be on the lookout for\n ")
            print("----CHOOSE A VALID OPTION-----")
            print("\n")

options =   {1:"Make a new Request",2:"exit"}

def Starter():
    Routing_function(Show_And_Get_Options(options))



def Get_Input(data:str)->str:
    return str(input(data+":"))



Starter()



