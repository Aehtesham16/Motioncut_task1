import random

def guess_the_number():
    print("Welcome to 'Guess the Number'!")
    number = random.randint(1, 100)  # Random number between 1 and 100
    attempts = 10  # Maximum number of attempts

    print("I've picked a number between 1 and 100. Can you guess it?")
    print(f"You have {attempts} attempts to guess the correct number.")

    # Game loop
    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}/{attempts}: Enter your guess: "))

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number {number} in {attempt} attempts.")
            break
    else:
        print(f"Sorry, you're out of attempts. The correct number was {number}.")

# Run the game
if __name__ == "__main__":
    guess_the_number()
