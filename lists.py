import random  # Importing the random module for generating random numbers

var = []  # Creating an empty list called var

print(type(var))  # Printing the type of var (it should be list)

print(var)  # Printing the content of var (it should be an empty list)

print(len(var))  # Printing the length of var (it should be 0)

var2 = [151, 251, 386, 493, 649]  # Creating a list var2 with some initial values

print(var2)  # Printing the content of var2

var3 = [151, 251, 386, 493, 649, "009"]  # Creating a list var3 with both numbers and a string

print(var3)  # Printing the content of var3

var3.append(721)  # Appending the number 721 to var3

print(var3)  # Printing the updated content of var3

print(dir(var3))  # Printing the list of attributes and methods of var3

print(dir(str))  # Printing the list of attributes and methods of the string class

numbers = [1, 2, 3, 4, 5, 6]  # Creating a list numbers with some numbers

print(numbers)  # Printing the content of numbers

print(numbers[3])  # Printing the element at index 3 of numbers

new_numbers = range(6)  # Creating a range object with numbers from 0 to 5

print(new_numbers)  # Printing the range object

print(type(new_numbers))  # Printing the type of new_numbers (it should be range)

new_numbers = list(new_numbers)  # Converting the range object to a list

print(new_numbers)  # Printing the content of new_numbers

print(type(new_numbers))  # Printing the type of new_numbers (it should be list)

new_numbers.reverse()  # Reversing the order of elements in new_numbers

print(new_numbers)  # Printing the reversed new_numbers

print(new_numbers[3])  # Printing the element at index 3 of new_numbers

print(new_numbers.index(1))  # Printing the index of the element 1 in new_numbers

try:
    print(new_numbers.index(7))  # Trying to print the index of the element 7 in new_numbers
except Exception as e:
    print(e)  # Printing the exception if 7 is not found in new_numbers

for new_number in new_numbers:  # Iterating over each element in new_numbers
    print(new_number, new_number**3)  # Printing the element and its cube

print(len(new_numbers))  # Printing the length of new_numbers

list_of_lists = [[random.randint(0,9), random.randint(0,9), random.randint(0,9)] for i in range(5)]  # Creating a list_of_lists with five lists of three random numbers each

list_of_lists.insert(2, [0, 1, 2] )  # Inserting a list [0, 1, 2] at index 2 of list_of_lists

print(list_of_lists)  # Printing the content of list_of_lists

for list_element in list_of_lists:  # Iterating over each list in list_of_lists
    print(list_element)  # Printing the list
    for element in list_element:  # Iterating over each element in the list
        print(element)  # Printing the element
