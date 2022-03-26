with open("Balance.txt","r") as f:
    Tempcontent = f.readlines()

Tempcontent = [x.strip("\n") for x in Tempcontent ]
Tempcontent = [x.strip() for x in Tempcontent]
print(Tempcontent)

