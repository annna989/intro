dic = {"Toyota":"Camy", "Cilinder":"v8"}

print(dic["Toyota"])
print(dic["Cilinder"])

#Adding New kay value

dic["Color"] = "Withe"
print(dic["Color"])

#Filling empty dictionaries

dic = {}

dic["Car"] = "bmw"
dic["audi"] = "black"
print(dic)

#Edit a Value in dictionaries
OS = {"Apple": "Mack","Microsoft": "Windows"}
#To edit that

print("Before is " + OS["Apple"])
OS["Apple"] = "Linux"

print("Now is " + OS["Apple"])

print(OS)


#To delete a kay with its value in Dictionaries
print("Before Deletion")
print(OS)

del OS["Apple"]
print("After delection")
print(OS) 