i = 1
user = ""

while(i<=5):
    user = input("Insert any name.\n")
    print("You inserted " + user)
    if(user == "Ana"):
        break
    elif( user == "Davor"):
        continue
    i += 1