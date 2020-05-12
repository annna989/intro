class Person():
    def __init__(self, name, age, idNum):
        self.name = name
        self.age = age
        self.idNum = idNum

    def output(self):
        print("Your name is " + self.name + " your age is " + self.age + " Your ID num is " + self.idNum)

ana = Person("Ana", "28", "23225655") # We've used the constructor here __init__
ivan = Person("Ivan", "20", "23544856")
# Print function output

ana.output()

#To access class object's variable or function
print(ana.name)
print(ana.age)
print(ana.idNum)
print(ana.output())

# We've use the dot to access a variable or a function

ivan.output()
print(ivan.name) 