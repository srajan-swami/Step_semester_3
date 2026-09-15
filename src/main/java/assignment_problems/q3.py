def findLongestStreak(signalLog):
    if len(signalLog) == 0:
        print("No signal readings found")
        return

    currentColor = signalLog[0]
    currentStreak = 1

    longestColor = signalLog[0]
    longestStreak = 1

    for i in range(1, len(signalLog)):
        if signalLog[i] == currentColor:
            currentStreak += 1
        else:
            currentColor = signalLog[i]
            currentStreak = 1

        if currentStreak > longestStreak:
            longestStreak = currentStreak
            longestColor = currentColor

    print("Longest Streak:", "'" + longestColor + "'",
          "repeated", longestStreak, "times")


signalLog = input("Enter signal log: ")

findLongestStreak(signalLog)