def intro():
    print("Hello! Welcome to Tic Tac Toe game!")
    print("\n")
    print("Rules: Player 1 and player 2, represented by X and O, take turns "
          "marking the spaces in a 3*3 grid. The player who succeeds in placing "
          "three of their marks in a horizontal, vertical, or diagonal row wins.")
    print("\n")
    input("Press any Enter to continue.")
    print("\n")
def designing_board():
    print('Here is the playboard: ')
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]        
    return board

def symbols():
    symbol_1 = input('Player 1,Choose Please  X or O? ')
    if symbol_1 == 'X':
        symbol_2 = 'O'
        print('Player 2, you are : ', symbol_2 )
    else:
        symbol_2 = 'X'
        print('Player 2, you are ', symbol_2 )
    input('Press enter to continue.')
    print('\n')
    return (symbol_1, symbol_2)

def starting(board,symbol_1,symbol_2,count):
    if count % 2 == 0:
        player = symbol_1
    elif count % 2 == 1:
        player = symbol_2
    print('player : ',player,' is your turn')
    row = int(input('Pick a row[upper row:'
                        '[enter 0, middle row: enter 1, bottom row: enter 2]:'))
    column = int(input('Pick a column:'
                           '[left column: enter 0, middle column: enter 1, right column enter 2]'))
    while (row > 2 or row < 0) or (column > 2 or column < 0):
        outOfBoard(row, column)
        row = int(input('Pick a row[upper row:'
                        '[enter 0, middle row: enter 1, bottom row: enter 2]:'))
        column = int(input('Pick a column:'
                           '[left column: enter 0, middle column: enter 1, right column enter 2]'))

        # Check if the square is already filled
    while (board[row][column] == symbol_1)or (board[row][column] == symbol_2):
        filled = illegal(board, symbol_1, symbol_2, row, column)
        row = int(input('Pick a row[upper row:'
                        '[enter 0, middle row: enter 1, bottom row: enter 2]:'))
        column = int(input('Pick a column:'
                           '[left column: enter 0, middle column: enter 1, right column enter 2]'))    
        
    # Locates player's symbol on the board
    if player == symbol_1:
        board[row][column] = symbol_1
            
    else:
        board[row][column] = symbol_2
    
    return (board)

def isFull(board, symbol_1, symbol_2):
    count = 1
    winner = True
    while count < 10 and winner == True:
        gaming = starting(board, symbol_1, symbol_2, count)
        shape = printshape(board)
        
        if count == 9:
            print('The board is full. Game over.')
            if winner == True:
                print('There is a tie.' )

        # Check if here is a winner
        winner = isWinner(board, symbol_1, symbol_2, count)
        count += 1
    if winner == False:
        print('Game over.') 
   
    report(count, winner, symbol_1, symbol_2)
    
def outOfBoard(row, column):
    print("Out of boarder. Pick another one. ")
    
def printshape(board):
    rows = len(board)
    cols = len(board)
    print("---+---+---")
    for r in range(rows):
        print(board[r][0], " |", board[r][1], "|", board[r][2])
        print("---+---+---")
    return board
def isWinner(board, symbol_1, symbol_2, count):
    winner = True
   
    for row in range (0, 3):
        if (board[row][0] == board[row][1] == board[row][2] == symbol_1):
            winner = False
            print('Player'  + symbol_1 + ' , you won!')
   
        elif (board[row][0] == board[row][1] == board[row][2] == symbol_2):
            winner = False
            print('Player  ' + symbol_2 + ' , you won!')
            
            
    # Check the columns
    for col in range (0, 3):
        if (board[0][col] == board[1][col] == board[2][col] == symbol_1):
            winner = False
            print('Player '  + symbol_1 + ' , you won!')
        elif (board[0][col] == board[1][col] == board[2][col] == symbol_2):
            winner = False
            print('Player  ' + symbol_2 + ' , you won!')

 # Check the diagnoals
    if board[0][0] == board[1][1] == board[2][2] == symbol_1:
        winner = False 
        print('Player '  + symbol_1 + ' , you won!')

    elif board[0][0] == board[1][1] == board[2][2] == symbol_2:
        winner = False
        print('Player  ' + symbol_2 + ' , you won!')

    elif board[0][2] == board[1][1] == board[2][0] == symbol_1:
        winner = False
        print('Player '  + symbol_1 + ' , you won!')

    elif board[0][2] == board[1][1] == board[2][0] == symbol_2:
        winner = False
        print('Player  ' + symbol_2 + ' , you won!')

    return winner

def illegal(board, symbol_1, symbol_2, row, column):
    print('The square you picked is already filled. Pick another one.')
def report(count, winner, symbol_1, symbol_2):
    print('\n')
    input('Press enter to see the game summary. ')
    if (winner == False) and (count % 2 == 1 ):
        print('Winner : Player  '+ symbol_1 + '.')
    elif (winner == False) and (count % 2 == 0 ):
        print('Winner : Player ' + symbol_2 + '.')
    else:
        print('There is a tie. ')
introduction = intro()
board = designing_board()
shape = printshape(board)
symbol_1, symbol_2 = symbols()
full = isFull(board, symbol_1, symbol_2) 
