#Bajram Metjahic
#bmetjahi

import string

class game(object):
    #game class is bookkeeping.. initializes board and some other variables
    def __init__(self):
        #init fxn
        
        self.player = 1
        #starts as player 1 (white)
        
        #initializing board:
        
        self.board = [[None for i in range(8)] for i in range(8)]
        
        self.board[0] = [space(rook(self),0,'blackrook1.gif'),
                        space(knight(self),0,"blackknight1.gif"),
                        space(bishop(self),0,"blackbishop1.gif"),
                        space(queen(self),0,"blackqueen.gif"),
                        space(king(self),0,"blackking.gif"),
                        space(bishop(self),0,"blackbishop2.gif"),
                        space(knight(self),0,"blackknight2.gif"),
                        space(rook(self),0,"blackrook2.gif")]
        
        self.board[1] = [space(pawn(self),0,"blackpawn1.gif"),
                         space(pawn(self),0,"blackpawn2.gif"),
                         space(pawn(self),0,"blackpawn3.gif"),
                         space(pawn(self),0,"blackpawn4.gif"),
                         space(pawn(self),0,"blackpawn5.gif"),
                         space(pawn(self),0,"blackpawn6.gif"),
                         space(pawn(self),0,"blackpawn7.gif"),
                         space(pawn(self),0,"blackpawn8.gif")  ]
        
        
        
        self.board[6] = [space(pawn(self),1,"whitepawn1.gif"),
                         space(pawn(self),1,"whitepawn2.gif"),
                         space(pawn(self),1,"whitepawn3.gif"),
                         space(pawn(self),1,"whitepawn4.gif"),
                         space(pawn(self),1,"whitepawn5.gif"),
                         space(pawn(self),1,"whitepawn6.gif"),
                         space(pawn(self),1,"whitepawn7.gif"),
                         space(pawn(self),1,"whitepawn8.gif")  ]
        
        self.board[7] = [space(rook(self),1,"whiterook1.gif"),
                        space(knight(self),1,"whiteknight1.gif"),
                        space(bishop(self),1,"whitebishop1.gif"),
                        space(queen(self),1,"whitequeen.gif"),
                        space(king(self),1,"whiteking.gif"), 
                        space(bishop(self),1,"whitebishop2.gif"), 
                        space(knight(self),1,"whiteknight2.gif"),
                        space(rook(self),1,"whiterook2.gif")]
        
        

        #for incorrect moves:
        self.tryAgain = False
        
        #changes to True when game conceded:
        self.player0Concede = False
        self.player1Concede = False
        

def freePath(game, searchingCheck = False):
    #returns if there is a free path from current position to newRow,newCol for selected piece
    
    #ensures pieces cannot improperly hop over one another
                
        if searchingCheck: 
            if game.player == 0:
                game.player = 1
            else:
                game.player = 0
   
        
        #right:
        
        #checking every place on board to right of game.oldCol
        
        if game.newCol > game.oldCol and game.newRow == game.oldRow:
            midRow = game.oldRow
            midCol = game.oldCol+1
            
            while game.newCol >= midCol:
                
                if game.newCol == midCol:
                    if game.board[midRow][midCol] == None:
                        #return True if land on None
                        return True
                    elif type(game.board[midRow][midCol]) == space and game.board[midRow][midCol].player != game.player:
                        #return True if land on opposing piece
                        return True
                    else: #it's one of your own pieces
                    
                       
                        return False
                        
                if game.board[midRow][midCol] != None and (game.oldRow,game.oldCol) != (midRow,midCol):
                    #if you hit ANY piece in the middle, return False
                 
                    return False
                    
                midCol += 1
                #midCol changes w/ each iteration of loop
        
            
        #left:
        elif game.newCol < game.oldCol and game.newRow == game.oldRow:
            midRow = game.oldRow
            midCol = game.oldCol
            
            while game.newCol <= midCol:
                
                if game.newCol == midCol:
                    if game.board[midRow][midCol] == None:
                        #return True if land on None
                        return True
                    elif type(game.board[midRow][midCol]) == space and game.board[midRow][midCol].player != game.player:
                        #return True if land on opposing piece
                        return True
                    else: #it's one of ur own pieces
                        return False
                
                if game.board[midRow][midCol] != None and (game.oldRow,game.oldCol) != (midRow,midCol):
                    #hit another piece before endpoint
                    return False
                
                midCol -= 1
            
        #up:    
        
        
        elif game.newRow < game.oldRow and game.newCol == game.oldCol:
            midRow = game.oldRow
            midCol = game.oldCol
            
            while game.newRow <= midRow:
                
                if game.newRow == midRow:
                    if game.board[midRow][midCol] == None:
                        #return True if land on None
                        return True
                    elif type(game.board[midRow][midCol]) == space and game.board[midRow][midCol].player != game.player:
                        #return True if land on opposing piece
                        return True
                    else: #it's one of your own pieces
                        return False
                        
                if game.board[midRow][midCol] != None and (game.oldRow,game.oldCol) != (midRow,midCol):
                    #hit piece in between
                    return False
                    
                midRow -= 1
                
                
        #down:    
        
        elif game.newRow > game.oldRow and game.newCol == game.oldCol:

            midRow = game.oldRow
            midCol = game.oldCol

            while game.newRow >= midRow:
                
                if game.newRow == midRow:
                    if game.board[midRow][midCol] == None:
                        #return True if land on None
                        return True
                    elif type(game.board[midRow][midCol]) == space and game.board[midRow][midCol].player != game.player:
                        #return True if land on opposing piece
                        return True
                    else: #it's one of your own pieces
                        return False
                        
                if game.board[midRow][midCol] != None and (game.oldRow,game.oldCol) != (midRow,midCol):

                    return False
                    
                midRow += 1
                
        #up-left:
        
        elif game.newRow < game.oldRow and game.newCol < game.oldCol:
            midRow = game.oldRow
            midCol = game.oldCol
            print(game.newRow,game.newCol)
            print(game.oldRow,game.oldCol)
            
            while game.newRow <= midRow and game.newCol <= midCol:
                
                if game.newRow == midRow and game.newCol == midCol:
                    if game.board[midRow][midCol] == None:
                        #return True if land on None
                        return True
                    elif type(game.board[midRow][midCol]) == space and game.board[midRow][midCol].player != game.player:
                        #return True if land on opposing piece
                        return True
                    else: #it's one of your own pieces
                        return False
                        
                if game.board[midRow][midCol] != None and (game.oldRow,game.oldCol) != (midRow,midCol):
                    return False
                    
                midRow -= 1
                midCol -= 1
                #move both left and up
            
        #up-right:
        
        elif game.newCol > game.oldCol and game.newRow < game.oldRow:
            midRow = game.oldRow
            midCol = game.oldCol
            
            while game.newRow <= midRow and game.newCol >= midCol:
                
                if game.newRow == midRow and game.newCol == midCol:
                    
                    if game.board[midRow][midCol] == None:
                        #return True if land on None
                        return True
                    elif type(game.board[midRow][midCol]) == space and game.board[midRow][midCol].player != game.player:
                        #return True if land on opposing piece
                        return True
                    else: #it's one of your own pieces
                        return False
                        
                if game.board[midRow][midCol] != None and (game.oldRow,game.oldCol) != (midRow,midCol):
                    #bumped into a piece before the end
                    return False
                    
                midRow -= 1
                midCol += 1
            
        #down-left:
        elif game.newCol < game.oldCol and game.newRow > game.oldRow:
            midRow = game.oldRow
            midCol = game.oldCol
            
            
            while game.newRow >= midRow and game.newCol <= midCol:
                
                if game.newRow == midRow and game.newCol == midCol:
                    
                    if game.board[midRow][midCol] == None:
                        #return True if land on None
                        return True
                    elif type(game.board[midRow][midCol]) == space and game.board[midRow][midCol].player != game.player:
                        #return True if land on opposing piece
                        return True
                    else: #it's one of your own pieces
                        return False
                        
                if game.board[midRow][midCol] != None and (game.oldRow,game.oldCol) != (midRow,midCol):
                    #hit a piece
                    return False
                    
                midRow += 1
                midCol -= 1
                
                
            
        #down-right:
        elif game.newCol > game.oldCol and game.newRow > game.oldRow:
            midRow = game.oldRow
            midCol = game.oldCol
            
            while game.newRow >= midRow and game.newCol >= midCol:
                
                if game.newRow == midRow and game.newCol == midCol:
                    
                    if game.board[midRow][midCol] == None:
                        #return True if land on None
                        return True
                    elif type(game.board[midRow][midCol]) == space and game.board[midRow][midCol].player != game.player:
                        #return True if land on opposing piece
                        return True
                    else: #it's one of your own pieces
                        return False
                        
                if game.board[midRow][midCol] != None and (game.oldRow,game.oldCol) != (midRow,midCol):
                    return False
                
                midRow += 1
                midCol += 1
            
            
        
        #if it doesn't fit any of these parameters:
        
        return False
            
 

