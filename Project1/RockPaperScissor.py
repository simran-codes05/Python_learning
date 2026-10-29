# Rock wins against Scissor  	Rock = 0
# Paper wins against Rock     	Paper = 1
# Scissor wins againts Paper 	Scissor = 2

# U  C
# 0  0 T
# 0  1 C
# 0  2 U
# 1  0 U
# 1  1 T
# 1  2 C
# 2  0 C
# 2  1 U
# 2  2 T

import random

want_to_play = True

while want_to_play:
    user_choice = int(input("\nEnter your choice 0 = Rock , 1 = Paper , 2 = Scissor : "))

    if user_choice >= 3 or user_choice < 0 :  #If user choice is greater than number 3 or equal to 3 and less than 0 2, just print wrong move
        print("Invalid move , you loose")
        
    else: 
        computer_choice = random.randrange(0 , 3)
        print(f"Computer choice : {computer_choice}")

        if user_choice == computer_choice :
            print("Tie")
            
        elif computer_choice == 0 and user_choice == 2:
            print("You loose!")

        elif user_choice == 0 and computer_choice == 2:
            print("You win!")

        elif computer_choice > user_choice :
            print("You loose!")
            
        elif user_choice > computer_choice :
            print("You Win!")
        
    want_to_continue = input("\nEnter 'y' to continue or 'n' to stop : ").lower()
    
    if want_to_continue == 'y':
        want_to_play = True
    elif want_to_continue == 'n':
        want_to_play = False
        print("Bye!")
    else:
        print("Invalid input. Game stopped.")
        want_to_play = False


