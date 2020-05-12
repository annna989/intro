class Pearson():

    def insert(self, name, age, idNum):
        self.name = name
        self.age = age
        self.idNum = idNum

    def output(self):
        print("Your name is " + self.name + 
        " You re age is " + self.age + " your idNum is " 
        + self.idNum)

j = Pearson()
j.insert("Ana", "28", "232257782")
j.output()