def inCheck(game):
    #sees if any of opposing team's pieces have legal and free path to your king, which is check
    
    #store old values of game.oldRow,game.oldCol,game.newRow,game.newCol
    #so we can switch back to these values later
    oldestRow = game.oldRow
    oldestCol = game.oldCol
    newestRow = game.newRow
    newestCol = game.newCol
    
    #locating current player's king:
    yungKing = tuple()
    for row in range(len(game.board)):
        for col in range(len(game.board[0])):
            if type(game.board[row][col]) == space:
                if game.board[row][col].piece.__repr__() == 'king' and game.board[row][col].player == game.player:
                    yungKing = (row,col)
                    #current player's king in check 

    
    #locating opposing team pieces:
    for row in range(len(game.board)):
        for col in range(len(game.board[0])):
            if type(game.board[row][col]) == space:
                #seeing if any of other teams players can legally get current team king
                if game.board[row][col].player != game.board[yungKing[0]][yungKing[1]].player:
#changing game.newRow and game.newCol,for the opposing team pieces, so it knows what to check in isLegalMove fxn
#isLegalMove and freePath, only take game, so it must take row and col in this form

                    game.oldRow = row
                    game.oldCol = col
                    game.newRow = yungKing[0]
                    game.newCol = yungKing[1]


                    if (game.board[row][col].piece.isLegalMove(game) and freePath(game, True) and game.board[row][col].piece != knight):
                        #can legally move from the aforementioned space on board to your king
                        
                        #set values back
                        game.oldRow = oldestRow
                        game.oldCol = oldestCol
                        game.newRow = newestRow
                        game.newCol = newestCol
                        
                        #set player to player of king
                        game.player = game.board[yungKing[0]][yungKing[1]].player
                            

                        return True
                        
                       
                    elif (game.board[row][col].piece.__repr__() == 'knight' and game.board[row][col].piece.isLegalMove(game)):
                        #checking separately for knight (don't use freePath fxn)
                        
                        game.oldRow = oldestRow
                        game.oldCol = oldestCol
                        game.newRow = newestRow
                        game.newCol = newestCol
                        
                        game.player = game.board[yungKing[0]][yungKing[1]].player
                        
                        return True
                    
                        
                        
                   
    #set player back if no check
    game.player = game.board[yungKing[0]][yungKing[1]].player
    
    #set rows and cols back if no check
    game.oldRow = oldestRow
    game.oldCol = oldestCol
    game.newRow = newestRow
    game.newCol = newestCol
    
    #return False if no check
    return False


class space(object):
    #space class holds the type of piece, player who owns it, and filename of its picture
    def __init__(self,pieceType,playerNum,pic):
        self.piece = pieceType
        self.player = playerNum
        self.pic = pic
        
    
    def __repr__(self):
        return 'piece'

