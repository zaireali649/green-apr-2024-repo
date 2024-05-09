import random  # Importing the random module for generating random numbers

var = {}  # Creating an empty dictionary called var

print(type(var))  # Printing the type of var (it should be dictionary)

print(var)  # Printing the content of var (it should be an empty dictionary)

var2 = {"juice": "cranberry", "movie": "The Lion King", "fruit": "mango"}  # Creating a dictionary var2 with some key-value pairs

print(var2)  # Printing the content of var2

print(var2["fruit"])  # Printing the value associated with the key "fruit" in var2

try:
    print(var2["food"])  # Trying to access the value associated with the key "food" in var2
except Exception as e:
    print("Keyerror", e)  # Printing a message if the key "food" is not found in var2

if "song" in var2:  # Checking if the key "song" is in var2
    print(var2["song"])  # Printing the value associated with the key "song" if it exists
else:
    print("Song not in var2")  # Printing a message if the key "song" is not in var2

var2["drank"] = "Patron"  # Adding a new key-value pair to var2

print(var2)  # Printing the updated content of var2

del var2["drank"]  # Deleting the key-value pair with the key "drank" from var2

print(var2)  # Printing the updated content of var2

var2["movie"] = "Interstellar"  # Updating the value associated with the key "movie" in var2

print(var2)  # Printing the updated content of var2

print(dir(var2))  # Printing the list of attributes and methods of var2

print(list(var2.keys()))  # Printing a list of keys in var2

print(list(var2.values()))  # Printing a list of values in var2

print(list(var2.items()))  # Printing a list of key-value pairs in var2

for k, v in var2.items():  # Iterating over each key-value pair in var2
    print(k, v)  # Printing the key and value

dict_of_lists = {str(i).zfill(2): [random.randint(0,9), random.randint(0,9), random.randint(0,9)] for i in range(5)}  # Creating a dictionary dict_of_lists with keys formatted as two-digit strings and values as lists of three random numbers each

print(dict_of_lists)  # Printing the content of dict_of_lists

for key, value in dict_of_lists.items():  # Iterating over each key-value pair in dict_of_lists
    print(key, value)  # Printing the key and value
    for element in value:  # Iterating over each element in the value list
        print(element)  # Printing the element
