# Loops

# for loop
fruits = ["apple", "orange", "pear", "cherries", "grapes"]
for fruit in fruits:
    print("Would you like an {} ?".format(fruit))


for number in range(1,11):
    print("Number {}".format(number))

# while loop
temp_f = 40

# break
while temp_f > 32:
    print("The water is {} degrees.".format(temp_f))
    temp_f -= 1
    if temp_f == 33:
        break

# continue
for number in range(1,11):
    if number == 7:
        print("We're skipping number 7.")
        continue
    print("This is the number {}.".format(number))

# pass
for number in range(1,11):
    if number == 3:
        pass
    else:
        print("The number is {}.".format(number))

# loop control
'''
Break - end the loop. go to the next statement in the program(outside the loop).

Continue - skips current part of loop. moves to the next part of the loop.

Pass - skips any part of the loop where "pass" appears. best used for testing code.

'''