class piece(object):
    #piece class holds subclasses of different piece types and their methods as well as location attributes
    def __init__(self,game):
        #location attributes
        self.oldRow = game.oldRow
        self.oldCol = game.oldCol 
        
        
    def move(self,game):
        #moves the piece

        if game.board[game.oldRow][game.oldCol].piece.__repr__() == 'knight':
            #knight moves separately from other pieces as does not use freePath fxn

            if self.isLegalMove(game) and game.board[game.oldRow][game.oldCol].player == game.player:

        
        #check before pieces actually move:
                if type(game.board[game.newRow][game.newCol]) == space:
                    #if it is space class(not None, which means no piece there)
                    if game.board[game.newRow][game.newCol].pic == 'blackrook1.gif':
                        #if knight moves onto blackrook1, don't draw its picture on board anymore
                        game.drawBR = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'blackknight1.gif':
                        game.drawBkn = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'blackbishop1.gif':
                        game.drawBB = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'blackqueen.gif':
                        game.drawBQ = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'blackking.gif':
                        game.drawBK = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'blackbishop2.gif':
                        game.drawBB2 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'blackknight2.gif':
                        game.drawBKn2 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'blackrook2.gif':
                        game.drawBR2 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'blackpawn1.gif':
                        game.drawBP1 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'blackpawn2.gif':
                        game.drawBP2 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'blackpawn3.gif':
                        game.drawBP3 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'blackpawn4.gif':
                        game.drawBP4 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'blackpawn5.gif':
                        game.drawBP5 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'blackpawn6.gif':
                        game.drawBP6 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'blackpawn7.gif':
                        game.drawBP7 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'blackpawn8.gif':
                        game.drawBP8 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'whiterook1.gif':
                        game.drawWR = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'whiteknight1.gif':
                        game.drawWKn = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'whitebishop1.gif':
                        game.drawWB = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'whitequeen.gif':
                        game.drawWQ = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'whiteking.gif':
                        game.drawWK = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'whitebishop2.gif':
                        game.drawWB2 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'whiteknight2.gif':
                        game.drawWk2 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'whiterook2.gif':
                        game.drawWR2 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'whitepawn1.gif':
                        game.drawWP1 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'whitepawn2.gif':
                        game.drawWP2 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'whitepawn3.gif':
                        game.drawWP3 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'whitepawn4.gif':
                        game.drawWP4 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'whitepawn5.gif':
                        game.drawWP5 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'whitepawn6.gif':
                        game.drawWP6 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'whitepawn7.gif':
                        game.drawWP7 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'whitepawn8.gif':
                        game.drawWP8 = False



                
                #making move and deleting where the piece used to be:
                temp = game.board[game.newRow][game.newCol]
                
                game.board[game.newRow][game.newCol] = game.board[game.oldRow][game.oldCol]
                game.board[game.oldRow][game.oldCol] = None
                
                #Useful for having a visual in console of how pieces are moving:
                for c in game.board:
                    print(c)

                #putting yourself in check and being put in check handled the same
    
                
                if inCheck(game):
                    #checking if move puts you/keeps you in check, if so, undo move
                    game.board[game.oldRow][game.oldCol] = game.board[game.newRow][game.newCol]
                    game.board[game.newRow][game.newCol] = temp
                    #warning appears
                    game.tryAgain = True
                    #player doesn't change
                    
 
                
                #change player at end of a move if not in check
                else:
                    if game.player == 0:
                        game.player = 1
                    else:
                        game.player = 0
                    
            else:
                #improper move - player doesn't change
                game.tryAgain = True
                
        
        
        
        elif self.isLegalMove(game) and freePath(game) and game.board[game.oldRow][game.oldCol].player == game.player:
            #for all non-knight, non-pawn pieces
            #checking if move is legal, path is free, and if correct player is making move (above)
                
                
            if type(game.board[game.newRow][game.newCol]) == space:
                if game.board[game.newRow][game.newCol].pic == 'blackrook1.gif':
                    #same as in knight move method
                    game.drawBR = False
                    
            if type(game.board[game.newRow][game.newCol]) == space:
                if game.board[game.newRow][game.newCol].pic == 'blackknight1.gif':
                    game.drawBkn = False
                    
            if type(game.board[game.newRow][game.newCol]) == space:
                if game.board[game.newRow][game.newCol].pic == 'blackbishop1.gif':
                    game.drawBB = False
                    
            if type(game.board[game.newRow][game.newCol]) == space:
                if game.board[game.newRow][game.newCol].pic == 'blackqueen.gif':
                    game.drawBQ = False
                    
            if type(game.board[game.newRow][game.newCol]) == space:
                if game.board[game.newRow][game.newCol].pic == 'blackking.gif':
                    game.drawBK = False
                    
            if type(game.board[game.newRow][game.newCol]) == space:
                if game.board[game.newRow][game.newCol].pic == 'blackbishop2.gif':
                    game.drawBB2 = False
                    
            if type(game.board[game.newRow][game.newCol]) == space:
                if game.board[game.newRow][game.newCol].pic == 'blackknight2.gif':
                    game.drawBKn2 = False
                    
            if type(game.board[game.newRow][game.newCol]) == space:
                if game.board[game.newRow][game.newCol].pic == 'blackrook2.gif':
                    game.drawBR2 = False
                    
            if type(game.board[game.newRow][game.newCol]) == space:
                if game.board[game.newRow][game.newCol].pic == 'blackpawn1.gif':
                    game.drawBP1 = False
                    
            if type(game.board[game.newRow][game.newCol]) == space:
                if game.board[game.newRow][game.newCol].pic == 'blackpawn2.gif':
                    game.drawBP2 = False
                    
            if type(game.board[game.newRow][game.newCol]) == space:
                if game.board[game.newRow][game.newCol].pic == 'blackpawn3.gif':
                    game.drawBP3 = False
                    
            if type(game.board[game.newRow][game.newCol]) == space:
                if game.board[game.newRow][game.newCol].pic == 'blackpawn4.gif':
                    game.drawBP4 = False
                    
            if type(game.board[game.newRow][game.newCol]) == space:
                if game.board[game.newRow][game.newCol].pic == 'blackpawn5.gif':
                    game.drawBP5 = False
                    
            if type(game.board[game.newRow][game.newCol]) == space:
                if game.board[game.newRow][game.newCol].pic == 'blackpawn6.gif':
                    game.drawBP6 = False
                    
            if type(game.board[game.newRow][game.newCol]) == space:
                if game.board[game.newRow][game.newCol].pic == 'blackpawn7.gif':
                    game.drawBP7 = False
                    
            if type(game.board[game.newRow][game.newCol]) == space:
                if game.board[game.newRow][game.newCol].pic == 'blackpawn8.gif':
                    game.drawBP8 = False
                    
            if type(game.board[game.newRow][game.newCol]) == space:
                if game.board[game.newRow][game.newCol].pic == 'whiterook1.gif':
                    game.drawWR = False
                    
            if type(game.board[game.newRow][game.newCol]) == space:
                if game.board[game.newRow][game.newCol].pic == 'whiteknight1.gif':
                    game.drawWKn = False
                    
            if type(game.board[game.newRow][game.newCol]) == space:
                if game.board[game.newRow][game.newCol].pic == 'whitebishop1.gif':
                    game.drawWB = False
                    
            if type(game.board[game.newRow][game.newCol]) == space:
                if game.board[game.newRow][game.newCol].pic == 'whitequeen.gif':
                    game.drawWQ = False
                    
            if type(game.board[game.newRow][game.newCol]) == space:
                if game.board[game.newRow][game.newCol].pic == 'whiteking.gif':
                    game.drawWK = False
                    
            if type(game.board[game.newRow][game.newCol]) == space:
                if game.board[game.newRow][game.newCol].pic == 'whitebishop2.gif':
                    game.drawWB2 = False
                    
            if type(game.board[game.newRow][game.newCol]) == space:
                if game.board[game.newRow][game.newCol].pic == 'whiteknight2.gif':
                    game.drawWk2 = False
                    
            if type(game.board[game.newRow][game.newCol]) == space:
                if game.board[game.newRow][game.newCol].pic == 'whiterook2.gif':
                    game.drawWR2 = False
                    
            if type(game.board[game.newRow][game.newCol]) == space:
                if game.board[game.newRow][game.newCol].pic == 'whitepawn1.gif':
                    game.drawWP1 = False
                    
            if type(game.board[game.newRow][game.newCol]) == space:
                if game.board[game.newRow][game.newCol].pic == 'whitepawn2.gif':
                    game.drawWP2 = False
                    
            if type(game.board[game.newRow][game.newCol]) == space:
                if game.board[game.newRow][game.newCol].pic == 'whitepawn3.gif':
                    game.drawWP3 = False
                    
            if type(game.board[game.newRow][game.newCol]) == space:
                if game.board[game.newRow][game.newCol].pic == 'whitepawn4.gif':
                    game.drawWP4 = False
                    
            if type(game.board[game.newRow][game.newCol]) == space:
                if game.board[game.newRow][game.newCol].pic == 'whitepawn5.gif':
                    game.drawWP5 = False
                    
            if type(game.board[game.newRow][game.newCol]) == space:
                if game.board[game.newRow][game.newCol].pic == 'whitepawn6.gif':
                    game.drawWP6 = False
                    
            if type(game.board[game.newRow][game.newCol]) == space:
                if game.board[game.newRow][game.newCol].pic == 'whitepawn7.gif':
                    game.drawWP7 = False
                    
            if type(game.board[game.newRow][game.newCol]) == space:
                if game.board[game.newRow][game.newCol].pic == 'whitepawn8.gif':
                    game.drawWP8 = False

            
            #making move and deleting where the piece used to be:
          
            
            temp = game.board[game.newRow][game.newCol]
            
            game.board[game.newRow][game.newCol] = game.board[game.oldRow][game.oldCol]
            game.board[game.oldRow][game.oldCol] = None
            
            #useful for visualization in console:
            for c in game.board:
                print(c)
            
            #checking if in check, as in knight move method
            if inCheck(game):
                game.board[game.oldRow][game.oldCol] = game.board[game.newRow][game.newCol]
                game.board[game.newRow][game.newCol] = temp
                game.tryAgain = True
                
            
            #change player at end of a proper move
            else:
                if game.player == 0:
                    game.player = 1
                else: 
                    game.player = 0
                
        else:
            game.tryAgain = True
            #warning... and player does not change for illegal move
                


