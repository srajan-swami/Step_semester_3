def sumOfNaturalNumbers(n):
    total = 0
    counter = 1

    while counter <= n:
        total = total + counter
        counter = counter + 1

    print("Sum of numbers from 1 to", n, "=", total)


n = int(input("Enter N: "))
sumOfNaturalNumbers(n)