class Animal:
    def __init__(self,      name, size):
        self.name=name
        self.size=size
    def pr(self):
        print(self.name, self.size)
class Birds(Animal):
    def __init__(self, name, size, fly):
        self.fly=fly    
    def pr2(self):
        print(self.fly)
class Fish(Animal):
    def __init__(self,swim):
        self.swim=swim    
    def pr3(self):
        print(self.swim)
class Lion(Animal):
    def __init__(self, predator):
        self.predator=predator
    def pr4(self):
        print(self.predator)
a=Animal("Lion",100)
c=Birds("", "", "Doesn't fly")
a.pr()
c.pr2()
"""
class Dad:
    surname="Johnson"
    def printlastname(self):
        print(self.surname)
class Mom:
    surname2="CJ"
    def printlastname2(self):
        print(self.surname2)
        
class child(Dad, Mom):
    pass
    #name="Bill"
    #def printfirstname(self):
    #    print(self.name)

child1=child()
#child1.printfirstname()
child1.printlastname()
child1.printlastname2()
"""
"""
class Parent:
    surname="Johnson"
    def printlastname(self):
        print(self.surname)

class child(Parent):
    name="Bill"
    def printfirstname(self):
        print(self.name)

child1=child()
child1.printfirstname()
child1.printlastname()
"""
"""
class Student:
    def __init__(self,id1,name,surname,age,gender):
        self.id1=id1
        self.name=name
        self.surname=surname
        self.age=age
        self.gender=gender

    def showname(self):
        print("Name is "+self.name) 
    def showother(self):
        print("Other info: ","id: ", self.id1,", surname: ", self.surname,", age: ",  self.age, ", gender: ", self.gender)
s1=Student(111,"Dimash","Kim",14,"Male")

s1.showname()
s1.showother()
"""
"""
class Enemy:
    life=3

    def killEnemy(self):
        self.life-=1
    def showLife(self):
        print(self.life)
enemy1=Enemy()
enemy1.killEnemy()
enemy1.showLife()
"""
"""
class Kazakhstan:
    cities=81
    obl=14
    language="Kazakh"
    valute="Tenge"
    president="Nazarbayev"
    def anotherLang(self):
        self.language+=", Russian"
        print(self.language)
    def printpres(self):
        print(self.president)

k=Kazakhstan()

print(k.cities)
print(k.valute)
k.anotherLang()
k.printpres()
"""
