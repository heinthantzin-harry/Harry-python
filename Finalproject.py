def display_board(board: list[str]) -> None:
    """
    Function to display the current board situation.
    
    Args:
    board: list - current game board
    
    Return:
    None
    """
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("___|___|___")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("___|___|___")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def check_win(board: list[str], player: str) -> bool:
    """
    Function to check if the current player has won.
    
    Args:
    board: list - current game board
    player: str - current player
    
    Return:
    bool: True if the player has won, else False
    """
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    
    return any(board[combo[0]] == board[combo[1]] == board[combo[2]] == player for combo in win_combinations)


def check_tie(board: list[str]) -> bool:
    """
    Function to check if the game is a tie.
    
    Args:
    board: list - current game board
    
    Return:
    bool: True if the game is a tie, else False
    """
    return " " not in board


def play_game() -> bool:
    """
    Function to play a single game of tic-tac-toe.
    
    Return:
    bool: True if the player wants to restart, else False
    """
    board = [" "] * 9
    current_player = "H"
    
    while True:
        display_board(board)
        move = input(f"Player {current_player}, enter your move (1-9): ")
        
        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print("Invalid move. Please enter a number between 1 and 9.")
            continue
        
        move = int(move) - 1 
        
        if board[move] != " ":
            print("This space is already taken. Try again.")
            continue
        
        board[move] = current_player
        if check_win(board, current_player):
            display_board(board)
            print(f"Congratulations {current_player}, you win!")
            break

        if check_tie(board):
            display_board(board)
            print("It's a tie! Please play again.")
            break

        current_player = "I" if current_player == "H" else "H"
    
    restart = input("Do you want to play again? (yes/no): ").strip().lower()
    return restart == "yes"


def show_menu() -> None:
    """
    Function to display the main menu and handle user choices.
    
    Return:
    None
    """
    while True:
        print("Welcome to Tic-Tac-Toe!")
        print("1. Play Game")
        print("2. Exit")
        
        choice = input("Please select an option (1/2): ").strip()
        
        if choice == "1":
            while play_game():
                pass
        elif choice == "2":
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid option. Please select 1 or 2.")

if __name__ == "__main__":
    show_menu()