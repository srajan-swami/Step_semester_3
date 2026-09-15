def countVowelsAndConsonants(text):
    vowels = 0
    consonants = 0

    for char in text:
        char = char.lower()

        if char in "aeiou":
            vowels += 1
        elif char != " ":
            consonants += 1

    print("Vowels:", vowels, "| Consonants:", consonants)


text = input("Enter text: ")

countVowelsAndConsonants(text)