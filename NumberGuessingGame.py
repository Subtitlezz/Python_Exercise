import random
number = random.randint(1, 100)
difficulties = ['easy', 'hard']
game_over = False
counter = 0

def score(answer, num):

    if answer == num:
        return True
    else:
        return False

ask_diff = str(input("What difficulty would you like to play on (Easy/Hard)?: ")).lower()

if ask_diff in difficulties:
    print(f'You have selected {ask_diff}')
else:
    print("A difficulty like that doesn\'t exist")
    ask_diff = str(input("What difficulty would you like to play on (Easy/Hard)?: ")).lower()

while not game_over:

    if ask_diff == 'easy':
        print(number)


        ask = int(input('Guess a number between 1 and 100: '))
        result = score(ask, number)

        if result is True:
            print('Nice!')
            game_over = True
        elif result is False:
            counter += 1
            print('Incorrect')
            print(counter)
        if counter == 10:
            print('You have reached the end of the game')
            game_over = True

    elif ask_diff == 'hard':

        ask = int(input('Guess a number between 1 and 100: '))
        result = score(ask, number)

        if result is True:
            print('Nice!')
            game_over = True
        elif result is False:
            print('Incorrect')
            counter += 1
        if counter == 5:
            print('You have reached the end of the game')
            game_over = True



    while game_over:

        if score(ask, number) is True:
            print('Congratulations, you have won the game!')
            break
        else:
            print('You have lost.')
            break




























