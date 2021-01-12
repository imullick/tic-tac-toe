# Python code for Tic Tac Toe by @imullick. Enjoy!
print("~ LETS PLAY WILD TIC TAC TOE ~" + 
"\nThe rules are simple, you have to get three in a row, \nbut you're allowed to choose "+
"whether you want to play 'X' or 'O' on each turn!!!\nThe person to place the winning 'X' or 'O' wins! " +
"\nLet's get started :)")

# Dictionary to store board and keys
gameBoard = {'1': ' ' , '2': ' ' , '3': ' ' ,
        '4': ' ' , '5': ' ' , '6': ' ' ,
        '7': ' ' , '8': ' ' , '9': ' ' }

# List of keys
boardKeys = []

for key in gameBoard:
    boardKeys.append(key)

# Printing board
def printBoard(board):
    print('\n')
    print('     ' + board['1'] + ' ' + '|' + ' ' + board['2'] + ' ' +  '|' + ' ' + board['3'])
    print('    ---+---+---')
    print('     ' + board['4'] + ' ' + '|' + ' ' + board['5'] + ' ' +  '|' + ' ' + board['6'])
    print('    ---+---+---')
    print('     ' + board['7'] + ' ' + '|' + ' ' + board['8'] + ' ' +  '|' + ' ' + board['9'])
    print('\n')

def getTurn():
    print("\nWho do you want to play as? Enter 'X' or 'O'. ")
    turn= input()
    if turn=='X' or turn=='x':
        return 'X'
    elif turn=='O' or turn=='o':
        return 'O'
    else:
        print("Enter either 'X' or 'O'")
        return getTurn()
 
def game():
    
    # Dictionary to store board and keys
    gameBoard = {'1': ' ' , '2': ' ' , '3': ' ' ,
                '4': ' ' , '5': ' ' , '6': ' ' ,
                '7': ' ' , '8': ' ' , '9': ' ' }
            
    count=0
    
    for i in range(9):
        printBoard(gameBoard)
        turn = getTurn()
        
        print("{}'s turn. Enter position: ".format(turn))
        move=input()
        if (ord(move)<49 or ord(move)>57): # ord converts character to its ASCII value. 
            print('Invalid. Enter a position from 1 to 9. Try again.\n')
            continue
        if gameBoard[move] == ' ':
            gameBoard[move] = turn
            count += 1
            
        else:
            print("That place is already filled. Try again.\n")
            continue
        
        if (count>=5):
            if(gameBoard['1']==gameBoard['2']==gameBoard['3']!=' '):
                printBoard(gameBoard)
                print('---GAME OVER---\n' + gameBoard['1'] + ' wins!')
                playagain()
            elif(gameBoard['4']==gameBoard['5']==gameBoard['6']!=' '):
                printBoard(gameBoard)
                print('---GAME OVER---\n' + gameBoard['4'] + ' wins!')
                playagain()
            elif(gameBoard['7']==gameBoard['8']==gameBoard['9']!=' '):
                printBoard(gameBoard)
                print('---GAME OVER---\n' + gameBoard['7'] + ' wins!')
                playagain()
            elif(gameBoard['1']==gameBoard['4']==gameBoard['7']!=' '):
                printBoard(gameBoard)
                print('---GAME OVER---\n' + gameBoard['1'] + ' wins!')
                playagain()
            elif(gameBoard['2']==gameBoard['5']==gameBoard['8']!=' '):
                printBoard(gameBoard)
                print('---GAME OVER---\n' + gameBoard['2'] + ' wins!')
                playagain()
            elif(gameBoard['3']==gameBoard['6']==gameBoard['9']!=' '):
                printBoard(gameBoard)
                print('---GAME OVER---\n' + gameBoard['3'] + ' wins!')
                playagain()
            elif(gameBoard['1']==gameBoard['5']==gameBoard['9']!=' '):
                printBoard(gameBoard)
                print('---GAME OVER---\n' + gameBoard['1'] + ' wins!')
                playagain()
            elif(gameBoard['3']==gameBoard['5']==gameBoard['7']!=' '):
                printBoard(gameBoard)
                print('---GAME OVER---\n' + gameBoard['3'] + ' wins!')
                playagain()

            if(count==9):
                print('---GAME OVER---\n' + 'Its a TIE!')
                playagain()

def playagain():
    print('Do you want to play again? Y/N')
    choice=input()
    if choice=='y' or choice=='Y':
        game()
    else:
        print('Thank you for playing! Have a nice day!')
        exit()
        
game()
