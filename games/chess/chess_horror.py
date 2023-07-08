
import pygame,time,copy
from itertools import permutations

move2 = None

def play(piece,move,A,B,board):
    record = copy.deepcopy(A['piece'])
    global go,valid,check,wind,state
    if go == 'w':
        goNum = 1
    else:
        goNum = 0
    if piece == 'rC' or piece == 'r':
        rook.moveCheck(move,piece)
        #print(valid)
        #print('rook')
        if valid:
            A['piece'] = 'r'
    elif piece == 'kn':
        knight.moveCheck(move,piece)
        #print(valid)
        #print('knight')
    elif piece == 'b':
        bishop.moveCheck(move,piece)
        #print(valid)
        #print('bishop')
    elif piece == 'q':
        queen.moveCheck(move,piece)
        #print(valid)
        #print('queen')
    elif piece == 'kC' or piece == 'k':
        king.moveCheck(move,piece)
        #print(valid)
        #print('king')
        if valid:
            A['piece'] = 'k'
    elif piece == 'pU' or piece == 'p':
        pawn.moveCheck(move,piece)
        #print('pawn')
        #print(valid)
        if valid:
            A['piece'] = 'p'
    if valid and not checkCheck(move,False):
            valid = False
    if valid and (piece != 'kC' and piece != 'k'):
        var1 = checkCheck(move,True)
        if go == 'w':
            go = 'b'
        else:
            go = 'w'
        var2 = enemyCheck(move)
        if not var1:
            check[goNum] = True
        else:
            check[goNum] = False

        check[abs(goNum-1)] = False


        for i in range(0,len(piecesL)):
            for e in range(0,len(piecesL[i])):
                search = piecesL[i][e]
                if (search['piece'] == 'k' or search['piece'] == 'kC') and search['col'] != go:
                    theOne = iluminate.k(search['pos'],search['col'],search['piece'],board,False)
                    break
        removal = []
        for i in range(0,len(theOne)):
            if theOne[i][0] == -1 or theOne[i][1] == -1:
                removal.append(theOne[i])
            try:
                board[theOne[i][1]][theOne[i][0]]
            except:
                removal.append(theOne[i])
        for i in range(0,len(removal)):
            try:
                theOne.remove(removal[i])
            except:
                pass

        removal = []
        for o in range(0,len(theOne)):
            for p in range(0,len(var2)):
                if var2[p] == theOne[o]:
                    removal.append(theOne[o])
        for u in range(0,len(removal)):
            try:
                theOne.remove(removal[u])
            except:
                pass
                
        if check[goNum]:
            #print(theOne)
            if theOne == []:
                state = 'win'
                if go == 'w':
                    wind = 'white'
                else:
                    wind = 'black'
        else:
            if go == 'b':
                colour = 'w'
            else:
                colour = 'b'
            stale(move,colour,theOne)
    #the thing I worked on last to allow pawn to move two even after being checked and seen as unvalid (It works)
    if not valid and A['piece'] == 'p' and record == 'pU':
        A['piece'] = 'pU'
        

def enemyCheck(move):
    global go
    board1 = copy.deepcopy(board)
    board1 = listPlay(move,board1)
    if go == 'w':
        go = 'b'
    else:
        go = 'w'
    enemies = []
    danger = []
    for o in range(0,len(piecesL)):
        for e in range(0,len(piecesL[o])):
            idk = piecesL[o][e]
            posTemp = [int(idk['pos'][0]/64),int(idk['pos'][1]/64)]
            if idk['col'] == go and posTemp != move[1]:
                enemies.append(idk)
    for i in range(0,len(enemies)):
        posTemp2 = [int(enemies[i]['pos'][0]/64),int(enemies[i]['pos'][1]/64)]
        if posTemp2 == move[0]:
            newPos = (move[1][0]*64,move[1][1]*64)
        else:
            newPos = enemies[i]['pos']
        check = enemies[i]['ilu'](newPos,enemies[i]['col'],enemies[i]['piece'],board1,True)
        danger = danger + check
    return danger
    

