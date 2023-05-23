import random

def print_board(board):
    print("---------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i*3+j], end=" | ")
        print("\n---------")

def check_winner(board):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            return board[i]

    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            return board[i]

    # Check diagonals
    if board[0] == board[4] == board[8] != " ":
        return board[0]
    if board[2] == board[4] == board[6] != " ":
        return board[2]

    return None

def is_board_full(board):
    for cell in board:
        if cell == " ":
            return False
    return True

def player_turn(board):
    print_board(board)
    while True:
        move = int(input("Enter your move (0-8): "))

        if move >= 0 and move < 9 and board[move] == " ":
            board[move] = "X"
            break
        else:
            print("Invalid move. Try again.")

def computer_turn(board):
    while True:
        move = random.randint(0, 8)

        if board[move] == " ":
            board[move] = "O"
            break

def play_game():
    board = [" " for _ in range(9)]
    current_player = "X"

    while True:
        if current_player == "X":
            player_turn(board)
        else:
            computer_turn(board)

        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == "X":
                print("Congratulations! You win!")
            else:
                print("Oops! Computer wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

play_game()
