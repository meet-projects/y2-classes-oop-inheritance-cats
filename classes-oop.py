import random

class Cat():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.lives = 9
        print("Hi I'm " + self.name + " and I'm " + str(self.age) + " years old")
    def meow(self):
        print("meow")

    def sleep(self, sleep_iterations):
        print(self.name + ": time for me to sleep!")
        i = 0
        while i < sleep_iterations:
            print("Zzz")
            i += 1

    def is_alive(self):
        if self.lives > 0:
            return True
        else:
            return False

    def kill(self, reason):
        if self.is_alive():
            self.lives -= 1
            print("Got killed because of: " + reason)
            if self.lives == 0:
                print("I'm dead")
        else:
            print("Cat is already dead")

y = Cat("Charlie", 11)
print(y.age)
print(y.name)
y.meow()

x = Cat("Winston", 5)
z = Cat("Cloudy", 3)

cats = []
for i in range(1000):
    cats.append(Cat("Cat " + str(i), i))

#cats[0].sleep()


random_integer = random.randint(0,1000)
cat = cats[random_integer]
cat.kill("Overslept")
