# Problem Statement
#
# The game of BombSweeper is a single-player game played on a rectangular grid. Each square in the grid is either a bomb (represented by 'B') or empty space (represented by '.'). The true identity of each square is hidden when the game begins. The object of the game is to correctly determine both the number of bombs on the board and their positions.
# You are trying to write a program which predicts the percent likelihood that you will win a given game of BombSweeper. You've recently become so good at the game that your success or failure depends only on your first few moves. To start, you pick a random square on the gameboard and uncover it. If the square you uncover is a bomb, you lose the game. If the square is not a bomb, but one or more of its horizontal, vertical, and diagonal neighbors is, you are no better off than when you started and you must take another turn. If the square is not a bomb, and none of its (up to) eight neighbors are bombs either, then you win the game.
# Given a tuple (string) board, representing the game board, return a number between 0.0 and 100.0, inclusive, representing the percent likelihood of you winning the game.
# Definition
#
# Class:
# BombSweeper
# Method:
# winPercentage
# Parameters:
# tuple (string)
# Returns:
# float
# Method signature:
# def winPercentage(self, board):


#Gendo90 has submitted the 600-point problem for 271.24 points
#Successful on first try! Probably would have gotten more points but had
#issues with the applet (internet was not working)
class BombSweeper(object):
    def checkNeighbors(self, i, j, board):
        width = len(board[0])
        height = len(board)
        test = []
        if(j-1>=0):
            lower_left = j-1
        else:
            lower_left = j
        if(j+1<width):
            upper_left = j+1
        else:
            upper_left = j
        if(i-1>=0):
            lower_right = i-1
        else:
            lower_right = i
        if(i+1<height):
            upper_right = i+1
        else:
            upper_right = i

        test = [a for i in board[lower_right:upper_right+1] for a in i[lower_left:upper_left+1]]
        # print(i, j)
        # print(test)
        if("B" in test):
            return False
        else:
            return True


    def winPercentage(self, board):
        num_bombs = sum([a.count("B") for a in board])
        num_wins = 0
        for i, row in enumerate(board):
            for j, letter in enumerate(row):
                if(letter=="." and self.checkNeighbors(i, j, board)):
                    num_wins+=1
        output = num_wins*100.0/(num_wins+num_bombs)
        output = round(output, 9)

        print(num_wins)
        return output



test = BombSweeper()

print(test.winPercentage(("BBBBB",
 "B...B",
 "B...B",
 "B...B",
 "BBBBB")))
