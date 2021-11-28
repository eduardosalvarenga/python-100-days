# Create a Number Guessing Game

from art import logo
import random

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1, 100)
print(number)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
    player_lives = 10
    print("You have 10 attempts remaining to guess the number.")
else:
    player_lives = 5
    print("You have 5 attempts remaining to guess the number.")


have_not_guessed = True
while have_not_guessed:
    user_guess = int(input("Make a guess: "))

    if user_guess == number:
        print(f"You got it! The answer was {number}.")
        have_not_guessed = False
    elif user_guess < number:
        print("Too low.")
        player_lives -= 1
        print(f"You have {player_lives} attempts remaining to guess the number.")
    elif user_guess > number:
        print("Too high.")
        player_lives -= 1
        print(f"You have {player_lives} attempts remaining to guess the number.")

    if player_lives == 0:
        have_not_guessed = False
        print("You've run out of guesses, you lose.")