import random

def provide_hint(secret, guess):
    correct_position = 0
    correct_digit = 0
    secret_list = list(secret)
    guess_list = list(guess)
    
    for i in range(len(secret_list)):
        if guess_list[i] == secret_list[i]:
            correct_position += 1
            secret_list[i] = guess_list[i] = None
            
    for i in range(len(secret_list)):
        if guess_list[i] is not None and guess_list[i] in secret_list:
            correct_digit += 1
            secret_list[secret_list.index(guess_list[i])] = None
            
    return correct_position, correct_digit

def play_round(player_num, secret):
    attempts = 0
    while True:
        guess = input(f"Player {player_num}, enter your guess: ")
        attempts += 1
        if guess == secret:
            print(f"Correct! Player {player_num} guessed the number in {attempts} attempts.")
            return attempts
        else:
            correct_position, correct_digit = provide_hint(secret, guess)
            print(f"{correct_position} digits are correct and in the right position.")
            print(f"{correct_digit} digits are correct but in the wrong position.")

def main():
    length_of_number = int(input("Enter the length of the number: "))
    digits = input("Allow repeated digits? (yes/no): ").strip().lower() == 'yes'
    
    def generate_secret():
        if digits:
            return ''.join(random.choices('0123456789', k=length_of_number))
        else:
            return ''.join(random.sample('0123456789', length_of_number))
    
    # Player 1 sets the number
    secret1 = input("Player 1, set your secret number: ").strip()
    
    # Player 2 guesses
    attempts_player2 = play_round(2, secret1)
    
    # Player 2 sets the number
    secret2 = input("Player 2, set your secret number: ").strip()
    
    # Player 1 guesses
    attempts_player1 = play_round(1, secret2)
    
    # Determine the winner
    if attempts_player1 < attempts_player2:
        print("Player 1 wins and is crowned Mastermind!")
    elif attempts_player1 > attempts_player2:
        print("Player 2 wins and is crowned Mastermind!")
    else:
        print("It's a tie!")
        
if __name__ == "__main__":
    main()