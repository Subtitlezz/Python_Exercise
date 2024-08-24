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

    options = ['Hold', 'Deal']

    if player == 'CPU':
        if player_score <= 17:
            turn = random.choice(options)
            if turn == 'Hold':
                return 'Hold'
            elif turn == 'Deal':
                return player_hand.append(dealing(deck2))
    else:
        for i, option in enumerate(options):
            print(f'{i + 1}. {option}')
        ask = str(input('Pick one: ')).lower()
        if ask == '2' or 'deal':
            return player_hand.append(dealing(deck2))
        else:
            return 'Hold'


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


    if choose_player == 'CPU':
        blackjack('CPU', score(cpu_hand), cpu_hand, cards, deal)
        choose_player = players[1]

    elif choose_player == players[1]:
        print(f'Your hand is currently worth: {player_score}')
        blackjack(players[1], score(hand), hand, cards, deal)
        choose_player = players[0]


    if player_score > 21:
        print('You have lost the game!')
        game_over = True
    elif cpu_score > 21:
        print(f'{players[0]} has won the game!')
        game_over = True

    while game_over:

        print(f'{players[1]} hand: {hand} worth a total of {score(hand)}')
        print(f'{players[0]} hand: {cpu_hand} worth a total of {score(cpu_hand)}')
        break



























































































