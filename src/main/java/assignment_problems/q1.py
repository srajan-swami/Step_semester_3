def checkDuplicateSeats(seatNumbers):
    duplicateFound = False

    for i in range(len(seatNumbers)):
        for j in range(i + 1, len(seatNumbers)):
            if seatNumbers[i] == seatNumbers[j]:
                print("Duplicate Seat Number Found:", seatNumbers[i])
                duplicateFound = True

    if not duplicateFound:
        print("No Duplicate Seats Found")


seatNumbers = list(map(int, input("Enter seat numbers: ").split()))

checkDuplicateSeats(seatNumbers)