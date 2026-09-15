def checkPinLength(pin):
    if len(pin) != 4:
        print("Invalid PIN — must be exactly 4 digits.")
    else:
        print("PIN length OK")


pin = input("Enter PIN: ")
checkPinLength(pin)