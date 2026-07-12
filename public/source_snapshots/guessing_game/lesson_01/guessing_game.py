# Store the secret number the player is trying to guess
secret_number = 5

# Ask the player to enter a guess
# input() gets text from the player
# int() changes that text into a number
guess = int(input("Enter your guess: "))

# Check whether the player's guess matches the secret number
if guess == secret_number:
    # This message runs only when the guess is correct
    print("You got it!")
else:
    # This message runs when the guess is not correct
    print("Not quite.")
