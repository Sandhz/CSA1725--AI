import math

# Constants representing different players
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

def evaluate(board):
    """
    Evaluate the current state of the board.
    """
    # Check rows
    for row in board:
        if row.count(PLAYER_X) == 3:
            return 10
        elif row.count(PLAYER_O) == 3:
            return -10
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == PLAYER_X:
            return 10
        elif board[0][col] == board[1][col] == board[2][col] == PLAYER_O:
            return -10
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == PLAYER_X or \
       board[0][2] == board[1][1] == board[2][0] == PLAYER_X:
        return 10
    elif board[0][0] == board[1][1] == board[2][2] == PLAYER_O or \
         board[0][2] == board[1][1] == board[2][0] == PLAYER_O:
        return -10
    
    # No winner
    return 0

def is_moves_left(board):
    """
    Check if there are any empty cells left on the board.
    """
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return True
    return False

def alpha_beta_pruning(board, depth, alpha, beta, is_max):
    """
    Alpha-Beta pruning algorithm implementation.
    """
    score = evaluate(board)
    
    # If maximizer or minimizer wins, return the score
    if score == 10:
        return score - depth
    elif score == -10:
        return score + depth
    
    # If there are no moves left or the game is a draw, return 0
    if not is_moves_left(board):
        return 0
    
    if is_max:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    best_score = max(best_score, alpha_beta_pruning(board, depth+1, alpha, beta, not is_max))
                    board[i][j] = EMPTY
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    best_score = min(best_score, alpha_beta_pruning(board, depth+1, alpha, beta, not is_max))
                    board[i][j] = EMPTY
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score

def find_best_move(board):
    """
    Find the best move for the AI using Alpha-Beta pruning algorithm.
    """
    best_move = (-1, -1)
    best_score = -math.inf
    alpha = -math.inf
    beta = math.inf
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                move_score = alpha_beta_pruning(board, 0, alpha, beta, False)
                board[i][j] = EMPTY
                if move_score > best_score:
                    best_score = move_score
                    best_move = (i, j)
    return best_move

def print_board(board):
    """
    Print the Tic Tac Toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("---------")

def main():
    # Initialize the Tic Tac Toe board
    board = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    
    # Main game loop
    while is_moves_left(board):
        print_board(board)
        
        # Player's move
        row = int(input("Enter the row (0, 1, or 2): "))
        col = int(input("Enter the column (0, 1, or 2): "))
        if board[row][col] != EMPTY:
            print("Cell already occupied. Please choose another cell.")
            continue
        board[row][col] = PLAYER_O
        
        # Check if player wins
        if evaluate(board) == -10:
            print_board(board)
            print("Congratulations! You win!")
            break
        
        # AI's move
        ai_row, ai_col = find_best_move(board)
        board[ai_row][ai_col] = PLAYER_X
        
        # Check if AI wins
        if evaluate(board) == 10:
            print_board(board)
            print("AI wins! Better luck next time!")
            break
    else:
        print_board(board)
        print("It's a draw!")

if __name__ == "__main__":
    main()
