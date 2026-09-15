def classifyWordLengths(review):
    words = review.split()

    short = 0
    medium = 0
    long = 0

    for word in words:
        length = len(word)

        if length <= 4:
            short += 1
        elif length <= 8:
            medium += 1
        else:
            long += 1

    print("Short:", short, "| Medium:", medium, "| Long:", long)


review = input("Enter movie review: ")

classifyWordLengths(review)