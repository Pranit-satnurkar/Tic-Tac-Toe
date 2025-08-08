# ==============================================================================
# Python Tic-Tac-Toe Game (Console-based)
# This program allows two players to play a classic game of Tic-Tac-Toe
# by entering a number from 1 to 9 to place their move.
# ==============================================================================

# The game board is represented as a list.
# We initialize it with numbers 1-9 to represent the positions.
board = [' ' for _ in range(9)] # The board will be a list of 9 empty strings

def print_board():
    """
    This function prints the current state of the Tic-Tac-Toe board.
    It displays a 3x3 grid with the player's marks.
    """
    print('-------------')
    print(f'| {board[0]} | {board[1]} | {board[2]} |')
    print('-------------')
    print(f'| {board[3]} | {board[4]} | {board[5]} |')
    print('-------------')
    print(f'| {board[6]} | {board[7]} | {board[8]} |')
    print('-------------')

def check_win(player):
    """
    This function checks all possible winning combinations to see if
    the current player has won the game.
    A winning combination is three of the same marks in a row.
    """
    # Check rows
    if (board[0] == player and board[1] == player and board[2] == player) or \
       (board[3] == player and board[4] == player and board[5] == player) or \
       (board[6] == player and board[7] == player and board[8] == player):
        return True
    
    # Check columns
    elif (board[0] == player and board[3] == player and board[6] == player) or \
         (board[1] == player and board[4] == player and board[7] == player) or \
         (board[2] == player and board[5] == player and board[8] == player):
        return True
        
    # Check diagonals
    elif (board[0] == player and board[4] == player and board[8] == player) or \
         (board[2] == player and board[4] == player and board[6] == player):
        return True
    
    else:
        return False

def check_tie():
    """
    This function checks if all spaces on the board are filled.
    If so, and no player has won, the game is a tie.
    """
    for cell in board:
        if cell == ' ':
            return False # If any space is empty, it's not a tie yet
    return True # All spaces are filled

def main():
    """
    The main function to run the game. It controls the game loop,
    player turns, and the end game conditions.
    """
    print("Welcome to Tic-Tac-Toe!")
    print("Player 1 is 'X', Player 2 is 'O'.")
    print("The board positions are numbered 1 to 9.")

    current_player = 'X'
    game_running = True
    
    while game_running:
        print_board()
        
        try:
            # Prompt the current player for their move
            move = int(input(f"Player '{current_player}', enter your move (1-9): "))
            
            # Adjust for 0-based list index
            move -= 1

            # Check if the move is valid (within range and space is empty)
            if 0 <= move <= 8 and board[move] == ' ':
                board[move] = current_player
                
                # Check for win or tie
                if check_win(current_player):
                    print_board()
                    print(f"Congratulations, Player '{current_player}' wins!")
                    game_running = False
                elif check_tie():
                    print_board()
                    print("The game is a tie!")
                    game_running = False
                else:
                    # Switch to the other player
                    current_player = 'O' if current_player == 'X' else 'X'
            else:
                print("Invalid move. That spot is already taken or out of range. Try again.")
        
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")
            
if __name__ == "__main__":
    main()