class pawn(piece):
    #pawn class
                
    def __init__(self,game):
        return None

        
    def isLegalMove(self,game):
        
        if game.newCol < 8 and game.newCol >-1 and game.newRow < 8 and game.newRow > -1:
            #if on board
            if game.player == 1:
                #player one's pawns can only move up
                if game.newCol == game.oldCol and game.newRow == game.oldRow-1:
                    #after first move of a specific pawn, no longer have option to move it two spaces
                    if game.board[game.oldRow][game.oldCol].pic == 'whitepawn1.gif':
                        #variable that lets you move pawn two on first move
                        game.WP1move = False
                        return True
                    if game.board[game.oldRow][game.oldCol].pic == 'whitepawn2.gif':
                        game.WP2move = False
                        return True
                    if game.board[game.oldRow][game.oldCol].pic == 'whitepawn3.gif':
                        game.WP3move = False
                        return True
                    if game.board[game.oldRow][game.oldCol].pic == 'whitepawn4.gif':
                        game.WP4move = False
                        return True
                    if game.board[game.oldRow][game.oldCol].pic == 'whitepawn5.gif':
                        game.WP5move = False
                        return True
                    if game.board[game.oldRow][game.oldCol].pic == 'whitepawn6.gif':
                        game.WP6move = False
                        return True
                    if game.board[game.oldRow][game.oldCol].pic == 'whitepawn7.gif':
                        game.WP7move = False
                        return True
                    if game.board[game.oldRow][game.oldCol].pic == 'whitepawn8.gif':
                        game.WP8move = False

                    return True
                    
                elif game.newCol == game.oldCol and game.newRow == game.oldRow-2:
                    #if your first move is two spaces (can only do on first move):
                    if game.board[game.oldRow][game.oldCol].pic == 'whitepawn1.gif' and game.WP1move == True:
                        #can no longer do once variable is false
                        game.WP1move = False
                        return True
                    if game.board[game.oldRow][game.oldCol].pic == 'whitepawn2.gif' and game.WP2move == True:
                        game.WP2move = False
                        return True
                    if game.board[game.oldRow][game.oldCol].pic == 'whitepawn3.gif' and game.WP3move == True:
                        game.WP3move = False
                        return True
                    if game.board[game.oldRow][game.oldCol].pic == 'whitepawn4.gif' and game.WP4move == True:
                        game.WP4move = False
                        return True
                    if game.board[game.oldRow][game.oldCol].pic == 'whitepawn5.gif' and game.WP5move == True:
                        game.WP5move = False
                        return True
                    if game.board[game.oldRow][game.oldCol].pic == 'whitepawn6.gif' and game.WP6move == True:
                        game.WP6move = False
                        return True
                    if game.board[game.oldRow][game.oldCol].pic == 'whitepawn7.gif' and game.WP7move == True:
                        game.WP7move = False
                        return True
                    if game.board[game.oldRow][game.oldCol].pic == 'whitepawn8.gif' and game.WP8move == True:
                        game.WP8move = False
                        return True
                
                    
                return False
                
                
            #same code, just for black team
            
            else: #game.player == 0 (black)
                if game.newCol == game.oldCol and game.newRow == game.oldRow+1:
                    #black can only move down the board
                    if game.board[game.oldRow][game.oldCol].pic == 'blackpawn1.gif':
                        game.BP1move = False
                        return True
                    if game.board[game.oldRow][game.oldCol].pic == 'blackpawn2.gif':
                        game.BP2move = False
                        return True
                    if game.board[game.oldRow][game.oldCol].pic == 'blackpawn3.gif':
                        game.BP3move = False
                        return True
                    if game.board[game.oldRow][game.oldCol].pic == 'blackpawn4.gif':
                        game.BP4move = False
                        return True
                    if game.board[game.oldRow][game.oldCol].pic == 'blackpawn5.gif':
                        game.BP5move = False
                        return True
                    if game.board[game.oldRow][game.oldCol].pic == 'blackpawn6.gif':
                        game.BP6move = False
                        return True
                    if game.board[game.oldRow][game.oldCol].pic == 'blackpawn7.gif':
                        game.BP7move = False
                        return True
                    if game.board[game.oldRow][game.oldCol].pic == 'blackpawn8.gif':
                        game.BP8move = False
                    return True
                    
                elif game.newCol == game.oldCol and game.newRow == game.oldRow+2:
                    if game.board[game.oldRow][game.oldCol].pic == 'blackpawn1.gif' and game.BP1move == True:
                        game.BP1move = False
                        return True
                    if game.board[game.oldRow][game.oldCol].pic == 'blackpawn2.gif' and game.BP2move == True:
                        game.BP2move = False
                        return True
                    if game.board[game.oldRow][game.oldCol].pic == 'blackpawn3.gif' and game.BP3move == True:
                        game.BP3move = False
                        return True
                    if game.board[game.oldRow][game.oldCol].pic == 'blackpawn4.gif' and game.BP4move == True:
                        game.BP4move = False
                        return True
                    if game.board[game.oldRow][game.oldCol].pic == 'blackpawn5.gif' and game.BP5move == True:
                        game.BP5move = False
                        return True
                    if game.board[game.oldRow][game.oldCol].pic == 'blackpawn6.gif' and game.BP6move == True:
                        game.BP6move = False
                        return True
                    if game.board[game.oldRow][game.oldCol].pic == 'blackpawn7.gif' and game.BP7move == True:
                        game.BP7move = False
                        return True
                    if game.board[game.oldRow][game.oldCol].pic == 'blackpawn8.gif' and game.BP8move == True:
                        game.BP8move = False
                        return True
                return False
                
        return False
        
    def isLegalCapture(self,game):
        #allows for diagonal capture with pawns
        if game.newCol < 8 and game.newCol >-1 and game.newRow < 8 and game.newRow > -1:
            #on board
            if game.player == 0:
                if game.newRow == game.oldRow+1 and game.newCol == game.oldCol+1:
                    return True
                elif game.newRow == game.oldRow+1 and game.newCol == game.oldCol-1:
                    return True
                return False
            else: #if game.player == 1
                if game.newRow == game.oldRow-1 and game.newCol == game.oldCol+1:
                    return True
                elif game.newRow == game.oldRow-1 and game.newCol == game.oldCol-1:
                    return True 
                    
                return False
            return False
        return False
        
    def move(self,game):
        #move method for pawns (need their own as they don't capture where they normally move, unlike other pieces):
    
        #can only move forward if we are moving forwards to an empty (None) space
        if self.isLegalMove(game) and freePath(game) and game.board[game.oldRow][game.oldCol].player == game.player and game.board[game.newRow][game.newCol] == None:
            
            temp = game.board[game.newRow][game.newCol]
            
            #making move and deleting where the piece used to be:
            game.board[game.newRow][game.newCol] = game.board[game.oldRow][game.oldCol]
            game.board[game.oldRow][game.oldCol] = None
            
            for c in game.board:
                print(c)
                
            
            if inCheck(game):
                #can't put your king in check
                game.board[game.oldRow][game.oldCol] = game.board[game.newRow][game.newCol]
                game.board[game.newRow][game.newCol] = temp
                game.tryAgain = True
                
                
            
            
            else:
                #change player at end of a move
                if game.player == 0:
                    game.player = 1
                else: #if game.player == 1:
                    game.player = 0
                
        
        #if board place we're trying to go to is a piece        
        elif type(game.board[game.newRow][game.newCol]) == space:
            
            
            
            #if piece we're trying to capture is opposing team, we can get it (must use isLegalCapture:
            if self.isLegalCapture(game) and game.board[game.oldRow][game.oldCol].player == game.player and game.board[game.newRow][game.newCol].player != game.player:
                
                if type(game.board[game.newRow][game.newCol]) == space:
                    #don't draw photo of piece captured by pawn
                    if game.board[game.newRow][game.newCol].pic == 'blackrook1.gif':
                        game.drawBR = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'blackknight1.gif':
                        game.drawBkn = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'blackbishop1.gif':
                        game.drawBB = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'blackqueen.gif':
                        game.drawBQ = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'blackking.gif':
                        game.drawBK = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'blackbishop2.gif':
                        game.drawBB2 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'blackknight2.gif':
                        game.drawBKn2 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'blackrook2.gif':
                        game.drawBR2 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'blackpawn1.gif':
                        game.drawBP1 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'blackpawn2.gif':
                        game.drawBP2 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'blackpawn3.gif':
                        game.drawBP3 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'blackpawn4.gif':
                        game.drawBP4 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'blackpawn5.gif':
                        game.drawBP5 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'blackpawn6.gif':
                        game.drawBP6 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'blackpawn7.gif':
                        game.drawBP7 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'blackpawn8.gif':
                        game.drawBP8 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'whiterook1.gif':
                        game.drawWR = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'whiteknight1.gif':
                        game.drawWKn = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'whitebishop1.gif':
                        game.drawWB = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'whitequeen.gif':
                        game.drawWQ = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'whiteking.gif':
                        game.drawWK = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'whitebishop2.gif':
                        game.drawWB2 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'whiteknight2.gif':
                        game.drawWk2 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'whiterook2.gif':
                        game.drawWR2 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'whitepawn1.gif':
                        game.drawWP1 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'whitepawn2.gif':
                        game.drawWP2 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'whitepawn3.gif':
                        game.drawWP3 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'whitepawn4.gif':
                        game.drawWP4 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'whitepawn5.gif':
                        game.drawWP5 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'whitepawn6.gif':
                        game.drawWP6 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'whitepawn7.gif':
                        game.drawWP7 = False
                        
                if type(game.board[game.newRow][game.newCol]) == space:
                    if game.board[game.newRow][game.newCol].pic == 'whitepawn8.gif':
                        game.drawWP8 = False
                
                #making move and deleting where the piece used to be:
                game.board[game.newRow][game.newCol] = game.board[game.oldRow][game.oldCol]
                game.board[game.oldRow][game.oldCol] = None
                
                #useful for in-console viewing
                for c in game.board:
                    print(c)
                
                
                #change player at end of a move
                if game.player == 0:
                    game.player = 1
                else: #if game.player == 1:
                    game.player = 0
                    
            #case that a pawn tries to move forward, but hits an opposing team piece: get warning message
            else:
                game.tryAgain = True

        else:
            game.tryAgain = True
            
    def __repr__(self):
        return 'pawn'
                
        
    
