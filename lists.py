'''
lists
* collection of data
* cab contain any/all data types in a single list
* can contain other collections (lists, dictionaries, sets, tuples) as list items
* mutable (items can be added, removed, changed)
* maintain order (can use index to find an item)
'''

# list methods

fruits = ["peaches", "apples", "pears", "apples", "apples"]
years = [3, "1998", 2.5, 987, "1994"]

print("apple" in fruits)
print("apples" in fruits)
print(fruits.count("apples"))
print(fruits.count("apple"))

print(fruits.index("apples"))

"""
print(fruits, years)

fruits.append("oranges")
print(fruits)

fruits.extend(years)
print(fruits)

fruits.remove("oranges")
print(fruits)

# removes first item in list
fruits.pop(0)
print(fruits)

# removes last item in list
fruits.pop(-1)
print(fruits)

# To use sort items must be all the same type ie. string or int and float. int and float can be sorted together.
numbers = [5, 1928, 4, 17, 68]
numbers.sort()
print(numbers)
"""
