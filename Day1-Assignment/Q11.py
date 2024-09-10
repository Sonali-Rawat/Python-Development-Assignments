# Create a function that takes two numbers as arguments and returns their sum. 

def add_numbers(n1, n2):
    return n1 + n2

n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))

result = add_numbers(n1,n2)

print(f"The sum of {n1} and {n2} is:  {result}")