import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game")
    
    # User decides the range
    start = int(input("Enter the starting number of the range: "))
    end = int(input("Enter the ending number of the range: "))
    
    # Generate random number within chosen range
    number_to_guess = random.randint(start, end)
    attempts = 0

    print(f"I have chosen a number between {start} and {end}. Can you guess it?")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("⚠️ Please enter a valid number.")

# Run the game
number_guessing_game()
