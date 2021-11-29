# Create a Higher-Lower game using the number of instagram followers

import random

from art import logo, vs
from game_data import data
from os import system, name

game_data = data
guessed_right = True
current_score = 0
print(logo)


# Clear the console
def clear():

    # For Windows
    if name == 'nt':
        _ = system('cls')
    # For Mac and Linux
    else:
        _ = system('clear')


# Generates the information from the game_data
def information():
    final_data = random.choices(game_data, k=2)

    if final_data[0] == final_data[1]:
        final_data = random.choices(game_data, k=2)

    print(f"Compare A: {final_data[0]['name']}, a {final_data[0]['description']}, from {final_data[0]['country']}")

    print(vs)

    print(f"Against B: {final_data[1]['name']}, a {final_data[1]['description']}, from {final_data[1]['country']}")

    return final_data


# Compares both data generated
def comparison(final_data):
    global current_score
    global guessed_right
    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    clear()

    if user_choice == 'A' and final_data[0]['follower_count'] > final_data[1]['follower_count']:
        current_score += 1
        print(logo)
        print(f"You're right! Current score: {current_score}.")
    elif user_choice == 'B' and final_data[1]['follower_count'] > final_data[0]['follower_count']:
        current_score += 1
        print(logo)
        print(f"You're right! Current score: {current_score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {current_score}")
        guessed_right = False


while guessed_right:
    comparison(information())