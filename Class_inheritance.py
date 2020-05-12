class Person():
    def __init__(self, name, age, idNum):
        self.name = name
        self.age = age
        self.idNum = idNum

    def output(self):
        print("Your name is " + self.name + " your age is " + self.age + " Your ID num is " + self.idNum)

ana = Person("Ana", "28", "23225655")

class Child(Person):
    pass            #Class inheritance means to creat a class called(Child) that inherits all features (Function and variable) of the base class(parent)
kid = Child("Davor", "28", "232555664")  # Create an object
kid.output()  #Called function