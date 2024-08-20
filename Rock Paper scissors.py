##### Rock Paper scissors
import random

players = ['Player', 'CPU']
game = [1, 2, 3]

players[0]

rock_paper_question = int(input('Please Type 1 for Rock, 2 for Paper, 3 for Scissors.\n'))

if rock_paper_question == game[0]:
    print(""" _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\ """)
    print('You have selected Rock!')
    players[1]
elif rock_paper_question == game[1]:
    print("""_ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|      """)
    print('You have Selected Paper!')
    players[1]
elif rock_paper_question == game[2]:
    print(""" _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\. """)
    print('You have selected Scissors!')
    players[1]
else:
    print('You have selected an incorrect value!')

while players[1]:
   choice = random.choice(game)
   if choice == game[0]:
        print(""" _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\ """)
        print('CPU has selected Rock!')
        break
   elif choice == game[1]:
       print("""_ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|      """)
       print('CPU has selected Paper!')
       break
   else:
       print(""" _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\. """)
       print('CPU has selected Scissors!')
       break

if rock_paper_question == choice:
    print('Tie!')
elif rock_paper_question == game[0] and choice == game[2]:
    print('Rock Beats Scissors! Player Wins!')
elif rock_paper_question == game[1] and choice == game[0]:
    print('Paper Beats Rock! Player Wins!')
elif rock_paper_question == game[2] and choice == game[1]:
    print('Scissors Beats Paper! Player Wins!')
elif choice == game[0] and rock_paper_question == game[2]:
    print('Rock Beats Scissors! CPU Wins!')
elif choice == game[1] and rock_paper_question == game[0]:
    print('Paper Beats Rock! CPU Wins!')
else:
    print('Scissors Beats Paper! CPU Wins!')



        



