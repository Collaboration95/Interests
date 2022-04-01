Options  = {1:"Login",2:"DummyFunction",3:"Gime A Chart",4:"exit"}

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
        print("Here we go again!")
        Chartfunction()
        
    elif N==4:
        exit("Thank You for using the bot ")

def MainFunction()->None:
    # This is the first function that is called when the program is executed
    Routing_function(ShowAndGetOptions(Options))

MainFunction()