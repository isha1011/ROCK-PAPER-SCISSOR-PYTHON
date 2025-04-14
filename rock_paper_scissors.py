import random

def get_user_choice():
    while True:
        choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        print("Invalid choice! Please try again.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    
    winning_combinations = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    
    if winning_combinations[user_choice] == computer_choice:
        return 'user'
    return 'computer'

def play_game():
    user_score = 0
    computer_score = 0
    rounds_to_win = 2
    
    print("Welcome to Rock Paper Scissors!")
    print(f"First to win {rounds_to_win} rounds wins the game!")
    
    while user_score < rounds_to_win and computer_score < rounds_to_win:
        print(f"\nScore - You: {user_score}, Computer: {computer_score}")
        
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        
        if result == 'tie':
            print("It's a tie!")
        elif result == 'user':
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
    
    print(f"\nFinal Score - You: {user_score}, Computer: {computer_score}")
    if user_score > computer_score:
        print("Congratulations! You won the game!")
    else:
        print("Game Over! Computer wins!")

if __name__ == "__main__":
    while True:
        play_game()
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break