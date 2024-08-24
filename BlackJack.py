import random

print("""⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠉⠀⠀⠀⠀⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡿⠿⠿⠿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠿⠿⠿⢿⣿⣿⣿⣿⣿
⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿
⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿
⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿
⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿
⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠀⠀⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿
⣿⣿⣿⣿⣷⣦⣄⣀⣀⣠⣤⣾⣿⡇⠀⠀⢸⣿⣷⣤⣄⣀⣀⣠⣴⣾⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿""")
print('Welcome to BlackJack!')

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
players = ['CPU']
hand = []
cpu_hand = []
game_over = False
cpu_wins = 0
player_wins = 0
draw = 0


name = input("What is your name?\n")
players.append(name)


## Functions

def deal(deck):
    return random.choice(deck)

def score(current_hand):
    total = 0
    for amount in current_hand:
        total += amount
    return total

def blackjack(player, player_score, player_hand, deck2, dealing):

    options = ['hold', 'deal']

    if player == 'CPU':
        if player_score <= 17:
            turn = random.choice(options)
            if turn == 'hold':
                return 'hold'
            elif turn == 'deal':
                return player_hand.append(dealing(deck2))
        else:
            return 'hold'
    else:
        for i, option in enumerate(options):
            print(f'{i + 1}. {option}')
        ask = str(input('Pick one: ')).lower()
        if ask == '1' or ask == 'hold':
            return 'hold'
        elif ask == '2' or ask == 'deal':
            return player_hand.append(dealing(deck2))


## Starting Cards
hand.append(deal(cards))
hand.append(deal(cards))
cpu_hand.append(deal(cards))
cpu_hand.append(deal(cards))
print(hand)

## Game

while not game_over:

    player_score = score(hand)
    cpu_score = score(cpu_hand)

    choose_player = random.choice(players)

    if player_score > 21:
        print('You have lost the game!')
        game_over = True
    elif cpu_score > 21:
        print(f'{players[0]} has won the game!')
        game_over = True
    elif player_score == cpu_score:
        print('There is a draw!')
        game_over = True

    if not game_over:

        if choose_player == 'CPU' and cpu_score <= 21:
            blackjack('CPU', score(cpu_hand), cpu_hand, cards, deal)
            choose_player = players[1]
            if blackjack('CPU', score(cpu_hand), cpu_hand, cards, deal) == 'hold':
                choose_player = players[1]


        elif choose_player == players[1] and player_score <= 21:
            print(f'Your hand is currently worth: {player_score}')
            blackjack(players[1], score(hand), hand, cards, deal)
            choose_player = players[0]
            if blackjack(players[1], score(hand), hand, cards, deal) == 'hold':
                choose_player = players[1]

        elif blackjack(players[1], score(hand), hand, cards, deal) == 'hold' == 'hold' and blackjack('CPU', score(cpu_hand), cpu_hand, cards, deal) == 'hold':
            game_over = True




    while game_over:

        if player_score > 21:
            cpu_wins += 1
        elif cpu_score > 21:
            player_wins += 1
        elif player_score == cpu_score:
            draw += 1


        print(f'{players[1]} hand: {hand} worth a total of {score(hand)}')
        print(f'{players[0]} hand: {cpu_hand} worth a total of {score(cpu_hand)}')
        print(f'{players[1]} wins: {player_wins}, {players[0]} wins: {cpu_wins}, Draws: {draw}')

        ask_for_replay = str(input('Do you want to play again? (y/n): ')).lower()

        if ask_for_replay == 'y':
            hand.clear()
            cpu_hand.clear()
            hand.append(deal(cards))
            hand.append(deal(cards))
            cpu_hand.append(deal(cards))
            cpu_hand.append(deal(cards))
            game_over = False
        else:
            print('Thanks for playing!')
            break



























































































