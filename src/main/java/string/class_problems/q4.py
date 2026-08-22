number1 = int(input("Enter number1: "))
number2 = int(input("Enter number2: "))

origNumber1 = number1
origNumber2 = number2

while number2 != 0:
    remainder = number1 % number2
    number1 = number2
    number2 = remainder

print("The GCD of", origNumber1, "and", origNumber2, "is", number1)