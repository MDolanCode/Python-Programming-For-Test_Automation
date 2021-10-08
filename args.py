# Positional Arguments are read in the order and Python cannot tell what argument should be where. It just goes in order.
def user_info(name, age, city):
    '''This function prints name, age, and city
     from an argument provided to the function.'''

    print("{} is {} years old, from {}". format(name, age, city))

user_info("Janet", 58, "Oklahoma City")

# You need all the arguments or you will get an error
# user_info(34, "New York")

# Key word arguments
def user_info2(name, age=0, city="Tucson"):
    print("{} is {} years old, from {}".format(name, age, city))

user_info2("Micah")
user_info2(age=56, name="Kadeem")

# *args & **kwargs
'''
*args: allows for unlimited variable to be passed 
into a function without defining them ahead of time.
'''
'''
**kwargs: allows for unlimited keyword arguments to be passed 
into a function without defining them ahead of time.
'''
'''
All three argument types can be used in a single function. 
They must be used in order: formal positional arguments, *args, **kwargs. 
'''
def application(fname, lname, email, company, *args, **kwargs):
    print("{} {} works at {}. Her email is {}.".format(fname, lname, company, email))

application("Jess", "Ingrass", "mail@mail.com", "Teachcode.org", 75000, hire_date="September 2010")
