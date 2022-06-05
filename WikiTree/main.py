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
    # This is serving as a temporary user interface for my python backend
    pass

def Brains():
    # Credits to Bill The Lizard https://stackoverflow.com/users/1288/bill-the-lizard
    session = requests.Session()

    url = "https://en.wikipedia.org/w/api.php"
    params = {
    "action": "query",
    "format": "json",
    "titles": "Albert Einstein",
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

