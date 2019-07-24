# Description

This repo contains code for Classes (Object Oriented Programming) and Inheritance lectures given on July 22nd 2019 and July 23rd 2019 for MEETx.


# classes-oop.py
In class we did the following:
1. Defined a `Cat` class
2. Defined an `__init__` method to we can customize how the object is initialized
    i.   Allowed the `__init__` to take in a name and an age
    ii.  Set the properties `self.name` and `self.age` to the value of the parameters
    iii. Added a `self.lives` property to keep track of how many lives the cat has
4. Defined a `meow` method that makes the cat "meow"
5. Defined a `wsleep` method that takes a `sleep_iterations` as an argument and makes the cat sleep for a that number of iterations
6. Defined an `is_alive` method that returns whether or not the cat still has `> 0` lives
7. Defined a `kill` method that takes a `reason` as an argument and removes one life from the cat if it's still alive, otherwise prints "Cat is already dead"
8. We then created cats, imported the `random` library (at the top of the file for best practice) and picked a cat at random to make it sleep, and the die :(.

# inheritance.py
In class we did the following:
1. Defined a new `Animal` class
2. Defined a `drink` method that makes the animal drink (prints a drinking sound)
3. Copied the Cat class to a new file, and removed all methods except `__init__`
4. Made the Cat class inherit from the Animal class - now our cat can also drink!
6. Overrode the `drink` in cat function to change the drinking behavior - now the cat makes multiple sounds, including the sound other animals make!
7. Defined a new class `HairAnimal`
8. Defined a method `has_hair` to return whether this animal is hairy or not, always returns true
9. Used multiple inheritance to make the cat inherit from the `HairyAnimal` class, now the cat can tell us whether it's hair or not!

# Glossary
## Arguments
Those are what you pass in to a function or method. For example, in the following function, the `sleep_iterations` is the argument.
```python
def sleep(sleep_iterations):
    pass
```
## Class
A Class is what allows us to create custom-type objects and add our own functionality to them. We would otherwise only be using the [built-in types](https://docs.python.org/3/library/stdtypes.html "Python3.7.4 Built-in Types")!

## Instantiate, instance and object
To instantiate a class is to create an instance of that class.
An instance is an object that has a specific type (e.g. type Cat).
An object is simply what we use to describe an actual value that is not of a built-in type.
Those are Best described using an example:
```python
my_cat = Cat("Charlie", 11)
```
What this line of code does is *instantiate* a new Cat.
The variable `my_cat` refers to "an object of type Cat" or, put differently, "an instance of class Cat".

This is simply terminology, it's just what we use to describe those things.

# Reserved Keywords
## object
Every Class [implicitly](https://www.google.com/search?q=define%3A+implicitly&oq=define%3A+implicitly&aqs=chrome..69i57j69i58.3153j0j7&sourceid=chrome&ie=UTF-8) inherits from a special class called `object`. This allows the class to inherit default mehtods.
