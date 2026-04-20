theBoard = {1: " ", 2: " ", 3 : " ", 4: " ", 5: " ", 6: " ", 7 : " ", 8: " ", 9: " "}                       # this dictionary defines the tic tac toe board
winningConditions = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]                # this list defines the winning conditions

def printBoard(board) :                                                                             # this functions prints the board
    print(board[1],"|",board[2],"|",board[3])
    print("--+---+--")
    print(board[4],"|",board[5],"|",board[6])
    print("--+---+--")
    print(board[7],"|",board[8],"|",board[9])

def checkWin(board) :                                                                               # this functions check the winner 
    for conditions in winningConditions:                                                            # for every winning conditions defined in 2nd line
        a, b, c = conditions

        if board[a] == board[b] == board[c] != ' ':
            return board[a]                                                                         # if someone is winner then return that person or none
    
    return None


turn = 'X'                                                                          # varaible to manage turns
validMoves = 0                                                                      # varaible to count valid moves for draw conditions and much more
while True:
    printBoard(theBoard)
    
    print("Turn for", turn, "Move on which space? (numbers only)" )
    
    try:                                                                            # exception handeling: if someone enter other than number
        move = int(input())
    except:
        print("enter a valid number!")
        continue

    if move not in range(1,10):                                                     # check if the number is in range
        print("enter a value between 1 and 9")
        continue

    if theBoard[move] != " ":                                                       # check if the space is already filled or not
        print("The Space is already filled, choose another space!")
        continue

    theBoard[move] = turn                                                           # if all the above conditions are valid then we place a move to that space
    validMoves += 1                                                                 # and increament the counter

    if validMoves >= 5:                                                             # check the winner after 5th move, cause its not possible to calculate win under 5 move
        winner = checkWin(theBoard)
        if winner:
            print(winner ,"won the game!")                                          # if winner exists return him and end the game
            break

    if validMoves == 9:                                                             # if the player runs out of space to play we draw the game
        print("The game is Draw")
        break

    if turn == 'X':                                                                 # update turn after each move
        turn = 'O'
    else : 
        turn = 'X'

printBoard(theBoard)                                                                # print board in the end