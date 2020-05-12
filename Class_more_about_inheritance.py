class Person():
    def __init__(self, name, age, idNum):
        self.name = name
        self.age = age
        self.idNum = idNum

    def output(self):
        print("Your name is " + self.name + " your age is " + self.age + " Your ID num is " + self.idNum)

ana = Person("Ana", "28", "23225655") 

class Man():   #New class that is over Child class
    def strong(self):
        print("Man is strong")

class Child(Person, Man):
    pass
kid = Child("Davor", "28", "232555664")
kid.output()

kid.strong()     # Now kid object will inherit these features