class bishop(piece):
    #bishop class
    def __init__(self,game):
        return None
        
    def isLegalMove(self,game):
        if game.newCol < 8 and game.newCol >-1 and game.newRow < 8 and game.newRow > -1:
            #on board
            if abs(game.newCol - game.oldCol) == abs(game.newRow - game.oldRow):
                #moves diagonally
                return True
            return False
        return False
        
    def __repr__(self):
        return 'bishop'
        
        
        
class knight(piece):
    #knight class
    def __init__(self,game):
        return None
        
        
    #isLegalMove for knight also easiest place to control for landing on teammates vs enemies
    def isLegalMove(self,game):
        if game.newCol < 8 and game.newCol >-1 and game.newRow < 8 and game.newRow > -1:
            #on board
            if (game.newCol-game.oldCol, game.newRow-game.oldRow) in [(-2, -1), (-2, +1), (+2, -1), (+2, +1), (-1, -2), (-1, +2), (+1, -2), (+1, +2)]:
                #knight can only move in L-shapes
#inspired by: https://stackoverflow.com/questions/32933193/using-the-same-function-for-a-different-chess-piece
                if type(game.board[game.newRow][game.newCol]) != space:
                    return True
                elif game.board[game.newRow][game.newCol].player != game.player:
                    #can legally land on opposing team pieces, but not your own
                    return True
                return False
                    
            return False
        return False
        
    def __repr__(self):
        return 'knight'

        
class rook(piece):
    #rook class
    def __init__(self,game):
        return None
        
    def isLegalMove(self,game):
        if game.newCol < 8 and game.newCol >-1 and game.newRow < 8 and game.newRow > -1:
            #on board
            #controlling for vertical movement:
            if game.oldCol == game.newCol and game.newRow != game.oldRow:
                return True
            #controlling for horizontal movement:
            elif game.oldRow == game.newRow and game.newCol != game.oldCol:
                return True
            return False
        return False
        
    def __repr__(self):
        return 'rook'
        
class queen(piece):
    #queen class
    def __init__(self,game):
        return None
        
    def isLegalMove(self,game):
        #can move like either a bishop or a rook (
        
        if game.newCol < 8 and game.newCol >-1 and game.newRow < 8 and game.newRow > -1:
            #controlling for vertical movement:
            if game.oldCol == game.newCol and game.newRow != game.oldRow:
                return True
            #controlling for horizontal movement:
            elif game.oldRow == game.newRow and game.newCol != game.oldCol:
                return True
            #controlling for diag movement:
            elif abs(game.newCol - game.oldCol) == abs(game.newRow - game.oldRow):
                return True
            #return False
            else:
                return False
        return False
    
    
    def __repr__(self):
        return 'queen'
        
        
