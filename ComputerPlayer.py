import random
from TicTacToe import *
from gameState import *
from val import *
d0 = [0,4,8]
d1 = [2,4,6]

class ComputerPlayer:

    

    def __init__(self, TicTacToe,val):
        self.TicTacToe = TicTacToe
        self.val = val
        self.otherVal = None
        if (self.val == val.X):
            self.otherVal = val.O
        else:
            self.otherVal = val.X
        self.wins = 0

    def Play(self):
        boardInfo =[[],[],[]]
        self.getInfo(boardInfo)
        seq_Two_Win= self.nextMoveCheck(boardInfo, 2,True)
        seq_Two_Lose = self.nextMoveCheck(boardInfo,2,False)
        seq_One_Win = self.nextMoveCheck(boardInfo,1, True)
        seq_One_Lose = self.nextMoveCheck(boardInfo,1,False)
        start_move = self.getStartMove()
        rand = random.randint(1,100)

        if (seq_Two_Win != -1):
            self.TicTacToe.setVal(seq_Two_Win)
        elif (seq_Two_Lose != -1):
            self.TicTacToe.setVal(seq_Two_Lose)
        elif (seq_One_Win != -1):
            self.TicTacToe.setVal(seq_One_Win)
        elif (seq_One_Lose != -1 and rand < 50):
            self.TicTacToe.setVal(seq_One_Lose)
        else:
            self.TicTacToe.setVal(start_move)
            
       
    def nextMoveCheck(self,a,Seq_length,b):
        ## 0,1
        ## 2,3
        ## 4,5
        
        currentRow = 0
        currentColumn = 0 
        currentDiagonal =0
        
        for i in range (0, 6, 2):
            

            if (currentDiagonal<2):
                if (b==True):
                    Condition_to_Check = (a[2][i] == Seq_length and a[2][i+1] == 0)
                elif b== False:
                    Condition_to_Check = (a[2][i] == 0 and a[2][i+1] == Seq_length)

                if Condition_to_Check :
                    return self.playDiagonal(currentDiagonal)
 
            if (b == True):
                Condition_to_Check = (a[0][i] == Seq_length and a[0][i+1] == 0)

            
            elif b== False:
                Condition_to_Check = (a[0][i] == 0 and a[0][i+1] == Seq_length)

           
            if Condition_to_Check:
                return self.playRow(currentRow)
            

            if (b==True):
                Condition_to_Check = (a[1][i] == Seq_length and a[1][i+1] == 0)

            elif b== False:

                Condition_to_Check = (a[1][i] == 0 and a[1][i+1] == Seq_length)


            if Condition_to_Check:
                return self.playColumn(currentColumn)

            

            currentColumn+=1
            currentRow+=1
            currentDiagonal+=1
    
        return -1

    def getStartMove(self):
        a = [4,0,8,6,2,7,1,3]
        for a0 in a:
            if self.TicTacToe.board[a0] == val.E:
                return a0
 

    def getInfo(self, a):

        for i in range (3):
            ### getting row info and putting it in sub_list 0
            a[0].append(self.elemsInRow(i,self.val))
            a[0].append(self.elemsInRow(i,self.otherVal))

            ### getting columns info and putting it in sub_list 1
            a[1].append(self.elemsInColumns(i,self.val))
            a[1].append(self.elemsInColumns(i, self.otherVal))

            if (i<2):
                a[2].append(self.elemsInDiagonal(i,self.val))
                a[2].append(self.elemsInDiagonal(i,self.otherVal))

        
    def elemsInRow(self,row,val):
        toReturn =0
        for x in range (3):
            if (self.TicTacToe.board[self.__indexConverter(3,row,x)] == val):
                toReturn+=1
        return toReturn
    
    def elemsInColumns(self, column,val):
        toReturn =0
        for x in range (3):
            if (self.TicTacToe.board[self.__indexConverter(3,x,column)] == val):
                toReturn+=1
        return toReturn

    def elemsInDiagonal(self,diagonal,val):
        toReturn = 0

        if diagonal == 0:
            a = d0
        else:
            a= d1

        for item in a:
            if (self.TicTacToe.board[item] == val):
                toReturn+=1
        return toReturn
        
        



    
        

    def playRow(self,row):
        toReturn = -1
        for y in range (3):
            index = self.__indexConverter(3,row,y)
            if self.TicTacToe.getValue(index) == val.E:
                return index
                #toReturn = index
        return toReturn

    def playColumn(self,column):
        toReturn = -1
        for x in range (3):
            index = self.__indexConverter(3,x,column)
            if self.TicTacToe.getValue(index) == val.E:
                return index
                #toReturn = index
        return toReturn

    def playDiagonal(self,diagonal):
        a=[]
        if diagonal == 0:
            a=d0
        else:
            a= d1


        for i in a:
            if (self.TicTacToe.getValue(i) == val.E):
                return i
                #toReturn = i
        return toReturn
    

    
    def __indexConverter(self , constant, row, columns):
        """
        (int,int,int) -> int
        return a 1d index from a 2d index 
        constant -- Board Columns
        row -- row number of the index
        columns -- column number of the index

        """
        return (constant * row ) + columns







    



