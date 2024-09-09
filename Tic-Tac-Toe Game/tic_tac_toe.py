#creating board for game

def print_board(board):
    for row in board:
        print(" | ".join(row)) #joins the elements of each row with "|" in betn
        print("-" * 9) #prints a line of "-" equal to the length of row


def check_winner (board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ": #iterates through each row (i = 0, 1, 2)
            return True
        
        if board[0][i] == board[1][i] == board[2][i] != " ": # #iterates through each column (i = 0, 1, 2)
            return True
        
        if board[0][0] == board[1][1] == board [2][2] != " ": #checks the diagonal from the top-left to the bottom-right 
            return True

        if board[0][2] == board[1][1] == board [2][0] != " ": #checks the diagonal from the top-right to the bottom-left 
            return True
        return False
    
    
#check if the board is full
def is_board_full(board):
    for row in board:
        if " " in row:
            return False
        return True
    

#Main function to play Tic-Tac-Toe

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}, it's your turn!")

        #Input Validation
        while True:
            try:
                row = int(input("Enter row (0, 1, or 2): "))
                col = int(input("Enter column (0, 1, or 2): "))
                if board [row][col] == " ":
                    board[row][col] = current_player
                    break
                else:
                    print("That spot is taken, try again")
            except (ValueError, IndexError):
                print("Invalid input, please enter a number between 0 and 2")


        if check_winner(board):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        #Switch Players

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
 play_game()



