# Tic-Tac-Toe

A simple command-line Tic-Tac-Toe game built using Python 3.12.4.

## Features

- Interactive gameplay in the terminal
- Supports two players (X and O)
- Checks for winners and ties
- Validates user input

## Usage

1. Run the `tic_tac_toe.py` script.
2. The game board will be displayed with empty spots represented by spaces.
3. Player X goes first.
4. Enter the row and column numbers (0-2) to place your mark on the board.
5. The game will continue until a player wins or the board is full (tie).
6. The winner or tie result will be displayed.
7. The game will automatically switch to the other player's turn after each valid move.

## Code Structure

The code is organized into the following functions:

- `print_board(board)`: Prints the current state of the game board.
- `check_winner(board)`: Checks if a player has won the game by checking rows, columns, and diagonals.
- `is_board_full(board)`: Checks if the game board is full (no more empty spots).
- `play_game()`: Manages the main game loop, handles player input, updates the board, and checks for winners and ties.

The `play_game()` function initializes an empty 3x3 board and sets the starting player to "X". It then enters a loop that continues until a winner is found or the board is full (tie). Inside the loop, the current player's turn is displayed, and the function prompts the player to enter the row and column numbers to place their mark. Input validation is performed to ensure that the entered values are within the valid range (0-2) and that the chosen spot is empty.

After a valid move, the function checks if the current player has won the game using the `check_winner()` function. If no winner is found and the board is not full, the function switches to the other player's turn. The loop continues until a winner is found or the game ends in a tie.

## Dependencies

- Python 3.12.4 or higher

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to create a new issue or submit a pull request.
