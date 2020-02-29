#.................global variables..............
game_not_over = True
win = None
game = 0
player_turn = "x"

#main defined board
board=  ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

def game_board():
    print(board[0] + "|" + board[1] + "|" + board[2] + "|")
    print(board[3] + "|" + board[4] + "|" + board[5] + "|")
    print(board[6] + "|" + board[7] + "|" + board[8] + "|")

game_board()

def play_game():
     global game_not_over , player_turn
    
        
     while  game_not_over :
         position_on_board(player_turn)
         cheak_game_over()
         flip_player()
          
            

     if win=="x" or win=="o" :
            print(win+" won.")
     elif win == None :  
            print("tie.")

           
            
        



def position_on_board(player):

     print(player + "s'turn: ")
     
     valid= False
     while not  valid: 
            pos = input('enter the values from (1-9): ')

            while pos not in  ["1","2","3","4","5","6","7","8","9"] :
                pos =  input("put a valid value : ")
            position = int(pos) - 1 
            if board[int(position)] == '-':
                valid = True
            else:
                print('you cant go there , go again!!!! ')
                

     board[position] = player_turn
     game_board()
         


    
    

    

def cheak_game_over():
   cheak_if_won()
   cheak_if_tie()
   return

def cheak_if_won() :
    global win,collumn_win ,diagonal_win,row_win
    row_win = cheak_row()
    collumn_win = cheak_collumn()
    diagonal_win = cheak_diagonal()
    if row_win   :
        win = row_win
    elif collumn_win != None:
        win = collumn_win
    elif diagonal_win != None:
        win = diagonal_win
    else:
        win = None  


 
def cheak_row() :
        global win,collumn_win ,diagonal_win,row_win,game_not_over
        row_1 = board[0] == board[1] == board[2] != "-"
        row_2 = board[3] == board[4] == board[5] != "-"
        row_3 = board[6] == board[7] == board[8] != "-"
        if row_1 or row_2 or row_3 :
            game_not_over= False


        if row_1 :
            return board[0]
        elif row_2:
            return board[3]
        elif row_3:
            return board[6]
        else:
            return None

def cheak_collumn():
        global win,collumn_win ,diagonal_win,row_win,game_not_over
        collumn_1 = board[0] == board[3] == board[6] != "-"
        collumn_2 = board[1] == board[4] == board[7] != "-"
        collumn_3 = board[2] == board[5] == board[8] != "-"
        if collumn_1 or collumn_2 or collumn_3 :
            game_not_over = False

        if collumn_1 :
            return board[0]
        elif collumn_2:
            return board[1]
        elif collumn_3:
            return board[2]
        else:
            return None

def cheak_diagonal():
        global win,collumn_win ,diagonal_win,row_win, game_not_over
        diagonal_1 = board[0] == board[4] == board[8] != "-"
        diagonal_2 = board[2] == board[4] == board[6] != "-"
    
        if diagonal_1 or diagonal_2  :
            game_not_over = False

        if diagonal_1 :
            return board[0]
        elif diagonal_2:
            return board[2]
        else:
            return None

        
    
      

#cheak rows #cheak rows #cheak diagoanls
def cheak_if_tie():
     global game_not_over
     if "-" not in board:
            game_not_over = False
            
     return

def flip_player():
     global player_turn

     if player_turn == "x":
        player_turn = "o"
     elif player_turn == "o":
        player_turn = "x"
        
     return player_turn

play_game()