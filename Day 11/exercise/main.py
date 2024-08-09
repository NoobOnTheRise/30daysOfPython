"""
Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun. 
 1. The gun beats the snake, 
 2. the water beats the gun, 
 3. and the snake beats the water.
Write a python program to create a Snake Water Gun game in Python using if-else statements. Do not create any fancy GUI. Use proper functions to check for win.
"""

import random

print("Choices:  0: Snake, 1: Water, 2: Gun")
computer_choice = random.randint(0, 2)

user_choice = int(input("Enter your choice (0,2): "))
print("User's choice :", user_choice)
print("Computer's choice :", computer_choice)


def check_win(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 0
    if user_choice == 1 and computer_choice == 0:
        return -1
    if user_choice == 2 and computer_choice == 1:
        return -1
    if user_choice == 0 and computer_choice == 2:
        return -1
    return 1


score = check_win(user_choice, computer_choice)

if score == 0:
    print("It's a draw")
elif score == -1:
    print("You lose")
else:
    print("You win")