class king(piece):
    #king class
    def __init__(self,game):
        return None
        
    def isLegalMove(self,game):
        if game.newCol < 8 and game.newCol >-1 and game.newRow < 8 and game.newRow > -1:
            #on board
            if (game.oldCol == game.newCol +1 or game.oldCol == game.newCol - 1 or game.newRow == game.oldRow + 1 or game.newRow == game.oldRow - 1):
                #can move one space horizontally, diagonally, or vertically
                return True
        
    def __repr__(self):
        return 'king'





## ANIMATION 

from tkinter import *



def init(data):
    #initializing data
         
    data.toggle = 0 
    #0 represents oldRow,oldCol move, when it toggles, it becomes newRow,newCol, 
    
    #ariables for the size of the board and drawing:
    cellWidth = data.width//len(data.board[0])
    cellHeight = data.height//len(data.board)
    data.cellSize = min(cellWidth,cellHeight)
    
    #initializing this for warnings:
    data.tryAgain = False
    
    #coordinates for left and topmost pixels at which to draw pieces:
    data.BRleft = 0 
    data.BRtop = 0 
    data.BKnleft = data.cellSize
    data.BKntop = 0
    data.BBleft = 2*data.cellSize
    data.BBtop = 0
    data.BQleft = 3*data.cellSize
    data.BQtop = 0
    data.BKleft = 4*data.cellSize
    data.BKtop = 0
    data.BB2left = 5*data.cellSize
    data.BB2top = 0
    data.BKn2left = 6*data.cellSize
    data.Bkn2top = 0
    data.BRleft = 7*data.cellSize
    data.BRtop = 0
    
    data.BP1left = 0
    data.BP2left = data.cellSize
    data.BP3left = 2*data.cellSize
    data.BP4left = 3*data.cellSize
    data.BP5left = 4*data.cellSize
    data.BP6left = 5*data.cellSize
    data.BP7left = 6*data.cellSize
    data.BP8left = 7*data.cellSize
    
    data.BP1top = data.cellSize
    data.BP2top = data.cellSize
    data.BP3top = data.cellSize
    data.BP4top = data.cellSize
    data.BP5top = data.cellSize
    data.BP6top = data.cellSize
    data.BP7top = data.cellSize
    data.BP8top = data.cellSize
    
    data.WRleft = 0
    data.WRtop = data.height - data.cellSize
    data.WKnleft = data.cellSize
    data.WKntop = data.height - data.cellSize
    data.WBleft = 2*data.cellSize
    data.WBtop = data.height - data.cellSize
    data.WQleft = 3*data.cellSize
    data.WQtop = data.height - data.cellSize
    data.WKleft = 4*data.cellSize
    data.WKtop = data.height - data.cellSize
    data.WB2left = 5*data.cellSize
    data.WB2top = data.height - data.cellSize
    data.WKn2left = 6*data.cellSize
    data.Wkn2top = data.height - data.cellSize
    data.WRleft = 7*data.cellSize
    data.WRtop = data.height - data.cellSize
    
    data.WP1left = 0
    data.WP2left = data.cellSize
    data.WP3left = 2*data.cellSize
    data.WP4left = 3*data.cellSize
    data.WP5left = 4*data.cellSize
    data.WP6left = 5*data.cellSize
    data.WP7left = 6*data.cellSize
    data.WP8left = 7*data.cellSize
    
    data.WP1top = data.height - 2*data.cellSize
    data.WP2top = data.height - 2*data.cellSize
    data.WP3top = data.height - 2*data.cellSize
    data.WP4top = data.height - 2*data.cellSize
    data.WP5top = data.height - 2*data.cellSize
    data.WP6top = data.height - 2*data.cellSize
    data.WP7top = data.height - 2*data.cellSize
    data.WP8top = data.height - 2*data.cellSize
    
    #will control whether or not to draw a certain piece
    #changed to false when a piece is captured:
        
    data.drawBR = True
    data.drawBKn = True
    data.drawBB = True
    data.drawBQ = True
    data.drawBK = True
    data.drawBB2 = True
    data.drawBKn2 = True
    data.drawBR2 = True
    
    data.drawBP1 = True
    data.drawBP2 = True
    data.drawBP3 = True
    data.drawBP4 = True
    data.drawBP5 = True
    data.drawBP6 = True
    data.drawBP7 = True
    data.drawBP8 = True
    
    data.drawWR = True
    data.drawWKn = True
    data.drawWB = True
    data.drawWQ = True
    data.drawWK = True
    data.drawWB2 = True
    data.drawWKn2 = True
    data.drawWR2 = True
    
    data.drawWP1 = True
    data.drawWP2 = True
    data.drawWP3 = True
    data.drawWP4 = True
    data.drawWP5 = True
    data.drawWP6 = True
    data.drawWP7 = True
    data.drawWP8 = True
    
    
    #When True, that pawn has not moved yet, and its first move can be two forwards
    
    data.WP1move = True
    data.WP2move = True
    data.WP3move = True
    data.WP4move = True
    data.WP5move = True
    data.WP6move = True
    data.WP7move = True
    data.WP8move = True
    
    data.BP1move = True
    data.BP2move = True
    data.BP3move = True
    data.BP4move = True
    data.BP5move = True
    data.BP6move = True
    data.BP7move = True
    data.BP8move = True
    
    #start game on main menu
    data.menu = True


