def checkTypingAccuracy(original, typed):
    matched = 0
    firstMismatch = -1

    for i in range(len(original)):
        if original[i] == typed[i]:
            matched += 1
        elif firstMismatch == -1:
            firstMismatch = i

    total = len(original)
    accuracy = (matched / total) * 100

    if firstMismatch == -1:
        print(f"Matched: {matched}/{total} | Accuracy: {accuracy:.2f}% | No Mismatches")
    else:
        print(
            f"Matched: {matched}/{total} | Accuracy: {accuracy:.2f}% | "
            f"First Mismatch at position {firstMismatch + 1} "
            f"('{original[firstMismatch]}' vs '{typed[firstMismatch]}')"
        )


original = input("Enter original passage: ")
typed = input("Enter typed text: ")

checkTypingAccuracy(original, typed)