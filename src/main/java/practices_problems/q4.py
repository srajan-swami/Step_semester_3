def maskPhoneNumber(phone):
    if len(phone) != 10 or not phone.isdigit():
        return "Invalid phone number"

    maskedNumber = "XXXXXX-" + phone[-4:]
    return maskedNumber


phone = input("Enter phone number: ")
print(maskPhoneNumber(phone))