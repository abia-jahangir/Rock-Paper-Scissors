import random

user_count = 0
computer_count = 0
round_count = 1
user = None

def play(round_count):
    global user_count
    global computer_count
    print('\n')
    print('-' * 10)
    print("Round:", round_count)
    user = input("'r' for rock, 'p' for paper, 's' for scissors, 'q' to quit. ")
    computer = random.choice(['r', 'p', 's'])

    if (user == 'r') or (user == 'p') or (user == 's'):
        print('\nhmm... I chose...', computer)

        if user == computer:
            print("\nTie! Let's try again!")

        elif ((user == 'r') and (computer == 'p')) or ((user == 'p') and (computer == 's') or ((user == 's') and (computer == 'r'))):
            computer_count += 1
            print("\nI win! Lets play again")
        elif ((user == 'p') and (computer == 'r')) or ((user == 's') and (computer == 'p') or ((user == 'r') and (computer == 's'))):
            user_count += 1
            print("\nYou win! I'll get it next time!")
        
        print("\nYour wins:", user_count)
        print("My wins: ", computer_count)

    elif (user == 'q'):
        print("\nLets play again soon!")
        exit()

    else:
        print('\nPlease input a valid option.')

while user != 'q':
    play(round_count)
    round_count += 1