"""
What is Inheritance?
* Using attributes from one class in another class

class Person():
    def __init__(self, attribute, attribute2):

class Enemy(Person):
    def __init__(self, new_attribute, attribute, attribute2):
        super().__init__(self, attribute, attribute2)
        self.new_attribute = new_attribute
"""

"""
Multiple Inheritance
* When one class inherits from multiple classes, 
  and is able to use attributes and methods from both classes.

  PROS: The ability to reuse small amounts of code in multiple classes and mix ins.
  CONS: The order of inheritance matters. Inheriting from multiple classes can become quite complicated depending on
        the number of classes, the names of class methods, and other factors including common attributes shared among 
        multiple parent classes.
        There can be more maintenance involved when refactoring code that is using multiple inheritance.

There are 2 ways to do multiple inheritance in Python. 
1st way is not as Pythonic and requires a bit more maintanence. 
However, it is easy to see what is happening. 

class Animal(): 
    def __init__(self, sound, look):

2nd way is to continue to use the super method with a single inheritance. 
However, this method can be complicated and quite confusing, so we won't use it in the video. 
However, you can do research on multiple inheritance in Python and using the super method 
and the method resolution order or MRO to learn more about how these things work in Python.

class Place(): 
    def __init__(self, climate, lat, lon):

Typically if we have multiple classes that we want to inherit from we'll have the attributes of each class and then 
bring in the attributes of the class individually into the initialization or init method of the child class. This gives 
us access to methods and attributes of both parent classes.

class Mammal(Animal, Place):
    def __init__(self, sound, look, lat, lon, food):
        Animal.__init__(self, sound, look)
        Place.__init__(self, climate, lat, lon)
        self.food = food
"""

# Parent class 1
class Item():
    def __init__(self, sku):
        self.sku = sku

    def print_sku(self):
        print("The sku is {}.".format(self.sku))

# Parent class 2
class Garment():
    def __init__(self, section, type):
        self.section = section
        self.type = type

    def print_garment(self):
        print("The garment is in section {}, {}".format(self.section, self.type))

# Child Class
class Shirts(Item, Garment):
    def __init__(self, sku, section, type, name, color):
        self.name = name
        self.color = color
        Item.__init__(self, sku)
        Garment.__init__(self, section, type)

    def print_shirt(self):
        print("{} {} on sale!".format(self.color, self.name))

Blouse = Shirts("00001", 43, "Tops", "Formal Blouce", "White")

Blouse.print_sku()
Blouse.print_garment()
Blouse.print_shirt()

"""
Polymorphism (Method overriding)
* Occurs when we want to allow the child class to have a method with the same name and a similar implementation
as the parent class and we wish for that method to override the parent class method.
"""

