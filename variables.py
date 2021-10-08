_cars = 23
cars = 24

CARS = 25

number_of_cars = 23
kind_of_cars = "Ferrari"

print(_cars)
print(cars)
print(CARS)
print(number_of_cars)
print(kind_of_cars)

 # stings can use "" or ''
 # strings are also immutable and operations cannot be performed on them.

 # Integers - mathematical operations can be performed.

 # Floating Point - frational numbers, mathematical operations can be performed, Python calculates places for you9no specification needed)
 # examples 3.14, 9.86, 234.09823

"""
This is a multi-line comment
you can use this kind of comment to make longer notes as you are learning.
in Python, these are often used as docstrings.
 
We will do formatting now.
"""

name = "Janelle Jones"
type_of_car = "Rolls Royce"
school = "Foundation Elementary School"

print(name + school)
print(name + " " + school)
print(name + " works at " + school)

#python string.format()
print("{} works at {}.".format(name, school))