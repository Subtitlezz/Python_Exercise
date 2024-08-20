##### Treasure Island
print("""                            ,--.
                           {    }
                           K,   }
                          /  ~Y`
                     ,   /   /
                    {_'-K.__/
                      `/-.__L._
                      /  ' /`\_}
                     /  ' /
             ____   /  ' /
      ,-'~~~~    ~~/  ' /_
    ,'             ``~~~  ',
   (                        Y
  {                         I
 {      -                    `,
 |       ',                   )
 |        |   ,..__      __. Y
 |    .,_./  Y ' / ^Y   J   )|
 \           |' /   |   |   ||
  \          L_/    . _ (_,.'(
   \,   ,      ^^""' / |      )
     \_  \          /,L]     /
       '-_~-,       ` `   ./`
          `'{_            )
              ^^\..___,.--`) """)



won = 0
lost = 0

ask_to_player = str(input('Would you like to play? (Y/N)\n')).lower()

while ask_to_player == 'y':
    print('Welcome to Treasure Island\nYour mission is to find the treasure.')
    ask_direction = str(input('You\'re at a cross road. Where do you want to go? Left or right?\n')).lower()

    if ask_direction == 'left':
        ask_transport = str(input('You come to a lake. There\'s an island in the middle of the lake. Do you wish to "wait" for a boat or "swim" across?\n')).lower()

        if ask_transport == 'swim':
            print('You have been eaten by a monster')
            lost += 1
            print(f'You have lost: {lost}')
            ask_to_player = str(input('Would you like to play? (Y/N)\n')).lower()


        elif ask_transport == 'wait':
            ask_door_choice = str(input('You arrive at the island. There is 3 doors. One red, one yellow, one blue. Which colour will you choose?\n')).lower()

            if ask_door_choice == 'red':
                print('it\'s a room full of fire, you lose')
                lost += 1
                print(f'You have lost {lost}')
                ask_to_player = str(input('Would you like to play? (Y/N)\n')).lower()
            elif ask_door_choice == 'blue':
                print('You have opened the door, water rushes in and you drown!')
                lost += 1
                print(f'you have lost: {lost}')
                ask_to_player = str(input('Would you like to play? (Y/N)\n')).lower()
            elif ask_door_choice == 'yellow':
                print('YOU HAVE FOUND THE TREASURE! The spoils are yours to keep!')
                won += 1
                print(f'You have won: {won}')
                ask_to_player = str(input('Would you like to play? (Y/N)\n')).lower()
            else:
                print('You have not chosen a valid option, please try again!')
                ask_door_choice = str(input('You arrive at the island. There is 3 doors. One red, one yellow, one blue. Which colour will you choose?\n')).lower()
        else:
           print('You have not selected a valid option. Please Try again.')
           ask_transport = str(input('You come to a lake. There\'s an island in the middle of the lake. Do you wish to "wait" for a boat or "swim" across?\n')).lower()
           
    elif ask_direction == 'right':
        print('You have fallen into a hole! Game Over!')
        lost += 1
        print(f'you have lost: {lost}')
        ask_to_player = str(input('Would you like to play? (Y/N)\n')).lower()
    
    else:
        print('You have not selected a valid option. Please Try again.')
        ask_direction = str(input('You\'re at a cross road. Where do you want to go? Left or right?\n')).lower()

while ask_to_player == 'n':
    print('thank you for playing Treasure Island!')
    print(f'you have won: {won} and lost: {lost}')
    break

else:
    print('Invalid input, please try again.')
    ask_to_player = str(input('Would you like to play? (Y/N)\n')).lower()

            