def stale(move,col,theOne):
    global go,state,wind
    board1 = copy.deepcopy(board)
    board1 = listPlay(move,board1)
    if go == 'w':
        go = 'b'
    else:
        go = 'w'
    pieceMoves = []
    for o in range(0,len(piecesL)):
        for e in range(0,len(piecesL[o])):
            idk = piecesL[o][e]
            posTemp = [int(idk['pos'][0]/64),int(idk['pos'][1]/64)]
            if idk['col'] == col and posTemp != move[1]:
                if posTemp == move[0]:
                    newPos = (move[1][0]*64,move[1][1]*64)
                else:
                    newPos = copy.deepcopy(idk['pos'])
                pieceMove = idk['ilu'](newPos,idk['col'],idk['piece'],board1,False)
                pieceMoves = pieceMoves + pieceMove
    if pieceMoves == [] and theOne == []:
         state = 'win'
         wind = 'No one'         
                        


def checkCheck(move,reverse):
    def copyVar():
        return copy.deepcopy(board)
    tempBoard = copyVar()
    global go
    pos = ()
    tempBoard = listPlay(move,tempBoard)
    if go == 'w':
        go = 'b'
    else:
        go = 'w'
    if reverse:
        if go == 'w':
            go = 'b'
        else:
            go = 'w'
    fix = False
    if go == 'w':
        name1 = 'kw'
    else:
        name1 = 'kb'
    for i in range(0,8):
        for o in range(0,8):
            if tempBoard[i][o] == name1:
                pos = (o*64,i*64)
    return saftyCheck(pos,go,tempBoard,move,reverse,fix)
    tempBoard = []

def listPlay(move,board1):
    global go
    rowF = move[0][-1]
    columnF = move[0][0]
    rowE = move[-1][-1]
    columnE = move[-1][0]
    if isCastle:
        row2F = move2[0][-1]
        column2F = move2[0][0]
        row2E = move2[-1][-1]
        column2E = move2[-1][0]
    
    if not isCastle:
        board1[rowE][columnE] = board1[rowF][columnF]
        board1[rowF][columnF] = ' '
    else:
        board1[rowE][columnE] = board1[rowF][columnF]
        board1[rowF][columnF] = ' '
        board1[row2E][column2E] = board1[row2F][column2F]
        board1[row2F][column2F] = ' '
        
    if go == 'w':
        go = 'b'
    else:
        go = 'w'
    return board1

def pyPlay():
    if promote:
        A['image'] = metamorph[0]
        A['piece'] = metamorph[1]
    if not isCastle:
        changesA = [A['image'],A['col'],A['piece'],A['ilu']]
        B['image'] = changesA[0]
        B['col'] = changesA[1]
        B['piece'] = changesA[2]
        B['ilu'] = changesA[3]
        A['image'] = pygame.image.load('empty.png') 
        A['col'] = ' '
        A['piece'] = ' '
        A['ilu'] = None
    else:
        B['piece'] = 'r'
        posCheck = (move[1][0] *64 , move[1][1] *64)
        posCheck2 = (move2[1][0] *64 , move2[1][1] *64)
        for i in range(0,len(piecesL)):
            for e in range(0,len(piecesL[i])):
                if piecesL[i][e]['pos'] == posCheck:
                    a = piecesL[i][e]
                    #print('worked')
                elif piecesL[i][e]['pos'] == posCheck2:
                    b = piecesL[i][e]
                    #print('worked2')
        changesA = [A['image'],A['col'],A['piece'],A['ilu']]
        a['image'] = changesA[0]
        a['col'] = changesA[1]
        a['piece'] = changesA[2]
        a['ilu'] = changesA[3]
        A['image'] = pygame.image.load('empty.png') 
        A['col'] = ' '
        A['piece'] = ' '
        A['ilu'] = False
        

        changesB = [B['image'],B['col'],B['piece'],B['ilu']]
        b['image'] = changesB[0]
        b['col'] = changesB[1]
        b['piece'] = changesB[2]
        b['ilu'] = changesB[3]
        B['image'] = pygame.image.load('empty.png') 
        B['col'] = ' '
        B['piece'] = ' '



def newRectinator(positions):
    newRects = []
    for i in range(0,len(positions)):
        x = positions[i][0] * 64
        y = positions[i][1] * 64
        newRects.append(pygame.Rect(x,y,64,64))
    return newRects

