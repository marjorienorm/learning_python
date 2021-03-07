import random

computer_choice = random.choice(['rock', 'paper', 'scissors'])

user_choice = input('Do you want - rock, paper, or scissors?\n')

winning_message = 'You WIN! The computer choose '
loosing_message = 'You lose, computer wins! The computer choose '

if computer_choice == user_choice:
    print('TIE')
elif user_choice == 'rock' and computer_choice == 'scissors':
    print(winning_message  + computer_choice)
elif user_choice == 'paper' and computer_choice == 'rock':
    print(winning_message  + computer_choice)
elif user_choice == 'scissors' and computer_choice == 'paper':
    print(winning_message + computer_choice)
else:
    print(loosing_message + computer_choice)