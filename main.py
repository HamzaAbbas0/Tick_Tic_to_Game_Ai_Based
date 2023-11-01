import random

# Create the Tic-Tac-Toe board
board = [' ' for _ in range(9)]

# Function to display the Tic-Tac-Toe board
def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check for a win
def check_win(board, player):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Function to make a player move
def make_move(board, position, player):
    if board[position] == ' ':
        board[position] = player
        return True
    else:
        return False

# Function for the AI's move (random)
def ai_move(board):
    available_moves = [i for i, val in enumerate(board) if val == ' ']
    if available_moves:
        return random.choice(available_moves)
    return None

# Main game loop
while True:
    display_board(board)

    # Player's move
    player_position = int(input("Enter your move (0-8): "))
    if make_move(board, player_position, 'X'):
        if check_win(board, 'X'):
            display_board(board)
            print("You win!")
            break
        if ' ' not in board:
            display_board(board)
            print("It's a draw!")
            break

    # AI's move
    ai_position = ai_move(board)
    if ai_position is not None:
        make_move(board, ai_position, 'O')
        if check_win(board, 'O'):
            display_board(board)
            print("AI wins!")
            break
        if ' ' not in board:
            display_board(board)
            print("It's a draw!")
            break
