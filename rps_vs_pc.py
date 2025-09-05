from random import randint

print("Welcome to Rock Paper Scissors!")
valid_choices = ["rock", "paper", "scissors"]
p1 = input("Player 1 select Rock, Paper or Scissors: ").lower()

p2 = valid_choices[randint(0,2)]

if p1 not in valid_choices:
    print("Invalid input! Please choose Rock, Paper, or Scissors.")
elif p1 == p2:
    print("Draw!")
elif p1 == "rock" and p2 == "scissors":
    print("Player 1 wins!")
elif p1 == "paper" and p2 == "rock":
    print("Player 1 wins!")
elif p1 == "scissors" and p2 == "paper":
    print("Player 1 wins!")
else:
    print("Player 2 wins!")
