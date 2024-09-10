# program that iterates through numbers 1 to 10 and prints each number. Use the continue statement to skip numbers that are divisible by 3.
for number in range(1,11):
    if number % 3 == 0:
        continue

    print(number)