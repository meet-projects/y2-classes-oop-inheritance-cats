class Animal():
    def drink(self):
        print("hhhhhhhh")

class HairyAnimal():
    def has_hair(self):
        return True

class Mammal(Animal):
    def drink(self):
        print("glueglueglue")

class Cat(Mammal, HairyAnimal):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.lives = 9
        print("Hi I'm " + self.name + " and I'm " + str(self.age) + " years old")


    def drink(self):
        print("psskhkhwop")
        super().drink()
        super(Mammal, self).drink()
        Animal.drink(self)
        

y = Cat("Charlie", 11)
print("dict output: " + str(y.__dict__()))
print("dict output: " + str(y.__class__))
y.drink()
print("do I have hair? " + str(y.has_hair()))
