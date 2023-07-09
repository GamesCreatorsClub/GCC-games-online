

import pygame,time

move2 = None

def play(piece,move,A,B,board):
    global go
    if piece == 'rC' or piece == 'r':
        rook.moveCheck(move,piece)
        print(valid)
        print('rook')
        if valid:
            A['piece'] = 'r'
    elif piece == 'kn':
        print('knight')
    elif piece == 'b':
        print('bishop')
    elif piece == 'q':
        print('queen')
    elif piece == 'kC' or piece == 'k':
        king.moveCheck(move,piece)
        print(valid)
        print('king')
        if valid:
            A['piece'] = 'k'
    elif piece == 'pU' or piece == 'p':
        pawn.moveCheck(move,piece)
        print('pawn')
        print(valid)
        if valid:
            A['piece'] = 'p'


    

def listPlay(move):
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
        board[rowE][columnE] = board[rowF][columnF]
        board[rowF][columnF] = ' '
    else:
        board[rowE][columnE] = board[rowF][columnF]
        board[rowF][columnF] = ' '
        board[row2E][column2E] = board[row2F][column2F]
        board[row2F][column2F] = ' '
        
    if go == 'w':
        go = 'b'
    else:
        go = 'w'

def pyPlay():
    if not isCastle:
        changesA = [A['image'],A['col'],A['piece']]
        B['image'] = changesA[0]
        B['col'] = changesA[1]
        B['piece'] = changesA[2]
        A['image'] = pygame.image.load('empty.png') 
        A['col'] = ' '
        A['piece'] = ' '
    else:
        B['piece'] = 'r'
        posCheck = (move[1][0] *64 , move[1][1] *64)
        posCheck2 = (move2[1][0] *64 , move2[1][1] *64)
        print(posCheck)
        print(posCheck2)
        for i in range(0,len(piecesL)):
            for e in range(0,len(piecesL[i])):
                if piecesL[i][e]['pos'] == posCheck:
                    a = piecesL[i][e]
                    print('worked')
                elif piecesL[i][e]['pos'] == posCheck2:
                    b = piecesL[i][e]
                    print('worked2')
        changesA = [A['image'],A['col'],A['piece']]
        a['image'] = changesA[0]
        a['col'] = changesA[1]
        a['piece'] = changesA[2]
        A['image'] = pygame.image.load('empty.png') 
        A['col'] = ' '
        A['piece'] = ' '

        changesB = [B['image'],B['col'],B['piece']]
        b['image'] = changesB[0]
        b['col'] = changesB[1]
        b['piece'] = changesB[2]
        B['image'] = pygame.image.load('empty.png') 
        B['col'] = ' '
        B['piece'] = ' '


###############################################
class king:
    def __init__(self,move,col):
        self.move = move
        self.col = col

    def moveCheck(move,piece):
        
        rowF = move[0][-1]
        columnF = move[0][0]
        rowE = move[-1][-1]
        columnE = move[-1][0]

        global valid,move2
        
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
        
        def makeRange(f,t,inc):
            print(f,t,inc)
            return range(f-1,t,inc) if inc < 0 else range(f+1,t,inc)
        
        global valid
        
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

        global valid,promote,state
        
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
            
                
            
        
    
#############################################################
'''
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

board = [['rb',' ',' ',' ','kb',' ','nb','rb'],#8
         [' ','pw','pb',' ','pb','pb','pb','pb'],#7
         [' ',' ',' ',' ',' ',' ',' ',' '],#6
         [' ',' ',' ',' ',' ',' ',' ',' '],#5
         [' ',' ',' ',' ',' ',' ',' ',' '],#4
         [' ',' ',' ',' ',' ',' ',' ',' '],#3
         ['pw','','pw','pw','pw','pw','pw',' '],#2
         ['rw',' ',' ','qw','kw',' ',' ','rw']]#1
#           a     b    c   d    e   f      g    h

go = 'w'
sinceClick = -500
move = [None,None]


for i in range (0,8):
    print(board[i])


pygame.init()
screen = pygame.display.set_mode((512,512))

bg = pygame.image.load('board.png')


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


boardPy = ['o###g#io'
          ,'#pa#aaaa'
          ,'########'
          ,'########'
          ,'########'
          ,'########'
          ,'p#ppppp#'
          ,'r##qk##r'
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
'''
x=y=0
for row in boardPy:
    for col in row:
        if col == 'o':
            bRook = {
                'pos': (x,y),
                'rect': pygame.Rect(x,y,64,64),
                'image': pygame.image.load('bRook.png'),
                'col': 'b',
                'piece': 'rC'
                }
            bRooks.append(bRook)
        if col == 'i':
            bKnight = {
                'pos': (x,y),
                'rect': pygame.Rect(x,y,64,64),
                'image': pygame.image.load('bKnight.png'),
                'col': 'b',
                'piece': 'kn'
                }
            bKnights.append(bKnight)
        if col == 's':
            bBishop = {
                'pos': (x,y),
                'rect': pygame.Rect(x,y,64,64),
                'image': pygame.image.load('bBishop.png'),
                'col': 'b',
                'piece': 'b'
                }
            bBishops.append(bBishop)
        if col == 'u':
            bQueen = {
                'pos': (x,y),
                'rect': pygame.Rect(x,y,64,64),
                'image': pygame.image.load('bQueen.png'),
                'col': 'b',
                'piece': 'q'
                }
            bQueens.append(bQueen)
        if col == 'g':
            bKing = {
                'pos': (x,y),
                'rect': pygame.Rect(x,y,64,64),
                'image': pygame.image.load('bKing.png'),
                'col': 'b',
                'piece': 'kC'
                }
            bKings.append(bKing)
        if col == 'a':
            bPawn = {
                'pos': (x,y),
                'rect': pygame.Rect(x,y,64,64),
                'image': pygame.image.load('bPawn.png'),
                'col': 'b',
                'piece': 'pU'
                }
            bPawns.append(bPawn)
        if col == 'r':
            wRook = {
                'pos': (x,y),
                'rect': pygame.Rect(x,y,64,64),
                'image': pygame.image.load('wRook.png'),
                'col': 'w',
                'piece': 'rC'
                }
            wRooks.append(wRook)
        if col == 'n':
            wKnight = {
                'pos': (x,y),
                'rect': pygame.Rect(x,y,64,64),
                'image': pygame.image.load('wKnight.png'),
                'col': 'w',
                'piece': 'kn'
                }
            wKnights.append(wKnight)
        if col == 'b':
            wBishop = {
                'pos': (x,y),
                'rect': pygame.Rect(x,y,64,64),
                'image': pygame.image.load('wBishop.png'),
                'col': 'w',
                'piece': 'b'
                }
            wBishops.append(wBishop)
        if col == 'q':
            wQueen = {
                'pos': (x,y),
                'rect': pygame.Rect(x,y,64,64),
                'image': pygame.image.load('wQueen.png'),
                'col': 'w',
                'piece': 'q'
                }
            wQueens.append(wQueen)
        if col == 'k':
            wKing = {
                'pos': (x,y),
                'rect': pygame.Rect(x,y,64,64),
                'image': pygame.image.load('wKing.png'),
                'col': 'w',
                'piece': 'kC'
                }
            wKings.append(wKing)
        if col == 'p':
            wPawn = {
                'pos': (x,y),
                'rect': pygame.Rect(x,y,64,64),
                'image': pygame.image.load('wPawn.png'),
                'col': 'w',
                'piece': 'pU'
                }
            wPawns.append(wPawn)
        if col == '#':
            empty = {
                'pos': (x,y),
                'rect': pygame.Rect(x,y,64,64),
                'image': pygame.image.load('empty.png'),
                'col': ' ',
                'piece': ' '
                }
            emptys.append(empty)
        x=x+64
    y=y+64
    x=0
           
