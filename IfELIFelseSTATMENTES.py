print("This program checks if you are eligbe for loan or not")

salary = int(input("How much is your salary"))

if(salary>1000):
    amount = 200
    print("You are eligbe to get a bank loan py paying", amount, "monthly")
elif(salary == 1000):
    amount=500
    print("you are eligbe to get bank loan with higher monthly price", amount, "monthly")
else:
    print("Sorry you are not eligbe")