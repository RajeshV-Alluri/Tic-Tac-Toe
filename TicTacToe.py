''' Program To Run Tic-Tac-Toe '''

''' Global Variables '''
Board = [
    '-','-','-',
    '-','-','-',
    '-','-','-'
]

position = [1, 2, 3, 4, 5, 6, 7, 8, 9]

Turn = 'X'

''' Function to display Board '''
def DisplayBoard():
    print("\n")
    print(Board[0] , ' | ' , Board[1] , ' | ' , Board[2] , "    1 | 2 | 3")
    print(Board[3] , ' | ' , Board[4] , ' | ' , Board[5] , "    4 | 5 | 6")
    print(Board[6] , ' | ' , Board[7] , ' | ' , Board[8] , "    7 | 8 | 9")
    print("\n")

'''Function to take Input'''
def TakeInput():
    while(True):
        try:
            choice = int(input("Enter the number:"))
            if choice < 1 or choice > 9:
                print("Enter numbers between 0-9 only")
            break
        except:
            print("Enter valid input")
    return choice

''' Function to insert Player's input on Board'''
def UserInput():
    global Turn
    replace = TakeInput()
    if replace not in position:
        print("Position taken, Enter any other number!")
    else:
        Board[replace - 1] = Turn
        position.remove(replace)
        if Turn == 'X':
            Turn = 'O'
        else:
            Turn = 'X'

''' Function to check Win condition '''
def CheckWin():

    if (
            # Checking Rows
            Board[0] == Board[1] == Board[2] == 'X'
            or Board[3] == Board[4] == Board[5] == 'X'
            or Board[6] == Board[7] == Board[8] == 'X'
            # Checking Columns
            or Board[0] == Board[3] == Board[6] == 'X'
            or Board[1] == Board[4] == Board[7] == 'X'
            or Board[2] == Board[5] == Board[8] == 'X'
            # Checking Diagonals
            or Board[0] == Board[4] == Board[8] == 'X'
            or Board[2] == Board[4] == Board[6] == 'X'
    ):
        print ("Player 'X' Won")
        quit()

    elif (
            # Checking Rows
            Board[0] == Board[1] == Board[2] == 'O'
            or Board[3] == Board[4] == Board[5] == 'O'
            or Board[6] == Board[7] == Board[8] == 'O'
            # Checking Columns
            or Board[0] == Board[3] == Board[6] == 'O'
            or Board[1] == Board[4] == Board[7] == 'O'
            or Board[2] == Board[5] == Board[8] == 'O'
            # Checking Diagonals
            or Board[0] == Board[4] == Board[8] == 'O'
            or Board[2] == Board[4] == Board[6] == 'O'
    ):
        print ("Player 'O' Won")
        quit()

''' Function to check Tie condition '''
def CheckTie():
    if (
            Board[0] != '-' and Board[1] != '-' and Board[2] != '-' and
            Board[3] != '-' and Board[4] != '-' and Board[5] != '-' and
            Board[6] != '-' and Board[7] != '-' and Board[8] != '-'
    ):
        print("Tie Game")
        quit()

''' Function to play the game '''
def PlayGame():
    DisplayBoard()
    while(True):
        UserInput()
        DisplayBoard()
        CheckWin()
        CheckTie()

PlayGame()
