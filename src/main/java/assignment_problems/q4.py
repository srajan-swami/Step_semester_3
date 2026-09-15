def analyzeInventory(sectionA, sectionB):
    totalA = 0
    totalB = 0

    # Calculate total quantity of Section A
    for quantity in sectionA:
        totalA += quantity

    # Calculate total quantity of Section B
    for quantity in sectionB:
        totalB += quantity

    # Compare totals
    if totalA == totalB:
        status = "Balanced"
    else:
        status = "Not Balanced"

    # Find highest quantity
    highestQuantity = sectionA[0]
    highestSection = "Section A"
    highestIndex = 0

    for i in range(len(sectionA)):
        if sectionA[i] > highestQuantity:
            highestQuantity = sectionA[i]
            highestSection = "Section A"
            highestIndex = i

    for i in range(len(sectionB)):
        if sectionB[i] > highestQuantity:
            highestQuantity = sectionB[i]
            highestSection = "Section B"
            highestIndex = i

    print("Section A Total:", totalA)
    print("Section B Total:", totalB)
    print("Status:", status)
    print(
        "Highest Quantity:", highestQuantity,
        "(" + highestSection + ", Item", highestIndex + 1, ")"
    )


sectionA = list(map(int, input("Enter quantities for Section A: ").split()))
sectionB = list(map(int, input("Enter quantities for Section B: ").split()))

analyzeInventory(sectionA, sectionB)