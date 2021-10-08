"""
dictionaries

contents: key/value pairings.
mutable: can be changed.
order: maintain order of entru as of python 3.7.
syntax: curly braces contain keys and values,
        keys and values separated by a colon.
"""
years = {"Layla": 1974, "Ackeem": 1997}

# dictionary methods

stuff = {"food": 15, "energy": 100, "enemies": 3}

# print(stuff.get("food"))

# print(stuff.items())

# print(stuff.keys())

# removes last item in dictionary

# print(stuff.popitem())
# print(stuff)

print(stuff.setdefault("food"))
print(stuff)
print(stuff.setdefault("friends", 123))
print(stuff)


# new_items = {"rocks": 4, "arrows": 18}
# stuff.update(new_items)
# print(stuff)

# new_items = {"rocks": 2, "arrows": 5}
# stuff.update(new_items)
# print(stuff)

# up_new = {"food": 3, "webs": 2}
# stuff.update(up_new)
# print(stuff)

# can add items without creating a new dictionary
# stuff.update(food=400, cookies=6)
# print(stuff)

