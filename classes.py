"""
python classes

class features - Single file per class
                OR
                Multiple classes can be contained in one file.

inheritance: derived/child class can use attributes and methods of parent class.

multiple inheritance: derived/child class can inherit attributes and methods from more than one class.

polymorphism: derived/child classes can override class methods of parent class.

All classes are objects.

Class variables: for use by all the methods in the class.
Instance variables: for use by the specific methods in which the variable is declared/created.

"""

# __init__method
"""
__init__

* sets attributes for an object at object creation; is a constructor**

    __init__ method is not required BUT is generally used to set default state of object when it is created.
    
    The __init__ method is the first method for a class.
    
    **the word constructor is another word that can be used to refer to the __init__ method.
"""

"""
Self

* Self-referencing variable
* Used to reference the object that is constructed by the init method.

"""

class Person:
    def __init__(self, firstname, lastname, health, status):
        " initialize attributes to be used in/available for all of \
        class methods in this class, and for class objects created \
        by this class."

        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def introduce(self):
        "All people introduce themselves."
        print("Hello, my name is {} {}".format(self.firstname, self.lastname))


    def emote(self):
        emotion = random.randrange(1,3)
        if emotion == 1:
            print("{} is happy today".format(self.firstname))
        elif emotion == 2:
            print("{} is sad right now".format(self.firstname))

    def status_change(self):
        if self.health == 100:
            print("{} is totally healthy!".format(self.firstname))
        elif self.health >= 76:
            print("{} is a little tired today.".format(self.firstname))
        elif self.health >= 51:
            print("{} feels unwell.".format(self.firstname))
        elif self.health >= 40:
            print("{} goes to the doctor.".format(self.firstname))
        else:
            print("{} is unconscious.".format(self.firstname))


Maria = Person("Maria", "Gutierrez", 95, status=True)
Rey = Person("Rey", "Jones", 88, status=False)
Lee = Person("Lee", "Williams", 72, status=True)

print("{} is my friend? {}".format(Maria.firstname, Maria.status))
print("{} is my friend? {}".format(Rey.firstname, Rey.status))

Maria.introduce()
Rey.introduce()
Lee.introduce()

Maria.status_change()
Rey.status_change()
Lee.status_change()


class Enemy(Person):
    def __init__(self, weapon, firstname, lastname, health, status):
        super().__init__(firstname, lastname, health, status)
        self.weapon = weapon

    """ Polymorphism(Method overriding) """
    def introduce(self):
        print("You are my mortal enemy!!!!")

    def hurt(self, other):
        if self.weapon == 'rock':
            other.health -= 10
        elif self.weapon == 'stick':
            other.health -= 5
        print(other.health)

    def insult(self, other):
        if other.health <= 80:
            print("{}, you are tired and weak.".format(other.firstname))

    def steal(self, other):
        print("ha ha ha, {}, I have your stuff!".format(other.firstname))
        if other.status == True:
            other.status = False

Alex = Enemy('rock', 'Alex', 'Wayne', 75, status = False)
Alex.hurt(Maria)
Alex.insult(Rey)
Alex.insult(Lee)
Alex.steal(Rey)

Alex.introduce()

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