def mousePressed(event,data):
    #handles clicking of mouse
    
    if data.menu == False:
        data.tryAgain = False
        if data.toggle == 0:
            #first click always handles choosing a piece
            (data.oldRow,data.oldCol) = (event.y//data.cellSize, event.x//data.cellSize)
            data.toggle = 1
        elif data.toggle == 1:
            #second click always handles choosing where that piece goes
            #these strict demarcations controlled by switching of data.toggle
            (data.newRow,data.newCol) = (event.y//data.cellSize, event.x//data.cellSize)
            if type(data.board[data.oldRow][data.oldCol]) == space:
                (data.board[data.oldRow][data.oldCol]).piece.move(data)
                data.toggle = 0
            else:
                data.tryAgain = True
                data.toggle = 0

        
    
    
def keyPressed(event,data):
    #handles pressing of keys
    
    if data.menu == True:
        if event.keysym == 'space':
            #unpauses or starts game
            data.menu = False
    else:
        if event.keysym == 'r':
            #restarts game
            data.__init__()
            init(data)
            
        if event.keysym == 'x':
            #player 0 concedes (black)
            data.player0Concede = True
            
        if event.keysym == 'o':
            #player 1 concedes (white)
            data.player1Concede = True
            
        if event.keysym == 'm':
            #view main menu without restarting game
            data.menu = True
        

    
def timerFired(data):
    #not used
    return 420
    
def redrawAll(canvas,data):
    #redraws all
    
    if data.menu == True:
        #draws background and words for main menu
        canvas.pack()
        background = PhotoImage(file="chessBackground.gif") 
        canvas.create_image(0,0, image=background) 

        canvas.create_text(data.width/2, data.height/2 - 200, text = 'Python Chess', font = 'Helvetica 60 bold', fill = 'gold')
        
        canvas.create_text(data.width/2, data.height/2 - 60, text = 'Press \'Space\' to start!', fill = 'gold', font = 'Helvetica 40 bold')
        
        canvas.create_text(data.width/2, data.height/2, text = 'Controls:', font = 'Helvetica 34 bold', fill = 'gold')
        canvas.create_text(data.width/2, data.height/2 + 55, text = 'Click a piece to select it', font = 'Helvetica 28 bold', fill = 'gold')
        canvas.create_text(data.width/2, data.height/2 + 90, text = 'Click location on board to move there', font = 'Helvetica 28 bold', fill = 'gold')
        canvas.create_text(data.width/2, data.height/2 + 125, text = 'Press \'r\' to restart game', font = 'Helvetica 28 bold', fill = 'gold')
        canvas.create_text(data.width/2, data.height/2 + 160, text = 'Press \'x\' to concede as Black', font = 'Helvetica 28 bold', fill = 'gold')
        canvas.create_text(data.width/2, data.height/2 + 195, text = 'Press \'o\' to concede as White', font = 'Helvetica 28 bold', fill = 'gold')
        canvas.create_text(data.width/2, data.height/2 + 230, text = 'Press \'m\' to pause game at menu', font = 'Helvetica 28 bold', fill = 'gold')
        canvas.create_text(data.width/2, data.height/2 + 265, text = 'Press \'Space\' to continue paused game', font = 'Helvetica 28 bold', fill = 'gold')
        
        mainloop()
        
    else:
        #when game actually starts 
            
        drawBoard(canvas,data)
        #draws the actual board
        
        if data.tryAgain == True:
            #warning message if data.tryAgain is True
            canvas.create_text(data.width/2, data.height/2, text = 'Invalid move, choose a piece!', fill = 'red', font = 'Times 34 bold')
            
        
    
        
        canvas.pack()    
        #loading in images to be drawn  
        img = PhotoImage(file="blackrook1.gif") 
        img2 = PhotoImage(file="blackknight1.gif")
        img3 = PhotoImage(file="blackbishop1.gif") 
        img4 = PhotoImage(file="blackqueen.gif")
        img5 = PhotoImage(file="blackking.gif") 
        img6 = PhotoImage(file="blackbishop2.gif")
        img7 = PhotoImage(file="blackknight2.gif") 
        img8 = PhotoImage(file="blackrook2.gif") 
        img9 = PhotoImage(file="blackpawn1.gif") 
        img10 = PhotoImage(file="blackpawn2.gif")
        img11 = PhotoImage(file="blackpawn3.gif") 
        img12 = PhotoImage(file="blackpawn4.gif")
        img13 = PhotoImage(file="blackpawn5.gif") 
        img14 = PhotoImage(file="blackpawn6.gif")
        img15 = PhotoImage(file="blackpawn7.gif") 
        img16 = PhotoImage(file="blackpawn8.gif") 
        img17 = PhotoImage(file="whiterook1.gif") 
        img18 = PhotoImage(file="whiteknight1.gif")
        img19 = PhotoImage(file="whitebishop1.gif") 
        img20 = PhotoImage(file="whitequeen.gif")
        img21 = PhotoImage(file="whiteking.gif") 
        img22 = PhotoImage(file="whitebishop2.gif")
        img23 = PhotoImage(file="whiteknight2.gif") 
        img24 = PhotoImage(file="whiterook2.gif") 
        img25 = PhotoImage(file="whitepawn1.gif") 
        img26 = PhotoImage(file="whitepawn2.gif")
        img27 = PhotoImage(file="whitepawn3.gif") 
        img28 = PhotoImage(file="whitepawn4.gif")
        img29 = PhotoImage(file="whitepawn5.gif") 
        img30 = PhotoImage(file="whitepawn6.gif")
        img31 = PhotoImage(file="whitepawn7.gif") 
        img32 = PhotoImage(file="whitepawn8.gif")

        
        if data.drawBR == True:
            #draw image for a certain piece if its variable is True (not captured)
            canvas.create_image(data.BRleft,data.BRtop, anchor=NW, image=img) 
            
        if data.drawBKn == True:
            canvas.create_image(data.Bknleft,data.Bkntop, anchor=NW, image=img2) 
            
        if data.drawBB == True:
            canvas.create_image(data.BBleft,data.BBtop, anchor = NW, image=img3)
        
        if data.drawBQ == True:
            canvas.create_image(data.BQleft,data.BQtop, anchor=NW, image=img4) 
            
        if data.drawBK == True:
            canvas.create_image(data.BKleft,data.BKtop, anchor = NW, image=img5)
            
        if data.drawBB2 == True:
            canvas.create_image(data.BB2left,data.BB2top, anchor=NW, image=img6)
        
        if data.drawBKn2 == True:
            canvas.create_image(data.Bkn2left,data.Bkn2top, anchor = NW, image=img7)
            
        if data.drawBR2 == True:
            canvas.create_image(data.BR2left,data.BR2top, anchor=NW, image=img8) 
            
        if data.drawBP1 == True:
            canvas.create_image(data.BP1left,data.BP1top, anchor = NW, image=img9)
            
        if data.drawBP2 == True:
            canvas.create_image(data.BP2left,data.BP2top, anchor=NW, image=img10) 
            
        if data.drawBP3 == True:
            canvas.create_image(data.BP3left,data.BP3top, anchor = NW, image=img11)
            
        if data.drawBP4 == True:
            canvas.create_image(data.BP4left,data.BP4top, anchor=NW, image=img12) 
            
        if data.drawBP5 == True:
            canvas.create_image(data.BP5left,data.BP5top, anchor = NW, image=img13)
        
        if data.drawBP6 == True:
            canvas.create_image(data.BP6left,data.BP6top, anchor=NW, image=img14) 
            
        if data.drawBP7 == True:
            canvas.create_image(data.BP7left,data.BP7top, anchor = NW, image=img15)
            
        if data.drawBP8 == True:
            canvas.create_image(data.BP8left,data.BP8top, anchor=NW, image=img16) 
            
        if data.drawWR == True:
            canvas.create_image(data.WRleft,data.WRtop, anchor=NW, image=img17) 
            
        if data.drawWKn == True:
            canvas.create_image(data.Wknleft,data.Wkntop, anchor=NW, image=img18) 
            
        if data.drawWB == True:
            canvas.create_image(data.WBleft,data.WBtop, anchor = NW, image=img19)
            
        if data.drawWQ == True:
            canvas.create_image(data.WQleft,data.WQtop, anchor=NW, image=img20) 
            
        if data.drawWK == True:
            canvas.create_image(data.WKleft,data.WKtop, anchor = NW, image=img21)
        
        if data.drawWB2 == True:
            canvas.create_image(data.WB2left,data.WB2top, anchor=NW, image=img22) 
        
        if data.drawWKn2 == True:
            canvas.create_image(data.Wkn2left,data.Wkn2top, anchor = NW, image=img23)
        
        if data.drawWR2 == True:
            canvas.create_image(data.WR2left,data.WR2top, anchor=NW, image=img24) 
            
        if data.drawWP1 == True:
            canvas.create_image(data.WP1left,data.WP1top, anchor = NW, image=img25)
            
        if data.drawWP2 == True:
            canvas.create_image(data.WP2left,data.WP2top, anchor=NW, image=img26) 
            
        if data.drawWP3 == True:
            canvas.create_image(data.WP3left,data.WP3top, anchor = NW, image=img27)
            
        if data.drawWP4 == True:
            canvas.create_image(data.WP4left,data.WP4top, anchor=NW, image=img28)
        
        if data.drawWP5 == True:
            canvas.create_image(data.WP5left,data.WP5top, anchor = NW, image=img29)
            
        if data.drawWP6 == True:
            canvas.create_image(data.WP6left,data.WP6top, anchor=NW, image=img30) 
            
        if data.drawWP7 == True:
            canvas.create_image(data.WP7left,data.WP7top, anchor = NW, image=img31)
            
        if data.drawWP8 == True:
            canvas.create_image(data.WP8left,data.WP8top, anchor=NW, image=img32)
            
        if data.player0Concede:
            #show screen demarcating end of game if player 0 (black) concedes
            canvas.create_rectangle(0,0,data.width,data.height,fill='blue')
            canvas.create_text(data.width/2,data.height/2,text = 'Good game! Black has conceded. Press \'r\' to restart',font = 'Helvetica 22 bold')
            
        if data.player1Concede:
            #show screen demarcating end of game if player 1 (white) concedes
            canvas.create_rectangle(0,0,data.width,data.height,fill='blue')
            canvas.create_text(data.width/2,data.height/2,text = 'Good game! White has conceded. Press \'r\' to restart',font = 'Helvetica 22 bold')
            
        mainloop()
        
    
def drawBoard(canvas,data):
    #draws the actual board
    i = 0
    j = 0
    for row in range(len(data.board)):
        i += 1
        for col in range(len(data.board[0])):
            
            #setting color of each space in the board:
            if (i+j)%2 == 0:
                color = 'black'
            else: 
                color = 'white'
                
            left = col*data.cellSize
            top = row*data.cellSize
            canvas.create_rectangle(left, top, left+data.cellSize, top+data.cellSize, fill = color)
            #draw black and white squares in pattern in correct locations
            
            #initialize variables for each instance of space here
            
            if type(data.board[row][col]) == space:
               #different pieces of same type have different filenames to differentiate them
                
                if data.board[row][col].pic == 'blackrook1.gif':
                    #draw pieces in correct locations on the board
                    data.BRleft = left
                    data.BRtop = top
                    
                if data.board[row][col].pic == 'blackknight1.gif':
                    data.Bknleft = left
                    data.Bkntop = top
                    
                if data.board[row][col].pic == 'blackbishop1.gif':
                    data.BBleft = left
                    data.BBtop = top
                    
                if data.board[row][col].pic == 'blackqueen.gif':
                    data.BQleft = left
                    data.BQtop = top
                    
                if data.board[row][col].pic == 'blackking.gif':
                    data.BKleft = left
                    data.BKtop = top
                    
                if data.board[row][col].pic == 'blackbishop2.gif':
                    data.BB2left = left
                    data.BB2top = top
                    
                if data.board[row][col].pic == 'blackknight2.gif':
                    data.Bkn2left = left
                    data.Bkn2top = top
                    
                if data.board[row][col].pic == 'blackrook2.gif':
                    data.BR2left = left
                    data.BR2top = top
                    
                if data.board[row][col].pic == 'blackpawn1.gif':
                    data.BP1left = left
                    data.BP1top = top
                    
                if data.board[row][col].pic == 'blackpawn2.gif':
                    data.BP2left = left
                    data.BP2top = top
                    
                if data.board[row][col].pic == 'blackpawn3.gif':
                    data.BP3left = left
                    data.BP3top = top
                    
                if data.board[row][col].pic == 'blackpawn4.gif':
                    data.BP4left = left
                    data.BP4top = top
                    
                if data.board[row][col].pic == 'blackpawn5.gif':
                    data.BP5left = left
                    data.BP5top = top
                    
                if data.board[row][col].pic == 'blackpawn6.gif':
                    data.BP6left = left
                    data.BP6top = top
                    
                if data.board[row][col].pic == 'blackpawn7.gif':
                    data.BP7left = left
                    data.BP7top = top
                    
                if data.board[row][col].pic == 'blackpawn8.gif':
                    data.BP8left = left
                    data.BP8top = top
                    
                if data.board[row][col].pic == 'whiterook1.gif':
                    data.WRleft = left
                    data.WRtop = top
                    
                if data.board[row][col].pic == 'whiteknight1.gif':
                    data.Wknleft = left
                    data.Wkntop = top
                    
                if data.board[row][col].pic == 'whitebishop1.gif':
                    data.WBleft = left
                    data.WBtop = top
                    
                if data.board[row][col].pic == 'whitequeen.gif':
                    data.WQleft = left
                    data.WQtop = top
                    
                if data.board[row][col].pic == 'whiteking.gif':
                    data.WKleft = left
                    data.WKtop = top
                    
                if data.board[row][col].pic == 'whitebishop2.gif':
                    data.WB2left = left
                    data.WB2top = top
                    
                if data.board[row][col].pic == 'whiteknight2.gif':
                    data.Wkn2left = left
                    data.Wkn2top = top
                    
                if data.board[row][col].pic == 'whiterook2.gif':
                    data.WR2left = left
                    data.WR2top = top
                    
                if data.board[row][col].pic == 'whitepawn1.gif':
                    data.WP1left = left
                    data.WP1top = top
                    
                if data.board[row][col].pic == 'whitepawn2.gif':
                    data.WP2left = left
                    data.WP2top = top
                    
                if data.board[row][col].pic == 'whitepawn3.gif':
                    data.WP3left = left
                    data.WP3top = top
                    
                if data.board[row][col].pic == 'whitepawn4.gif':
                    data.WP4left = left
                    data.WP4top = top
                    
                if data.board[row][col].pic == 'whitepawn5.gif':
                    data.WP5left = left
                    data.WP5top = top
                    
                if data.board[row][col].pic == 'whitepawn6.gif':
                    data.WP6left = left
                    data.WP6top = top
                    
                if data.board[row][col].pic == 'whitepawn7.gif':
                    data.WP7left = left
                    data.WP7top = top
                    
                if data.board[row][col].pic == 'whitepawn8.gif':
                    data.WP8left = left
                    data.WP8top = top
                    
            j += 1
            

#################################################################
# use the run function as-is
#################################################################

def run(width=300, height=300):
    #run function
    #Taken from 15-112 course website:
    #https://www.cs.cmu.edu/~112/notes/rec6.py
    def redrawAllWrapper(canvas, game):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, game.width, game.height,
                                fill='white', width=0)
        redrawAll(canvas, game)
        canvas.update()

    def mousePressedWrapper(event, canvas, game):
        mousePressed(event, game)
        redrawAllWrapper(canvas, game)

    def keyPressedWrapper(event, canvas, game):
        keyPressed(event, game)
        redrawAllWrapper(canvas, game)

    def timerFiredWrapper(canvas, game):
        timerFired(game)
        redrawAllWrapper(canvas, game)
        # pause, then call timerFired again
        canvas.after(game.timerDelay, timerFiredWrapper, canvas, game)
    # Set up data and call init
    #class Struct(object): pass
    data = game()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(600, 600)    





