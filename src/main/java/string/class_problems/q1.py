number = int(input("Enter a number: "))

isPrime = True

for i in range(2, number):
    if number % i == 0:
        isPrime = False
        break

print("Is the number", number, "a Prime number?", isPrime)