from random import choice

WINNING_SCORE = 3
CHOICES = ("rock", "paper", "scissors")
WIN = {("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")}

print("Welcome to Rock Paper Scissors! (type 'exit' to quit)")
p1_score = p2_score = 0

while p1_score < WINNING_SCORE and p2_score < WINNING_SCORE:
    p1 = input("Your move [rock/paper/scissors]: ").strip().lower()
    if p1 in {"exit", "quit", "q"}:
        print("Game exited.")
        break
    if p1 not in CHOICES:
        print("Invalid input! Please choose rock, paper, or scissors.")
        continue

    p2 = choice(CHOICES)
    print(f"CPU chose {p2}")

    if p1 == p2:
        print("Draw!")
    elif (p1, p2) in WIN:
        p1_score += 1
        print("You win this round!")
    else:
        p2_score += 1
        print("CPU wins this round!")

    print(f"Score: You {p1_score} — CPU {p2_score}\n")

if p1_score == WINNING_SCORE:
    print("🎉 You won the match!")
elif p2_score == WINNING_SCORE:
    print("😅 CPU won the match!")