def saftyCheck(pos,col,board1,move,reverse,fix):
    pos = (int(pos[0]/64),int(pos[1]/64))
    enemies = []
    danger = []
    for o in range(0,len(piecesL)):
        for e in range(0,len(piecesL[o])):
            idk = piecesL[o][e]
            posTemp = [int(idk['pos'][0]/64),int(idk['pos'][1]/64)]
            if idk['col'] != col and idk['col'] != ' ' and posTemp != move[1]:
                enemies.append(idk)
    for i in range(0,len(enemies)):
        posTemp2 = [int(enemies[i]['pos'][0]/64),int(enemies[i]['pos'][1]/64)]
        if posTemp2 == move[0]:
            newPos = (move[1][0]*64,move[1][1]*64)
        else:
            newPos = copy.deepcopy(enemies[i]['pos'])
            
        check = enemies[i]['ilu'](newPos,enemies[i]['col'],enemies[i]['piece'],board1,fix)

        danger = danger + check

    for i in range(0,len(danger)):
        if pos == danger[i]:
            booli =  False
            break
    else:
        booli = True
    return booli
    enemies = []
    

###############################################
class iluminate:
    def __init__(self,pos):
        self.pos = pos

    def iterator(moves,iters,pos,col,board1):
        if col == 'w':
            op = 'b'
        else:
            op = 'w'
        for o in range(0,4):
            for i in range(1,8):
                try:
                    if board1[int(pos[1]/64) + i*iters[o][1]][int(pos[0]/64) + i*iters[o][0]] == ' ':
                        moves.append((int(pos[0]/64) + i*iters[o][0],int(pos[1]/64) + i*iters[o][1]))
                    elif list(board1[int(pos[1]/64) + i*iters[o][1]][int(pos[0]/64) + i*iters[o][0]])[-1] == op:
                        moves.append((int(pos[0]/64) + i*iters[o][0],int(pos[1]/64) + i*iters[o][1]))
                        break
                    elif list(board1[int(pos[1]/64) + i*iters[o][1]][int(pos[0]/64) + i*iters[o][0]])[-1] == col:
                        break
                except:
                    break
        return moves
        

    def r(pos,col,piece,board1,fix):
        global checked
        checked = True
        rookMoves = []
        iters = [(0,1),(0,-1),(1,0),(-1,0)]
        rookMoves = iluminate.iterator(rookMoves,iters,pos,col,board1)
        return rookMoves
            
        
    def b(pos,col,piece,board1,fix):
        global checked
        checked = True
        bishopMoves = []
        iters = [(1,1),(-1,1),(1,-1),(-1,-1)]
        bishopMoves = iluminate.iterator(bishopMoves,iters,pos,col,board1)
        return bishopMoves

    def kn(pos,col,piece,board1,fix):
        global checked
        checked = True
        knightMove = [(1,2),(1,-2),(-1,2),(-1,-2),(2,-1),(2,1),(-2,-1),(-2,1)]
        knightMoves = []
        for i in range(0,8):
            try:
                if list(board1[int(pos[1]/64) + knightMove[i][1]][int(pos[0]/64)+knightMove[i][0]])[-1] != col:
                    #coordMoves.append((int(pos[0]/64)+knightMove[i][0],int(pos[1]/64)+knightMove[i][1]))
                    knightMoves.append((int(pos[0]/64)+knightMove[i][0],int(pos[1]/64)+knightMove[i][1]))
            except:
                pass
        return knightMoves
            

    def k(pos,col,piece,board1,fix):
        global checked
        checked = True
        if col == 'w':
            row = 7
        else:
            row = 0
        kingMove = permutations((-1,0,1),2);kingMove = list(kingMove);kingMove.append((-1,-1));kingMove.append((1,1))
        kingMoves = []
        for i in range(0,len(kingMove)):
            try:
                if list(board1[int(pos[1]/64) + kingMove[i][1]][int(pos[0]/64)+kingMove[i][0]])[-1] != col:
                    #coordMoves.append((int(pos[0]/64)+kingMove[i][0],int(pos[1]/64)+kingMove[i][1]))
                    kingMoves.append((int(pos[0]/64)+kingMove[i][0],int(pos[1]/64)+kingMove[i][1]))
            except:
                pass
        if piece == 'kC':

            for o in range(0,len(piecesL)):
                for e in range(0,len(piecesL[o])):
                    block = piecesL[o][e]
                    if block['pos'][1] == row*64 and block['pos'][0] == 0:
                        corn1 = block['piece']
                    if block['pos'][1] == row*64 and block['pos'][0] == 7*64:
                        corn2 = block['piece']
                            

            if corn1 == 'rC':             
                for i in range(1,int(pos[0]/64)):
                    if board1[row][i] != ' ':
                        break
                else:
                    kingMoves.append((0,row))

            if corn2 == 'rC':
                for i in range(int(pos[0]/64)+1,7):
                    if board1[row][i] != ' ':
                        break
                else:
                    kingMoves.append((7,row))
                    
        return kingMoves

    
    def q(pos,col,piece,board1,fix):
        global checked
        checked = True
        iters = [(1,1),(-1,1),(1,-1),(-1,-1)]
        iters2 = [(0,1),(0,-1),(1,0),(-1,0)]
        queenMoves = []
        queenMoves = iluminate.iterator(queenMoves,iters,pos,col,board1)
        queenMoves = iluminate.iterator(queenMoves,iters2,pos,col,board1)
        return queenMoves
        

    def p(pos,col,piece,board1,fix):
        global checked
        checked = True
        if col == 'w':
            dire = -1
            op = 'b'
        else:
            dire = 1
            op = 'w'
        pawnMoves = []
        take = [(-1,dire),(1,dire)]
        if not fix:
            for i in range(0,2):
                try:
                    if list(board1[int(pos[1]/64) + take[i][1]][int(pos[0]/64)+take[i][0]])[-1] == op:
                        pawnMoves.append((int(pos[0]/64)+take[i][0],int(pos[1]/64)+take[i][1]))
                except:
                    pass
            if list(board1[int(pos[1]/64) + dire][int(pos[0]/64)])[-1] == ' ':
                    pawnMoves.append((int(pos[0]/64),int(pos[1]/64) + dire))
            if piece == 'pU' and board1[int(pos[1]/64) + 2*dire][int(pos[0]/64)] == ' ' and board1[int(pos[1]/64) + dire][int(pos[0]/64)] == ' ':
                    pawnMoves.append((int(pos[0]/64),int(pos[1]/64) + 2*dire))
        if fix:
            for i in range(0,2):
                try:
                    #if list(board1[int(pos[1]/64) + take[i][1]][int(pos[0]/64)+take[i][0]])[-1] != col:
                    pawnMoves.append((int(pos[0]/64)+take[i][0],int(pos[1]/64)+take[i][1]))
                except:
                    pass
            
        return pawnMoves
                

        
