import random

number = random.randint(0,10)  # Generate a random integer between 0 and 10

threshold = 5  # Set the threshold value

if number > threshold:  # Check if the number is greater than the threshold
    print("Big number")
elif number < threshold:  # Check if the number is smaller than the threshold
    print("Small number")
else:  # If the number is equal to the threshold
    print(f"Number is {threshold}")

if number > 7:  # Check if the number is greater than 7
    print("Really big number")

print(number)  # Print the generated number
