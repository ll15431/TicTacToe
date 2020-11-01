from random import randrange

cols = 3
rows = 3
board = [['0' for i in range(rows)] for j in range(cols)]
Freespace = []
sign = ['X','O']

def InitiateBoard(board):
    num = 0
    for i in range(rows):
        for j in range(cols):
            board[i][j] = (num + 1)
            num += 1
 
 
 
 
def DisplayBoard(board):
        
    for row in board:
        print('+-------+-------+-------+')
        print('|       |       |       |')
        print('|   %s   |' % '   |   '.join(map(str, row)))
        print('|       |       |       |')
    print('+-------+-------+-------+')





def EnterMove(board):
    valid = False
    MakeListOfFreeFields(board)
    while valid == False:
        
        Move = int(input('Please choose a number (1-9): '))
        valid = True
        
        if Move not in range(1,10):
            valid = False
            print ('Choice out of range')
            
        elif Move not in Freespace:
            valid = False
            print ('This spot is already taken')

        else:
            for i in range(rows):
                for j in range(cols):
                    if board[i][j] == Move:
                        board[i][j] = 'O'
                    else:
                        continue
    Freespace.clear()


def MakeListOfFreeFields(board):
    one2nine = list(range(1,10))
    for i in range(rows):
        for j in range(cols):
            if board[i][j] in one2nine:
                Freespace.append(board[i][j])
            else:
                continue
    return Freespace

    

def DrawMove(board):
    MakeListOfFreeFields(board)
    valid = False
    while valid == False:
        valid = True
        compMove = randrange(10)
        if compMove in Freespace:
            for i in range(rows):
                for j in range(cols):
                    if board[i][j] == compMove:
                        board[i][j] = 'X'
                    else:
                        continue
        else:
            valid = False
    Freespace.clear()        

            

def VictoryFor(board,sign):
    win = []
    turn = 0
    valid = False
    while valid == False:
        i = 0
        j = 0
        o = 0
        x = 0
        valid = True
        DisplayBoard(board)
        while i < 3:
            for j in range(cols):
                win.append(board[i][j])
            for l in range(3):
                if win[l] == 'O':
                    o += 1
                elif win[l] == 'X':
                    x += 1
                else:
                    continue
            if o == 3:
                print('Player Victory!!')
                return board
            elif x == 3:
                print('Computer Victory!!')
                return board
            else:
                o = 0
                x = 0
                i +=1
                win.clear()
        
        i = 0
        j = 0
        while j < 3:
            for i in range(rows):
                win.append(board[i][j])
            for l in range(3):
                if win[l] == 'O':
                    o += 1
                elif win[l] == 'X':
                    x += 1
                else:
                    continue
            if o == 3:
                print('Player Victory!!')
                return board
            elif x == 3:
                print('Computer Victory!!')
                return board
            else:
                o = 0
                x = 0
                j +=1
                win.clear()
        
        i = 0
        j = 0
        o = 0
        x = 0
        while j < 3:
            win.append(board[i][j])
            i +=1
            j+=1
        for l in range(3):
            if win[l] == 'O':
                o += 1
            elif win[l] == 'X':
                x += 1
            else:
                continue
            
        if o == 3:
            print('Player Victory!!')
            return board
        elif x == 3:
            print('Computer Victory!!')
            return board
        else:
            o = 0
            x = 0
            win.clear()
            
            
            ######
        i = 2
        j = 0
        o = 0
        x = 0
        while j < 3:
            win.append(board[i][j])
            i -=1
            j+=1
        for l in range(3):
            if win[l] == 'O':
                o += 1
            elif win[l] == 'X':
                x += 1
            else:
                continue
            
        if o == 3:
            print('Player Victory!!')
            return board
        elif x == 3:
            print('Computer Victory!!')
            return board
        else:
            o = 0
            x = 0
            win.clear()
            
        ########## 
            
        if turn <= 8:
            print ('Turn number: ',turn)
            if turn % 2 == 0:
                DrawMove(board)
                turn += 1
                valid = False
            else:
                EnterMove(board)
                turn += 1
                valid = False
                
        else:
            print('The game is a draw!')
            break
            
        
        
        

InitiateBoard(board)
VictoryFor(board,sign)