class king:
    def __init__(self,move,col):
        self.move = move
        self.col = col

    def moveCheck(move,piece):
        
        rowF = move[0][-1]
        columnF = move[0][0]
        rowE = move[-1][-1]
        columnE = move[-1][0]

        global move2,valid
        
        if isCastle:
            if columnF > columnE:
                tempCoord = columnF -1
            if columnE > columnF:
                tempCoord = columnF +1
            while tempCoord != columnE:
                if board[rowF][tempCoord] != ' ':
                    valid = False

                if tempCoord < columnE:
                    tempCoord += 1
                if tempCoord > columnE:
                    tempCoord -= 1
            if valid:
                if move[1] == [0,7]:
                    move[1] = [2,7]
                    move2 = [[0,7],[3,7]]
                elif move[1] == [7,7]:
                    move[1] = [6,7]
                    move2 = [[7,7],[5,7]]
                elif move[1] == [0,0]:
                    move[1] = [2,0]
                    move2 = [[0,0],[3,0]]
                elif move[1] == [7,0]:
                    move[1] = [6,0]
                    move2 = [[7,0],[5,0]]
        elif abs(rowF - rowE) > 1 or abs(columnF - columnE) > 1:
            valid = False
    
class rook:
    def __init__(self,move,col):
        self.move = move
        self.col = col

    def moveCheck(move,piece):
        
        rowF = move[0][-1]
        columnF = move[0][0]
        rowE = move[-1][-1]
        columnE = move[-1][0]
        global valid
        
        def makeRange(f,t,inc):
            print(f,t,inc)
            return range(f-1,t,inc) if inc < 0 else range(f+1,t,inc)

        
        if move[0][0] != move[-1][0] and move[0][-1] != move[-1][-1]:
            valid = False
        elif move[0][0] == move[-1][0]:
            if move[0][-1] > move[-1][-1]:
                inc = -1
            else:
                inc = 1
            for i in makeRange(rowF,rowE,inc):
                if board[i][columnF] != ' ':
                    valid = False

        elif move[0][-1] == move[-1][-1]:
            if move[0][0] > move[-1][0]:
                inc = -1
            else:
                inc = 1
            for i in makeRange(columnF,columnE,inc):
                if board[rowF][i] != ' ':
                    valid = False


