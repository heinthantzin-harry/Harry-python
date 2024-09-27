# Simplified chess game

# Define the initial positions of the pieces on a standard chessboard
def initialize_board():
    return [
        ["r", "n", "b", "q", "k", "b", "n", "r"],  # Black's pieces
        ["p", "p", "p", "p", "p", "p", "p", "p"],  # Black's pawns
        [" ", " ", " ", " ", " ", " ", " ", " "],  # Empty space
        [" ", " ", " ", " ", " ", " ", " ", " "],  # Empty space
        [" ", " ", " ", " ", " ", " ", " ", " "],  # Empty space
        [" ", " ", " ", " ", " ", " ", " ", " "],  # Empty space
        ["P", "P", "P", "P", "P", "P", "P", "P"],  # White's pawns
        ["R", "N", "B", "Q", "K", "B", "N", "R"]   # White's pieces
    ]

# Function to display the current chessboard
def display_board(board):
    print("  a b c d e f g h")
    print("  ----------------")
    for row in range(8):
        print(f"{8-row} " + " ".join(board[row]) + f" {8-row}")
    print("  ----------------")
    print("  a b c d e f g h")

# Translate user input (like 'e2') into row and column indices
def position_to_index(pos):
    column = ord(pos[0]) - ord('a')  # Convert letter to column index
    row = 8 - int(pos[1])  # Convert number to row index (8 -> 0, 7 -> 1, etc.)
    return row, column

# Main function to handle the game
def play_game():
    board = initialize_board()
    current_player = "White"  # White always starts first

    while True:
        display_board(board)
        print(f"{current_player}'s turn. Enter your move (e.g., e2 e4):")
        
        move = input().split()  # Input in the form of "e2 e4"
        
        if len(move) != 2:
            print("Invalid input. Please enter your move as 'e2 e4'.")
            continue
        
        start_pos, end_pos = move[0], move[1]
        start_row, start_col = position_to_index(start_pos)
        end_row, end_col = position_to_index(end_pos)
        
        # Get the piece at the starting position
        piece = board[start_row][start_col]
        
        # Check if the move is valid (in a real game, more rules are needed)
        if piece == " ":
            print("Invalid move. There's no piece at the start position.")
            continue
        
        # Check if it's the right player's turn
        if (current_player == "White" and piece.islower()) or (current_player == "Black" and piece.isupper()):
            print("Invalid move. It's not your turn.")
            continue
        
        # Make the move
        board[start_row][start_col] = " "  # Remove the piece from the start
        board[end_row][end_col] = piece  # Place the piece at the end
        
        # Switch turns
        current_player = "Black" if current_player == "White" else "White"

# Run the game
play_game()