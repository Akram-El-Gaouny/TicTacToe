from myExceptions import * 
from TicTacToe import *
class HumanPlayer():
    def __init__(self, TicTacToe):
        self.wins = 0
        self.TicTacToe = TicTacToe
    def Play(self):
        stop = False
        while stop == False:
            try:
                x = int(input("What is your next move? \n(0) - help, (100) - Exit\n"))
                if (x == 100):
                    exit()

                if (x == 0):
                    raise HelpError
                x= x-1 ### ensures to match the index of the board
                if x<0 or x >= len(self.TicTacToe):
                    raise InvalidInputError
                if self.TicTacToe.getValue(x) != val.E:
                    raise CellNotEmptyError
                stop = True
            except ValueError:
                print("Please Enter an Integer")
            except CellNotEmptyError:
                print("The cell you have chosen is full")
            except InvalidInputError:
                print("The value you picked is an invalid input")
            except HelpError:
                x = HelpError()
                print(x)

        self.TicTacToe.setVal(x)



        

