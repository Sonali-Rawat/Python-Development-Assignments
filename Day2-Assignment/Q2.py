#  Python program that takes user input to add multiple elements to an array and then prints the final array:
numbers = []

num_elements = int(input("How many elements do you want to add to the array? "))

for i in range(num_elements):
    element = int(input(f"Enter element {i+1}: "))
    numbers.append(element)

# Print the final array
print("Final array:", numbers)
