# lets make a minigame with python
# The winner of the game is determined by three simple rules:
# Rock beats Scissors
# Scissors beats Paper
# Paper beats Rock
# The game will be played against the computer.
# The computer will randomly select one of the three options.
# The user will be prompted to select an option.
# The player can choose one of the three options by typing the name of the option
# The player should be warned if they enter an invalid option.
# At each round, the player must enter an option, and be informed of the result of the round.
# Display the player's score at the end of every three rounds.
# By the end of each three rounds, the player can choose to play again or exit the game.
# The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.
# The game must be able to handle both uppercase and lowercase inputs.

import random

def game():
    print("Welcome to Rock, Paper, Scissors!")
    print("The rules are simple: Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.")
    print("You will be playing against the computer. Good luck!")
    player_score = 0
    computer_score = 0
    while True:
        for i in range(3):
            print(f"Round {i + 1}")
            print("Select an option: Rock, Paper, or Scissors.")
            player = input().lower()
            computer = random.choice(["rock", "paper", "scissors"])
            if player == "rock" or player == "paper" or player == "scissors":
                if player == computer:
                    print(f"Computer chose {computer}. It's a tie!")
                elif player == "rock" and computer == "scissors":
                    print(f"Computer chose {computer}. You win!")
                    player_score += 1
                elif player == "scissors" and computer == "paper":
                    print(f"Computer chose {computer}. You win!")
                    player_score += 1
                elif player == "paper" and computer == "rock":
                    print(f"Computer chose {computer}. You win!")
                    player_score += 1
                else:
                    print(f"Computer chose {computer}. You lose!")
                    computer_score += 1
            else:
                print("Invalid option. Please try again.")
        print(f"Player score: {player_score}")
        print(f"Computer score: {computer_score}")
        print("Do you want to play again? (yes or no)")
        play_again = input().lower()
        if play_again == "no":
            break
    print("Thanks for playing!")

game()

   
