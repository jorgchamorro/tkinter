number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

largest_number = None
if number1 > number2 and number1 > number3:
    largest_number = number1
if number2 > number1 and number2 > number3:
    largest_number = number2
if number3 > number1 and number3 > number2:
    largest_number = number3

print("The largest number is: ", largest_number)