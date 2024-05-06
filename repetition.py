import random

number = random.randint(0,10)  # Generate a random integer between 0 and 10
counter = 0  # Initialize a counter variable

while number != 7:  # Execute loop until the generated number is not 7
    counter += 1  # Increment the counter by 1
    number = random.randint(0,10)  # Generate a new random number
    
    if counter > 13:  # Check if the counter exceeds 13
        break  # Exit the loop if the condition is met
    
print(counter, number)  # Print the number of iterations and the final number


for i in range(10):  # Loop through the range from 0 to 9
    print(i, "Hello World", i**3)  # Print the index, "Hello World", and the cube of the index
