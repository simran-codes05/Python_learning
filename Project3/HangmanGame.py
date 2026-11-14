# first player     second player
#apple				-----   (in limited attempts you need to idendentify

# if second plyer not identify 1st player draw the hangman 1 by 1
#if the hang man complete 2nd loose or word is complete 1st loose

#------------
#		|
#		O
#	   /|\
#	   / \


import random
import stages_file

print("Let's play Hangman Game!\n")
#lists of fruits
fruits = ["apple","banana","Mango","Blueberry","strawberry","cherry", "kivi",
         "Avacado", "dragan fruit", "carrot", "beetroot", "Grapes" , "watermelon", "jackfruit","Orange","Guava"]
lives = 6

#Generate a word
fruit = random.choice(fruits).lower()
#print(f"The fruit word is {fruit}")

display = []

#Generate spaces for word
for f in range(len(fruit)):
    display += '_'
print(display)

#guess a letter

game_over = False
while not game_over:
    print(f"You have {lives} lives")
    guess_letter = input("Enter a letter to guess : ").lower()
    for position in range(len(fruit)):
        letter = fruit[position]
        
        if letter == guess_letter:
            display[position] = guess_letter
    print(display)
    
    if guess_letter not in fruit:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose!")
            print(f"The word was {fruit}")
    
    if '_' not in display:
        game_over = True
        print("You win!")
    print(stages_file.stages[lives])
    

