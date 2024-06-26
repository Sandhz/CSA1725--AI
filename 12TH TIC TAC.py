import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def player_move(board):
    while True:
        row, col = map(int, input("Enter your move (row and column): ").split())
        if board[row][col] == " ":
            board[row][col] = "X"
            break
        else:
            print("That cell is already taken. Try again.")

def computer_move(board):
    empty_cells = get_empty_cells(board)
    row, col = random.choice(empty_cells)
    board[row][col] = "O"

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")

    while True:
        print_board(board)
        player_move(board)

        if check_winner(board, "X"):
            print_board(board)
            print("Congratulations! You win!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        computer_move(board)

        if check_winner(board, "O"):
            print_board(board)
            print("Computer wins!")
            break

if __name__ == "__main__":
    main()
