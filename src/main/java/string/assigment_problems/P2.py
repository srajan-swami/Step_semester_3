def classifyNumber(number):
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")


number = int(input("Enter a number: "))
classifyNumber(number)
