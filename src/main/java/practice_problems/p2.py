def isPalindromeIterative(text):
    start = 0
    end = len(text) - 1

    while start < end:
        if text[start] != text[end]:
            return False

        start += 1
        end -= 1

    return True


def isPalindromeRecursive(text):
    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return isPalindromeRecursive(text[1:-1])


def isPalindromeArrayReversal(text):
    original = list(text)
    reversed_text = original[::-1]

    return original == reversed_text


text = input("Enter text: ")

iterative = isPalindromeIterative(text)
recursive = isPalindromeRecursive(text)
arrayReversal = isPalindromeArrayReversal(text)

print("Iterative:", "Palindrome" if iterative else "Not Palindrome")
print("Recursive:", "Palindrome" if recursive else "Not Palindrome")
print("Array Reversal:", "Palindrome" if arrayReversal else "Not Palindrome")