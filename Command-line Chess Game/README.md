# Command-Line Chess Game

Welcome to the Command-Line Chess Game! This is a simple, yet comprehensive chess game implemented in Python.  
It features a command-line interface and supports basic chess rules, including check and checkmate detection.  

## Introduction

This chess game allows two players to play chess from the command line. It includes Unicode symbols for chess pieces, supports all standard chess moves, and validates game states such as check and checkmate.  
The game is played by entering moves in standard algebraic notation, such as 'e2 e4'.

## Requirements

To run this game, you need:

1. **Python 3.12.4**: The game is developed using Python 3.12.4. Make sure you have Python installed on your system.

2. **Unicode Support**: The game uses Unicode symbols for chess pieces. Ensure that your terminal or IDE supports Unicode. For Visual Studio Code, you may need to:
   - Go to Extensions(ctrl+ shift+ X) for windows  
   - search for  ' insert unicode' and install it.  
   - Open Command Palette, Press (Ctrl + Shift + P), search for Insert Unicode Command ans type chess , the characters will be visible. you can choose the required one..  


## How to Play

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/chess-game.git
    cd chess-game
    ```

2. **Run the Game**:
    ```bash
    python chess_game.py
    ```

3. **Input Moves**: Enter moves in algebraic notation. For example, to move a pawn from e2 to e4, type:
    ```text
    e2 e4
    ```

4. **Game Progress**: The game will print the board after each move and announce game states such as check, checkmate, or stalemate.

## Code Explanation
## Code Explanation

1. **Unicode Dictionary**:
   - `uniDict`: Stores Unicode symbols for white and black chess pieces.

2. **Piece Class**:
   - `Piece`: Base class for all chess pieces with an abstract method `valid_moves` that needs to be implemented by subclasses.

3. **Piece Classes**:
   - **King**: Moves one square in any direction. Determines valid moves based on position.
   - **Queen**: Moves in horizontal, vertical, or diagonal directions for any number of squares.
   - **Rook**: Moves horizontally or vertically for any number of squares.
   - **Bishop**: Moves diagonally for any number of squares.
   - **Knight**: Moves in an "L" shape: two squares in one direction and one square perpendicular.
   - **Pawn**: Moves forward one or two squares from its starting position and captures diagonally.

4. **Board Class**:
   - **Setup**: Initializes the board with pieces in their starting positions.
   - **Print Board**: Displays the current state of the board with Unicode symbols.
   - **Move Piece**: Handles the movement of pieces and updates the board. Captures opponent pieces and tracks them.

5. **Game Class**:
   - **Initialization**: Sets up the board and starts the game with the white player.
   - **Main Loop**: Handles turns, checks for game end conditions (checkmate, stalemate), and processes player moves.
   - **Move Validation**: Ensures moves are valid and updates the board accordingly.
   - **Check/Checkmate/Stalemate**: Determines if a king is in check, checkmate, or if the game is in a stalemate.


## Contributing

Contributions are welcome! If you have suggestions or improvements, please fork the Repository or, Submit a pull request
