import math

# Constants to represent players
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

# Function to print the current state of the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Function to check if the current player has won
def check_win(board, player):
    for row in board:
        if row.count(player) == 3:
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full (draw)
def is_full(board):
    return all(board[row][col] != EMPTY for row in range(3) for col in range(3))

# Minimax algorithm to choose the best move for the AI
def minimax(board, depth, is_maximizing, alpha=-math.inf, beta=math.inf):
    # If AI wins, return a positive score
    if check_win(board, PLAYER_O):
        return 1
    # If human wins, return a negative score
    if check_win(board, PLAYER_X):
        return -1
    # If it's a draw, return 0
    if is_full(board):
        return 0

    # Maximizing for AI (O)
    if is_maximizing:
        max_eval = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER_O
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[row][col] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    # Minimizing for the opponent (X)
    else:
        min_eval = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER_X
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[row][col] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function to find the best move for the AI
def best_move(board):
    best_score = -math.inf
    move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER_O
                score = minimax(board, 0, False)
                board[row][col] = EMPTY
                if score > best_score:
                    best_score = score
                    move = (row, col)
    return move

# Function to handle the player's turn
def player_turn(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER_X
                break
            else:
                print("That spot is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid move. Please enter a number between 1 and 9.")

# Main function to run the game
def play_game():
    board = [[EMPTY] * 3 for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X' and the AI is 'O'.")
    print("The board is numbered as follows:")
    print("1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 9")

    while True:
        print_board(board)

        # Player's turn
        player_turn(board)
        if check_win(board, PLAYER_X):
            print_board(board)
            print("You win!")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # AI's turn
        print("AI is making its move...")
        row, col = best_move(board)
        board[row][col] = PLAYER_O
        if check_win(board, PLAYER_O):
            print_board(board)
            print("AI wins!")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
