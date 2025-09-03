print("Welcome to Rock Paper Scissors!")
player_1_input = input("Player 1 select Rock, Paper or Scissors: ").lower()
player_2_input = input("Player 2 select Rock, Paper or Scissors: ").lower()

if player_1_input == "Rock" and player_2_input == "Paper":
    print("Player 1 wins!")
elif player_1_input == "Paper" and player_2_input == "Scissors":
    print("Player 1 wins!")
elif player_1_input == "Scissors" and player_2_input == "Rock":
    print("Player 1 wins!")
elif player_1_input == player_2_input:
    print("It's a tie!")
else:
    print("Player 2 wins!")