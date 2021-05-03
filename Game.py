board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']

def display():
    j = 0
    for i in board:
        if j not in (2,5,8):
            print(i+" | ",end=" ")
            j+=1
        else:
            print(i+'\n' + 2 * "--+--" + "--+" + '\n', end="")
            j+=1
display()

def checkwin(player):
    global board
    playerwins=0
    for i in range(7):
        if board[i+1]==board[i+2]==board[i]:
            if board[i]!=' ':
                print(player,"has won!")
                playerwins+=1
    for i in range(2):
        if board[i+3]==board[i+6]==board[i]:
            if board[i]!=' ':
                print(player,"has won!")
                playerwins += 1
    if board[0]==board[4]==board[8]:
        if board[i] != ' ':
            print(player, "has won!")
            playerwins += 1
    if board[2] == board[4] == board[6]:
        if board[i] != ' ':
            print(player, "has won!")
            playerwins += 1
    if playerwins==1:
        board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']



def playo():
    play=int(input("Input Box No. To Play (O): "))
    if board[play - 1] == " ":
        board[play-1]='O'
        display()
        checkwin('O')
        playx()
    else:
        print("Already Taken! Try another box")
        playo()


def playx():
    play=int(input("Input Box No. To Play (X): "))
    if board[play-1]==" ":
        board[play-1]='X'
        display()
        checkwin('X')
        playo()
    else:
        print("Already Taken! Try another box")
        playx()



playx()