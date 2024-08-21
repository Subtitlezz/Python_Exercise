import random
word_list = ["aardvark", "baboon", "camel"]
placeholder = ''

correct_letters = []
game_over = False

chosen_word = random.choice(word_list)
print(chosen_word)
length = len(chosen_word)

for x in range(1, length + 1):
    placeholder += '_'

print(placeholder)

while game_over is not True:
    display = ''
    guess = input("Guess a letter: ").lower()
    lives = 6
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += '_'
    print(display)

    if guess not in chosen_word:
        lives -= 1

    if lives == 0:
        print('you have lost')
        game_over = True
        replay = input('would you like to play again? ')
        if replay.lower() == 'yes':
            game_over = True

    if '_' not in display:
        game_over = True
        print('You have won')
        replay = input('would you like to play again? ')
       
    

                

        
        
        
        
            

            
                

    


