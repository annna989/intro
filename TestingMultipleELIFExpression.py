print("This program checks for zoo dicounts")
print(", and enterance price is $120")

price = 120
times = int(input("Hoy many times did you go to this Zoo before\n"))

if(times == 3):
    price = 120-30
    print("Your total included dicount will be $", price)

elif(times == 4):
    price = 120 - 50
    print("Your total included discount will be $", price)

elif(times == 5):
    price = 120 - 60
    print("Your total included discount will be $", price)

elif(times >= 6):
    print("Your total included discount will be $", price)

else:
    print("Your total price is $", price, "and you are not eligble for dicount in this time")