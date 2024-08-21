print('''                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________|
                         `'-------'`
                       .-------------.
                      /_______________\ 
                      
                      
                    Subtitlez Auction House         ''''')
bids = {}


def find_better(bidding_directionary):
    winner = ""
    high_bid = 0

    for bidder in bidding_directionary:
        bid_amount = bids[bidder]
        if bid_amount > high_bid:
            high_bid = bid_amount
            winner = bidder

    print(f'The winner is {winner} with a bid of ${high_bid:.2f}')

ask_to_bid = str(input('Press enter to bid '))


while ask_to_bid == "":

    try:
        name = str(input('What is your name? '))
    except ValueError:
        print('Please enter a valid name.')
        name = str(input('What is your name? '))

    try:
        bid_amount = int(input('How much do you wish to bid? '))

    except ValueError:
        print('Please enter a valid number.')
        bid_amount = int(input('How much do you wish to bid? '))

    bids[name] = bid_amount

    try:
        ask_again = str(input('Is there a new Bidder (Y/N)? ')).lower()
        if ask_again == 'y':
            print('\n' * 100)
            try:
                name = str(input('What is your name? '))
            except ValueError:
                print('Please enter a valid name.')
                name = str(input('What is your name? '))

            try:
                bid_amount = int(input('How much do you wish to bid? '))

            except ValueError:
                print('Please enter a valid number.')
                bid_amount = int(input('How much do you wish to bid? '))

            bids[name] = bid_amount
            ask_again = str(input('Is there a new Bidder (Y/N)? ')).lower()
        if ask_again == 'n':
            print('\n' * 100)
            print('Thank you for bidding!')
            find_better(bids)

    except ValueError:
        print('Please enter a string')







