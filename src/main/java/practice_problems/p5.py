def reverseCustomerName(customerName):
    reversedName = ""

    for i in range(len(customerName) - 1, -1, -1):
        reversedName += customerName[i]

    return reversedName


customerName = input("Enter customer name: ")

reversedName = reverseCustomerName(customerName)

print("Original Name:", customerName)
print("Reversed Name:", reversedName)