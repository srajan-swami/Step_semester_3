def findFirstNonRepeatingChar(text):
    frequency = {}

    # Count frequency of each character
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    # Find first character with frequency 1
    for char in text:
        if frequency[char] == 1:
            return char

    return None


text = input("Enter text: ")

result = findFirstNonRepeatingChar(text)

if result is not None:
    print("First Non-Repeating Character:", "'" + result + "'")
else:
    print("No Non-Repeating Character Found")