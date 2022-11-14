Options  = {1:"QuickRun",2:"DummyFunction",3:"Gime A Chart",4:"exit"}
Pi  = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989"

def ShowAndGetOptions(OptionsDict:dict)->int:
    for key in OptionsDict:
        print("{}. {}".format(key,OptionsDict[key]))
    
    Option = int(input("Please enter your option"))
    if Option in OptionsDict.keys():
        return Option
    else:
        ShowAndGetOptions(Options)

def QuickRun():
    print("Now lets start the QuckRun")
    print("3.",end="")
    A = int(input())
    l = len(str(A))
    C = int(Pi[2:l+2])

    if A == C:
        print("You are correct!")

    pass
def QuickRunFailedImplement():
    print("Now ,Lets Start the QuickRun")
    start = 0
    M = []

    # while(True):
    #     if int(Pi[start]) !=int(input()):
    #         M.append({start : Pi[start]})
    #         pass


    pass

def Routing_function(N:int)->None:
    # This function is to route the functions and the correct options 
    if N==1:
        QuickRun()
    elif N==2:
        pass
    elif N==3:
        print("Here we go again!")
        pass
        
    elif N==4:
        exit("Thank You for using the bot ")

def MainFunction()->None:
    # This is the first function that is called when the program is executed
    Routing_function(ShowAndGetOptions(Options))

MainFunction()