class pawn:
    def __init__(self,move,col):
        self.move = move
        self.col = col

    def moveCheck(move,piece):
        
        rowF = move[0][-1]
        columnF = move[0][0]
        rowE = move[-1][-1]
        columnE = move[-1][0]

        global promote,state,valid
        
        if go == 'w':
            dire = -1
            row = 0
        else:
            dire = 1
            row = 7
        #print(dire)

        if piece == 'pU':
            if rowF + (2*dire) != rowE and rowF + dire != rowE:
                valid = False
                #print('1')
            if rowF + (2*dire) == rowE:
                if board[rowF+dire][columnF] != ' ':
                    valid = False
                    #print('6')
        elif rowF + dire != rowE:
            valid = False
            #print('2')

        if valid:
            if columnF != columnE:
                if columnF + 1 != columnE and columnF - 1 != columnE:
                    valid = False
                    #print('3')
                elif board[rowE][columnE] == ' ':
                    valid = False
                    #print('4')
            elif board[rowE][columnE] != ' ':
                valid = False
                #print('5')

        if valid and rowE == row:
            promote = True
            state = 'promote'

class knight:
    def __init__(self,move,col):
        self.move = move
        self.col = col

    def moveCheck(move,piece):
        
        rowF = move[0][-1]
        columnF = move[0][0]
        rowE = move[-1][-1]
        columnE = move[-1][0]
        global valid


        knightMove = [(1,2),(1,-2),(-1,2),(-1,-2),(2,-1),(2,1),(-2,-1),(-2,1)]
        for i in range(0,8):
            #print((columnF+knightMove[i][0],rowF+knightMove[i][1]))
            if [columnF+knightMove[i][0],rowF+knightMove[i][1]] == move[1]:
                break
        else:
            valid = False

class bishop:
    def __init__(self,move,col):
        self.move = move
        self.col = col

    def moveCheck(move,piece):
        
        rowF = move[0][-1]
        columnF = move[0][0]
        rowE = move[-1][-1]
        columnE = move[-1][0]
        global valid

        factor = ((columnF - columnE)*-1, (rowF - rowE)*-1)
        #print(factor)
        if abs(factor[0]) != abs(factor[1]):
            valid = False
        elif valid:
            interval = (int(factor[0]/abs(factor[0])),int(factor[1]/abs(factor[1])))
            #print(interval)
            for i in range(1,abs(factor[0])):
                if board[interval[1]*i+rowF][interval[0]*i+columnF] != ' ':
                    valid = False

class queen:
    def __init__(self,move,col):
        self.move = move
        self.col = col

    def moveCheck(move,piece):
        
        rowF = move[0][-1]
        columnF = move[0][0]
        rowE = move[-1][-1]
        columnE = move[-1][0]
        global valid

        factorQ = ((columnF - columnE)*-1, (rowF - rowE)*-1)
        #print(factor)
        if abs(factorQ[0]) == abs(factorQ[1]):
            #print('bishop')
            bishop.moveCheck(move,piece)
        else:
            #print('rook')
            rook.moveCheck(move,piece)
    
            
            
                
            
#############################################################

