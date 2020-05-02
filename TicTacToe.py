
from val import *
from gameState import *


class TicTacToe:
    
    def __init__(self):
       
        self.rows= 3
        self.columns = 3
        self.turn = 0
        self.board = []
        self.__begin()
        self.status = gameState.Ongoing

    def __begin(self):
        for i in range(self.rows*self.columns):
            self.board.append(val.E)

    def __str__(self):
        toReturn = ""
        counter = 0
        for item in self.board:
            if item == val.X:
                toReturn += " X "
            elif item == val.O:
                toReturn += " O "
            elif item == val.E:
                toReturn += "   "
            else: 
                toReturn+= item

            counter+=1

            if (counter%3 == 0) and counter != 1 and counter != len(self.board) :
                toReturn += "\n" + self.columns* "----" + "\n"
            elif counter != len(self.board):
                toReturn += "|"
        
        
        return toReturn
                
                
    def __eq__(self, other):
        if other == None:
            return False
        if self.rows != other.rows or self.columns != other.columns:
            return False

        for i in range(self.rows*self.columns):
            if self.board[i] != other.board[i]:
                return False

        return True

    def getTurn(self):
        return self.turn
    
    def __len__(self):
        return len(self.board)

    def valPlaying(self):
        if (self.turn %2 == 0):
            return val.X
        else:
            return val.O

    def setVal (self, position):
        
        if self.turn%2 == 0:
            toPlay = val.X
        else:
            toPlay = val.O

        self.board[position] = toPlay
        self.turn = self.turn+ 1
        self.wins()


    def getValue(self, position):
        return self.board[position]


##### BUUGGGGGG SOMEWHEREEE
    def wins(self):
        if self.status != gameState.Ongoing:
            return
        

        updated_status = None
        if (self.turn -1)%2 == 0:
            lasttoplay = val.X
            updated_status = gameState.X_win
        else:
            lasttoplay = val.O
            updated_status = gameState.O_win
        

### Check Columns
        
        for column in range(self.columns):
            sequence = 0
            for row in range(self.rows):
                if self.board[self.__indexConverter(self.columns, row, column )]  == lasttoplay:
                    sequence+=1
                else:
                    sequence = 0

                if sequence == 3:
                    self.status = updated_status
                    self.display(column,1)
                    return


## check Rows 
        for row in range(self.rows):
            sequence =  0
            for column in range(self.columns):
                if self.board[self.__indexConverter(self.columns, row,column)]  == lasttoplay:
                    sequence+=1
                else:
                    sequence = 0

                if sequence == 3:
                    self.display(row,0)
                    
                    self.status = updated_status
                    return
                    

        
        # checking 0-4-8 diagonal 
        if (self.board[0]==self.board[4] and self.board[8]== lasttoplay and self.board[0]== self.board[8] ):
            self.status = updated_status
            self.display(0,2)
            return
        

        if (self.board[2]==self.board[4] and self.board[6] == lasttoplay and self.board[2]==self.board[6]):
            self.status = updated_status
            self.display(1,2)

            return

        if self.rows*self.columns == self.turn:
            self.status = gameState.Draw
            return
    
    def reset(self):
        self.board = []
        self.__begin()
        self.status = gameState.Ongoing
        self.turn = 0


    def __indexConverter(self, constant, row, columns):
        """
        (int,int,int) -> int
        return a 1d index from a 2d index 
        constant -- Board Columns
        row -- row number of the index
        columns -- column number of the index

        """
        return (constant * row ) + columns

    def display(self, number ,winType):
        """
        type = [0,1,2] == [row column diagonal]
        """

        if winType == 0:
            for x in range (self.columns):
                self.board[self.__indexConverter(3,number,x)] = "---"
                 
        elif winType == 1:
            for x in range (self.rows):
                self.board[self.__indexConverter(3,x,number)] = " | "
                
        elif winType == 2:
            a= None
            if number == 0:
                a = [0,4,8]
                s= " \\ "
            else:
                a = [2,4,6]
                s = " / "

            for item in a:
                self.board[item] = s 
                


    





