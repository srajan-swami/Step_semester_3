import random


def playRound(playerMove, computerMove):
    if playerMove == computerMove:
        return "Draw"

    if (playerMove == "Rock" and computerMove == "Scissors") or \
       (playerMove == "Paper" and computerMove == "Rock") or \
       (playerMove == "Scissors" and computerMove == "Paper"):
        return "Player Wins"

    return "Computer Wins"


playerMoves = []
computerMoves = []
results = []

wins = 0
losses = 0
draws = 0

for i in range(5):
    playerMove = input(
        f"Round {i + 1} - Enter Rock, Paper, or Scissors: "
    ).capitalize()

    computerMove = random.choice(["Rock", "Paper", "Scissors"])

    result = playRound(playerMove, computerMove)

    playerMoves.append(playerMove)
    computerMoves.append(computerMove)
    results.append(result)

    print("Computer:", computerMove)
    print("Result:", result)
    print()

    if result == "Player Wins":
        wins += 1
    elif result == "Computer Wins":
        losses += 1
    else:
        draws += 1

winPercentage = (wins / 5) * 100

print("Final Summary")
print("-" * 55)
print("Round | Player Move | Computer Move | Result")
print("-" * 55)

for i in range(5):
    print(
        f"{i + 1:<5} | "
        f"{playerMoves[i]:<11} | "
        f"{computerMoves[i]:<13} | "
        f"{results[i]}"
    )

print("-" * 55)
print("Wins:", wins)
print("Losses:", losses)
print("Draws:", draws)
print("Win % =", winPercentage, "%")