board = [['rb','nb','bb','qb','kb','bb','nb','rb'],#0
         ['pb','pb','pb','pb','pb','pb','pb','pb'],#1
         [' ',' ',' ',' ',' ',' ',' ',' '],#2
         [' ',' ',' ',' ',' ',' ',' ',' '],#3
         [' ',' ',' ',' ',' ',' ',' ',' '],#4
         [' ',' ',' ',' ',' ',' ',' ',' '],#5
         ['pw','pw','pw','pw','pw','pw','pw','pw'],#6
         ['rw','nw','bw','qw','kw','bw','nw','rw']]#7
#           0     1    2   3    4   5      6    7
'''

board = [['rb',' ','bb',' ','kb',' ','nb','rb'],
         ['pb', 'pb', ' ', ' ', ' ', 'pb', 'pb','pb'],
         [' ', ' ', 'nb', ' ', 'pb', ' ', ' ', ' '],
         ['pw', ' ', 'pw', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', 'qb', 'pb', ' ', ' ', ' ', 'bb'],
         ['nw', ' ', ' ', ' ', ' ', 'pw', ' ', ' '],
         [' ', ' ', ' ', 'kw', 'pw', ' ', 'pw', 'pw'],
         ['rw', ' ', 'bw', 'qw', ' ', 'bw', 'nw', 'rw']]
#          a   b   c   d   e   f   g    h
'''
go = 'w'
lastClick = -500
move = [None,None]


for i in range (0,8):
    print(board[i])


pygame.init()
screen = pygame.display.set_mode((512,512))
icon = pygame.image.load('t.png')
pygame.display.set_icon(icon)

bg = pygame.image.load('board.png')
green = pygame.image.load('green.png')


bRooks = []
bKnights = []
bBishops = []
bQueens = []
bKings = []
bPawns = []
wRooks = []
wKnights = []
wBishops = []
wQueens = []
wKings = []
wPawns = []
emptys = []

'''
boardPy = ['o#s#g#io'
          ,'aa###aaa'
          ,'##i#a###'
          ,'p#p#####'
          ,'##ua###s'
          ,'n####p##'
          ,'###kp#pp'
          ,'r#bq#bnr'
           ]
'''
boardPy = ['oisugsio'
          ,'aaaaaaaa'
          ,'########'
          ,'########'
          ,'########'
          ,'########'
          ,'pppppppp'
          ,'rnbqkbnr'
           ]

    
x=y=0
for row in boardPy:
    for col in row:
        if col == 'o':
            bRook = {
                'pos': (x,y),
                'rect': pygame.Rect(x,y,64,64),
                'image': pygame.image.load('bRook.png'),
                'col': 'b',
                'piece': 'rC',
                'ilu': iluminate.r
                }
            bRooks.append(bRook)
        if col == 'i':
            bKnight = {
                'pos': (x,y),
                'rect': pygame.Rect(x,y,64,64),
                'image': pygame.image.load('bKnight.png'),
                'col': 'b',
                'piece': 'kn',
                'ilu': iluminate.kn
                }
            bKnights.append(bKnight)
        if col == 's':
            bBishop = {
                'pos': (x,y),
                'rect': pygame.Rect(x,y,64,64),
                'image': pygame.image.load('bBishop.png'),
                'col': 'b',
                'piece': 'b',
                'ilu': iluminate.b
                }
            bBishops.append(bBishop)
        if col == 'u':
            bQueen = {
                'pos': (x,y),
                'rect': pygame.Rect(x,y,64,64),
                'image': pygame.image.load('bQueen.png'),
                'col': 'b',
                'piece': 'q',
                'ilu': iluminate.q
                }
            bQueens.append(bQueen)
        if col == 'g':
            bKing = {
                'pos': (x,y),
                'rect': pygame.Rect(x,y,64,64),
                'image': pygame.image.load('bKing.png'),
                'col': 'b',
                'piece': 'kC',
                'ilu': iluminate.k
                }
            bKings.append(bKing)
        if col == 'a':
            bPawn = {
                'pos': (x,y),
                'rect': pygame.Rect(x,y,64,64),
                'image': pygame.image.load('bPawn.png'),
                'col': 'b',
                'piece': 'pU',
                'ilu': iluminate.p
                }
            bPawns.append(bPawn)
        if col == 'r':
            wRook = {
                'pos': (x,y),
                'rect': pygame.Rect(x,y,64,64),
                'image': pygame.image.load('wRook.png'),
                'col': 'w',
                'piece': 'rC',
                'ilu': iluminate.r
                }
            wRooks.append(wRook)
        if col == 'n':
            wKnight = {
                'pos': (x,y),
                'rect': pygame.Rect(x,y,64,64),
                'image': pygame.image.load('wKnight.png'),
                'col': 'w',
                'piece': 'kn',
                'ilu': iluminate.kn
                }
            wKnights.append(wKnight)
        if col == 'b':
            wBishop = {
                'pos': (x,y),
                'rect': pygame.Rect(x,y,64,64),
                'image': pygame.image.load('wBishop.png'),
                'col': 'w',
                'piece': 'b',
                'ilu': iluminate.b
                }
            wBishops.append(wBishop)
        if col == 'q':
            wQueen = {
                'pos': (x,y),
                'rect': pygame.Rect(x,y,64,64),
                'image': pygame.image.load('wQueen.png'),
                'col': 'w',
                'piece': 'q',
                'ilu': iluminate.q
                }
            wQueens.append(wQueen)
        if col == 'k':
            wKing = {
                'pos': (x,y),
                'rect': pygame.Rect(x,y,64,64),
                'image': pygame.image.load('wKing.png'),
                'col': 'w',
                'piece': 'kC',
                'ilu': iluminate.k
                }
            wKings.append(wKing)
        if col == 'p':
            wPawn = {
                'pos': (x,y),
                'rect': pygame.Rect(x,y,64,64),
                'image': pygame.image.load('wPawn.png'),
                'col': 'w',
                'piece': 'pU',
                'ilu': iluminate.p
                }
            wPawns.append(wPawn)
        if col == '#':
            empty = {
                'pos': (x,y),
                'rect': pygame.Rect(x,y,64,64),
                'image': pygame.image.load('empty.png'),
                'col': ' ',
                'piece': ' ',
                'ilu': None
                }
            emptys.append(empty)
        x=x+64
    y=y+64
    x=0
           
