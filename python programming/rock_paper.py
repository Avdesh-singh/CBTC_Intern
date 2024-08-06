import random

def get_player_choice(player_num):
    choice = input(f"Player {player_num}, enter your choice (rock, paper, or scissors): ").strip().lower()
    while choice not in ["rock", "paper", "scissors"]:
        choice = input(f"Invalid choice. Player {player_num}, please enter rock, paper, or scissors: ").strip().lower()
    return choice

def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return 0
    elif (choice1 == "rock" and choice2 == "scissors") or (choice1 == "paper" and choice2 == "rock") or (choice1 == "scissors" and choice2 == "paper"):
        return 1
    else:
        return 2

def main():
    while True:
        print("Rock, Paper, Scissors Game!")
        player1_choice = get_player_choice(1)
        player2_choice = get_player_choice(2)

        print(f"Player 1 chose {player1_choice}")
        print(f"Player 2 chose {player2_choice}")

        winner = determine_winner(player1_choice, player2_choice)
        
        if winner == 0:
            print("It's a tie!")
        elif winner == 1:
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
        
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    main()