piecesL = [bRooks,bKnights,bBishops,bQueens,bKings,bPawns,wRooks,wKnights,wBishops,wQueens,wKings,wPawns,emptys]


queenB = pygame.Rect(160,160,64,64)
rookB = pygame.Rect(160,288,64,64)
knightB = pygame.Rect(288,160,64,64)
bishopB = pygame.Rect(288,288,64,64)
bPos = [(160,160,64,64),(160,288,64,64),(288,160,64,64),(288,288,64,64)]
colour = [(123,6,98),(123,6,98),(123,6,98),(123,6,98)]



clickNum = 0
begin = False
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

    dt = clock.tick(30)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        gameRun = False

    ############Promote pawn
    if state == 'promote':

        if queenB.collidepoint(pygame.mouse.get_pos()):
            colour[0] = (45,250,146)
            if pygame.mouse.get_pressed()[0]:
                state = 'main'
                metamorph = [pygame.image.load('bQueen.png'),'q']
        else:
            colour[0] = (123,6,98)

        if rookB.collidepoint(pygame.mouse.get_pos()):
            colour[1] = (45,250,146)
            if pygame.mouse.get_pressed()[0]:
                state = 'main'
        else:
            colour[1] = (123,6,98)

        if knightB.collidepoint(pygame.mouse.get_pos()):
            colour[2] = (45,250,146)
            if pygame.mouse.get_pressed()[0]:
                state = 'main'
        else:
            colour[2] = (123,6,98)

        if bishopB.collidepoint(pygame.mouse.get_pos()):
            colour[3] = (45,250,146)
            if pygame.mouse.get_pressed()[0]:
                state = 'main'
        else:
            colour[3] = (123,6,98)
            
        

    #########Main
    if state == 'main':

        if keys[pygame.K_SPACE] and clickNum > 1:
            begin = True
            print('start')

        if keys[pygame.K_BACKSPACE] and not begin:
            clickNum = 0
            move = [None,None]
            print(move,clickNum)

        if not promote:
            valid = True
            
            for i in range(0,len(piecesL)):
                for e in range(0,len(piecesL[i])):
                    block = piecesL[i][e]
                    if block['rect'].collidepoint(pygame.mouse.get_pos()):
                        if pygame.mouse.get_pressed()[0] and pygame.time.get_ticks() - sinceClick > 500:
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
                                    if block['piece'] == 'rC' and A['piece'] == 'kC' and block['col'] == A['col']:
                                        isCastle = True
                                    elif block['col'] == A['col'] and A['piece'] == 'kC':
                                        move[1] = None
                                        print('cant move where anouther of your pieces are.')
                                        clickNum -= 1
                                        
                                elif clickNum == 0:
                                    if block['col'] != go:
                                        move[0] = None
                                        print('Not your piece')
                                        clickNum -= 1
                                    else:
                                        print(move[clickNum])
                                        piece = block['piece']
                                        print(piece + 'selet')
                                        A = block
                                clickNum += 1
                            else:
                                print(move)
                            sinceClick = pygame.time.get_ticks()

        if begin:
            if not promote:
                print(piece , 'begin')
                play(piece,move,A,B,board)
            if state == 'main':
                if valid:
                    listPlay(move)
                    pyPlay()

                isCastle = False       
                begin = False
                clickNum = 0
                move = [None,None]
                promote = False
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

        screen.blit(pygame.image.load('bQueen.png'),queenB)
        screen.blit(pygame.image.load('bRook.png'),rookB)
        screen.blit(pygame.image.load('bBishop.png'),bishopB)
        screen.blit(pygame.image.load('bKnight.png'),knightB)
        

    

    pygame.display.flip()


pygame.quit()