piecesL = [bRooks,bKnights,bBishops,bQueens,bKings,bPawns,wRooks,wKnights,wBishops,wQueens,wKings,wPawns,emptys]

qImg = ['wQueen.png','bQueen.png']
rImg = ['wRook.png','bRook.png']
knImg = ['wKnight.png','bKnight.png']
bImg = ['wBishop.png','bBishop.png']

queenB = pygame.Rect(160,160,64,64)
rookB = pygame.Rect(160,288,64,64)
knightB = pygame.Rect(288,160,64,64)
bishopB = pygame.Rect(288,288,64,64)
bPos = [(160,160,64,64),(160,288,64,64),(288,160,64,64),(288,288,64,64)]
colour = [(123,6,98),(123,6,98),(123,6,98),(123,6,98)]
font = pygame.font.SysFont('Ariel',69)
wind = ' '
winTxt = font.render(wind+' wins!!!!', False, (222,49,99))


check = [False,False]
idktempnum = 0
clickNum = 0
checked = begin = False
A = B =  None
piece = None
isCastle = False
promote = False
clock = pygame.time.Clock()
gameRun = True
state = 'main'
while gameRun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRun = False

    pygame.display.set_caption(go)
    
    dt = clock.tick(30)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        gameRun = False

    ############Win the game
    if state == 'win':
        winTxt = font.render(wind+' wins!!!!', False, (222,49,99))
        

    ############Promote pawn
    if state == 'promote':
        if go == 'w':
            idktempnum = 0
        else:
            idktempnum = 1

        if queenB.collidepoint(pygame.mouse.get_pos()):
            colour[0] = (45,250,146)
            if pygame.mouse.get_pressed()[0]:
                state = 'main'
                metamorph = [pygame.image.load(qImg[idktempnum]),'q']
        else:
            colour[0] = (123,6,98)

        if rookB.collidepoint(pygame.mouse.get_pos()):
            colour[1] = (45,250,146)
            if pygame.mouse.get_pressed()[0]:
                state = 'main'
                metamorph = [pygame.image.load(rImg[idktempnum]),'r']
        else:
            colour[1] = (123,6,98)

        if knightB.collidepoint(pygame.mouse.get_pos()):
            colour[2] = (45,250,146)
            if pygame.mouse.get_pressed()[0]:
                state = 'main'
                metamorph = [pygame.image.load(knImg[idktempnum]),'kn']
        else:
            colour[2] = (123,6,98)

        if bishopB.collidepoint(pygame.mouse.get_pos()):
            colour[3] = (45,250,146)
            if pygame.mouse.get_pressed()[0]:
                state = 'main'
                metamorph = [pygame.image.load(bImg[idktempnum]),'b']
        else:
            colour[3] = (123,6,98)
            
        

    #########Main
    if state == 'main':

        if go == 'w':
            goNum = 0
        else:
            goNum = 1

        if clickNum > 1:
            begin = True
            #print('start')

        if keys[pygame.K_BACKSPACE] and not begin:
            clickNum = 0
            move = [None,None]
            checked = False
            print('Move reset.')

        if not promote:
            valid = True
            
            for i in range(0,len(piecesL)):
                for e in range(0,len(piecesL[i])):
                    block = piecesL[i][e]
                    if block['rect'].collidepoint(pygame.mouse.get_pos()):
                        if pygame.mouse.get_pressed()[0] and pygame.time.get_ticks() - lastClick > 300:
                            if clickNum < 2:
                                start = block['pos']
                                move[clickNum] = [int(start[0]),int(start[1])]
                                for u in range(0,2):
                                    move[clickNum][u] = int(move[clickNum][u]/64)
                                if clickNum == 1:
                                    if move[0] == move[1]:
                                        move[1] = None
                                        print('cant move to where it already is.')
                                        clickNum -= 1
                                    elif block['col'] == A['col'] and A['piece'] != 'kC':
                                        move[1] = None
                                        print('cant move where anouther of your pieces are.')
                                        clickNum -= 1
                                    else:
                                        print(move[clickNum])
                                        B = block
                                    if block['piece'] == 'rC' and A['piece'] == 'kC' and block['col'] == A['col'] and not check[goNum]:
                                        isCastle = True
                                    elif block['col'] == A['col'] and A['piece'] == 'kC':
                                        move[1] = None
                                        print('cant move where another of your pieces are.')
                                        clickNum -= 1
                                        
                                elif clickNum == 0:
                                    if block['col'] != go:
                                        move[0] = None
                                        print('Not your piece')
                                        clickNum -= 1
                                    else:
                                        print(move[clickNum])
                                        piece = block['piece']
                                        #print(piece + 'selet')
                                        A = block
                                clickNum += 1
                            else:
                                print(move)
                            lastClick = pygame.time.get_ticks()



            if clickNum == 1 and not checked:
                rectPos = []
                rectPos = A['ilu'](A['pos'],A['col'],A['piece'],board,False)
                newRects = newRectinator(rectPos)
                
                

        if begin:
            if not promote:
                #print(piece , 'begin')
                play(piece,move,A,B,board)
            if state == 'main' or state == 'win':
                if valid:
                    board = listPlay(move,board)
                    pyPlay()
                        


                print(check)
                isCastle = False       
                checked = begin = False
                clickNum = 0
                move = [None,None]
                #check = [False,False]
                promote = False
                A = B = False
                for i in range (0,8):
                    print(board[i])




    screen.blit(bg,(0,0))
    for i in range(0,len(piecesL)):
        for e in range(0,len(piecesL[i])):
            name = piecesL[i][e]
            screen.blit(name['image'],name['rect'])
    if state == 'promote':
        pygame.draw.rect(screen,(123,6,98),(128,128,256,256))
        for i in range(0,4):
            pygame.draw.rect(screen,colour[i],bPos[i])
            pygame.draw.rect(screen,(0,0,0),bPos[i],1)

        screen.blit(pygame.image.load(qImg[idktempnum]),queenB)
        screen.blit(pygame.image.load(rImg[idktempnum]),rookB)
        screen.blit(pygame.image.load(bImg[idktempnum]),bishopB)
        screen.blit(pygame.image.load(knImg[idktempnum]),knightB)
    if clickNum == 1:
        for i in range(0,len(newRects)):
            screen.blit(green,newRects[i])
    if state == 'win':
        screen.blit(winTxt,(120,230))
        

    

    pygame.display.flip()


pygame.quit()
