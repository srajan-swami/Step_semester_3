def printFilteredWordFrequency(feedback):
    stopWords = {"the", "was", "and", "a", "is", "of", "in"}

    feedback = feedback.lower()
    feedback = feedback.replace(".", "")
    feedback = feedback.replace(",", "")

    words = feedback.split()

    frequency = {}

    for word in words:
        if word not in stopWords:
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1

    sortedWords = sorted(
        frequency.items(),
        key=lambda item: item[1],
        reverse=True
    )

    for word, count in sortedWords:
        print(word + ":", count)


feedback = input("Enter feedback: ")
printFilteredWordFrequency(feedback)