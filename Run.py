import random

from val import *
from TicTacToe import *
from ComputerPlayer import *
from HumanPlayer import *
from myExceptions import * 
from gameState import *

### main

print("Welcome To TicTacToe")
choices ="""
PLEASE MAKE A SELECTION FROM THE LIST BELOW:
1 - PLAY AGAINST A COMPUTER (Enter 1)
2 - PLAY AGAINST A HUMAN (Enter 2)
3 - QUIT (Enter 3)
"""

display = """
The Following Board Displays The Values Of Corresponding Cells 
Simply Enter The Number You Want to Play When It Is Your Turn!
 1 | 2 | 3 
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9
"""
keepGoing = 1
counter =0
askAgain = True
while askAgain == True:
    try:
        user_choice = int(input(choices))
        if user_choice not in [1,2,3]:
            raise InvalidInputError
        askAgain = False
    except ValueError:
        print("Please Enter One of The Follwing Intergers [1,2,3]")
    except InvalidInputError:
        print("The Value must be one of the following [1,2,3]")

    if user_choice == 3:
        exit()

gameBoard = TicTacToe()
player = [None,None]
player_names = ["",""]
name = ["Computer","User"]
print(display)

while keepGoing == 1:

  
    rand = random.randint(0,1)
    
    if user_choice == 1:
        
        if rand == 0:
            player[0] = ComputerPlayer(gameBoard, val.X)
            player[1] = HumanPlayer(gameBoard)
            if counter == 0:
                player_names[0] = "Computer "
                player_names[1] = input("Please Enter Your Name: ")
                name[1] = player_names[1]
            else:
                player_names[0]=name[0]
                player_names[1]=name[1]
            
            print(player_names[0] +" Will Start The Game --")
        else:
            player[1] = ComputerPlayer(gameBoard, val.O)
            player[0] = HumanPlayer(gameBoard)
            if counter == 0:
                player_names[1] = "Computer "
                player_names[0] = input("Please Enter Your Name: ")
            else:
                player_names[1] = name[0]
                player_names[0]= name[1]
            print(player_names[0] +" Will Start The Game --")

    else:
        if counter == 0:
            name[0] = input("Player 1 - Please Enter Your Name: ")
            name[1] = input("Player 2 - Please Enter Your Name: ")
            if rand==0:
                player_names[0]=name[0]
                player_names[1]=name[1]
            else:
                player_names[0]=name[1]
                player_names[1]=name[0]

        else:
            if rand==0:
                player_names[0]=name[0]
                player_names[1]=name[1]
            else:
                player_names[0]=name[1]
                player_names[1]=name[0]


        player=[HumanPlayer(gameBoard),HumanPlayer(gameBoard)]

 
    counter+=1
    while gameBoard.status == gameState.Ongoing:
        print()
        print(gameBoard )
        print()
        
        print(player_names[0] + "'s Turn: ")
        player[0].Play()
        print(gameBoard)
        print()
        if (gameState.Ongoing == gameBoard.status):
            print(player_names[1] + "'s Turn: ")
            player[1].Play()
    
    if (gameBoard.status ==gameState.X_win):
        print ("Congrats " + player_names[0]+ " You Won")
        player[0].wins+=1
        print(gameBoard)
    elif(gameBoard.status == gameState.O_win):
        print("Congrats "+ player_names[1] + " You Won")

        player[1].wins+=1
        print(gameBoard)
    else: 
        print ("It's A Tie")
        print(gameBoard)

    gameBoard.reset()
    askAgain=True
    while askAgain == True:
        try:
            keepGoing = int(input("Do You Want To Play Agin? YES  - Press(1)   NO- Press(2) "))
            if keepGoing not in [1,2]:
                raise InvalidInputError
            askAgain = False
        except ValueError:
            print("Please Enter One of The Follwing Intergers [1,2]")
        except InvalidInputError:
            print("The Value must be one of the following [1,2]")


    


    













