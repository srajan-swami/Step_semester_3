def reverseEachWord(sentence):
    words = sentence.split(" ")
    reversedWords = []

    for word in words:
        reversedWord = ""

        for i in range(len(word) - 1, -1, -1):
            reversedWord += word[i]

        reversedWords.append(reversedWord)

    return " ".join(reversedWords)


sentence = input("Enter sentence: ")
print(reverseEachWord(sentence))