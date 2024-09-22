import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    player_choice = input("Enter rock, paper, or scissors: ").lower()
    if player_choice not in ["rock", "paper", "scissors"]:
        return "Invalid choice, please select rock, paper, or scissors."
    
    computer_choice = get_computer_choice()
    
    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    
    return get_winner(player_choice, computer_choice)

# Run the game
if __name__ == "__main__":
    print(play_game())
