# Create a rock, paper scissor random game
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

computer_number = int(random.randint(0,2))

user_number = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

images = [rock, paper, scissors]

if user_number > 2 or user_number < 0:
    print("Invalid number")
else:
    print("You chose\n" + images[user_number])
    print("The computer chose\n" + images[computer_number])
    if user_number == 0 and computer_number == 2:
        print("You win")
    elif computer_number == 0 and user_number == 2:
        print("You lose")
    elif computer_number > user_number:
        print("You lose")
    elif user_number > computer_number:
        print("You win")
    elif user_number == computer_number:
        print("It's a draw")