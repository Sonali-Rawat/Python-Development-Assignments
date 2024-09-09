# program that prints the multiplication table of a given number using a while loop.

number = int(input("Enter a number to print its multiplication table: "))

# Initialize the multiplier
multiplier = 1

while multiplier <= 10:
    print(f"{number} x {multiplier} = {number * multiplier}")
    multiplier += 1
