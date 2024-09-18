# Dictionary holding Unicode symbols for white and black chess pieces
uniDict = {
    'WHITE': {"Pawn": "♙", "Rook": "♖", "Knight": "♘", "Bishop": "♗", "King": "♔", "Queen": "♕"},
    'BLACK': {"Pawn": "♟", "Rook": "♜", "Knight": "♞", "Bishop": "♝", "King": "♚", "Queen": "♛"}
}

# defining Constant players
WHITE = 'WHITE'
BLACK = 'BLACK'


#Initializes a piece with the specified color.
class Piece:
    def __init__(self, color):
        self.color = color

    def valid_moves(self, board, position): # board(list), position(tuple)
        # Abstract method to be overridden by subclasses
        raise NotImplementedError("This method should be overridden in subclasses")
    

# Class representing the King piece in a chess game.
class King(Piece):

    def valid_moves(self, board, position):
        """Calculate all valid moves for the King from the given position."""
        x, y = position
        moves = []

        # The king can move one square in any direction (horizontal, vertical, or diagonal)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 8 and 0 <= new_y < 8:  # Ensure the new position is within the board
                target = board.get((new_x, new_y), None)
                if target is None or target[0] != self.color:  # Empty square or opponent's piece
                    moves.append((new_x, new_y))

        return moves


# Class representing the Queen piece
class Queen(Piece):

    def valid_moves(self, board, position):
        """Calculate all valid moves for the Queen from the given position."""
        x, y = position
        moves = []

        # The queen can move in any number of squares in horizontal, vertical, or diagonal directions
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        for dx, dy in directions:
            for i in range(1, 8):
                new_x, new_y = x + i * dx, y + i * dy
                if 0 <= new_x < 8 and 0 <= new_y < 8:  # Ensure the new position is within the board
                    target = board.get((new_x, new_y), None)
                    if target is None:
                        moves.append((new_x, new_y))  # Empty square
                    elif target[0] != self.color:
                        moves.append((new_x, new_y))  # Capture opponent's piece
                        break  # Stop after capturing a piece
                    else:
                        break  # Stop if there's a piece of the same color
                else:
                    break  # Stop if the position is out of bounds

        return moves
    

# Class representing the Rook piece
class Rook(Piece):

    def valid_moves(self, board, position):
        """Calculate all valid moves for the Rook from the given position."""
        x, y = position
        moves = []

        # The rook can move horizontally or vertically any number of squares
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in directions:
            for i in range(1, 8):
                # new position by moving i squares in the (dx, dy) direction
                new_x, new_y = x + i * dx, y + i * dy
                # Ensure the new position is within the board boundaries
                if 0 <= new_x < 8 and 0 <= new_y < 8:
                    target = board.get((new_x, new_y), None)
                    if target is None:
                        moves.append((new_x, new_y))
                    elif target[0] != self.color:
                        moves.append((new_x, new_y))
                        break
                    else:
                        break
                else:
                    break

        return moves
    


# Class representing the Bishop piece
class Bishop(Piece):

    def valid_moves(self, board, position):
        """Calculate all valid moves for the Bishop from the given position."""
        x, y = position
        moves = []

        # The bishop moves diagonally in any direction
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        for dx, dy in directions:
            for i in range(1, 8):
                # Calculate the new position based on the direction and distance
                new_x, new_y = x + i * dx, y + i * dy
                if 0 <= new_x < 8 and 0 <= new_y < 8:
                    # Get the piece at the new position (if any)
                    target = board.get((new_x, new_y), None)
                    # if target pos. is empty, add it to the list of valid moves
                    if target is None:
                        moves.append((new_x, new_y))
                    # If the target position is occupied by an opponent's piece, add it to the list and stop further exploration in this direction
                    elif target[0] != self.color:
                        moves.append((new_x, new_y))
                        break
                    else:
                        break
                else:
                    break

        return moves


# Class representing the Knight piece
class Knight(Piece):

    def valid_moves(self, board, position):
        """Calculate all valid moves for the Knight from the given position."""
        x, y = position
        moves = []

        # The knight moves in an "L" shape: two squares in one direction and one square perpendicular
        knight_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

        for dx, dy in knight_moves:
            # Calculate the new position based on the knight's move
            new_x, new_y = x + dx, y + dy
            # Check if the new position is within the bounds of the board
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                target = board.get((new_x, new_y), None)
                # If the target position is empty or occupied by an opponent's piece, it's a valid move
                if target is None or target[0] != self.color:
                    moves.append((new_x, new_y))

        return moves
    

# Class representing the Pawn piece
class Pawn(Piece):

    def valid_moves(self, board, position):
        """Calculate all valid moves for the Pawn from the given position."""
        x, y = position
        moves = []

        # Pawn movement depends on the color
        if self.color == 'WHITE':
            # Move one square forward
            if board.get((x, y + 1)) is None:
                moves.append((x, y + 1))
                # Move two squares forward if on starting row
                if y == 1 and board.get((x, y + 2)) is None:
                    moves.append((x, y + 2))
            # Capture diagonally
            if board.get((x - 1, y + 1), None) and board.get((x - 1, y + 1))[0] == 'BLACK':
                moves.append((x - 1, y + 1))
            if board.get((x + 1, y + 1), None) and board.get((x + 1, y + 1))[0] == 'BLACK':
                moves.append((x + 1, y + 1))
        else:
            # Move one square forward
            if board.get((x, y - 1)) is None:
                moves.append((x, y - 1))
                # Move two squares forward if on starting row
                if y == 6 and board.get((x, y - 2)) is None:
                    moves.append((x, y - 2))
            # Capture diagonally
            if board.get((x - 1, y - 1), None) and board.get((x - 1, y - 1))[0] == 'WHITE':
                moves.append((x - 1, y - 1))
            if board.get((x + 1, y - 1), None) and board.get((x + 1, y - 1))[0] == 'WHITE':
                moves.append((x + 1, y - 1))

        return moves



# Class to represents a chessboard and manages the placement of chess pieces.

class Board:

    def __init__(self):
        # For simplicity, a dictionary where keys are tuples (x, y) and values are (color, piece)
        # Example: {(0, 0): ('WHITE', 'Rook'), (7, 7): ('BLACK', 'Queen')}
        self.board = self.setup_board()
        # Dictionaries to store captured pieces
        self.captured_pieces = {
            'WHITE': [],
            'BLACK': []
        }

    # function to set up the initial position of the chess pieces.
    def setup_board(self):
        """Set up the initial position of the chess pieces."""
        board = {}
        # Placing white pieces
        board[(0, 0)] = ('WHITE', 'Rook')
        board[(1, 0)] = ('WHITE', 'Knight')
        board[(2, 0)] = ('WHITE', 'Bishop')
        board[(3, 0)] = ('WHITE', 'Queen')
        board[(4, 0)] = ('WHITE', 'King')
        board[(5, 0)] = ('WHITE', 'Bishop')
        board[(6, 0)] = ('WHITE', 'Knight')
        board[(7, 0)] = ('WHITE', 'Rook')
        for x in range(8):
            board[(x, 1)] = ('WHITE', 'Pawn')

        # Placing black pieces
        board[(0, 7)] = ('BLACK', 'Rook')
        board[(1, 7)] = ('BLACK', 'Knight')
        board[(2, 7)] = ('BLACK', 'Bishop')
        board[(3, 7)] = ('BLACK', 'Queen')
        board[(4, 7)] = ('BLACK', 'King')
        board[(5, 7)] = ('BLACK', 'Bishop')
        board[(6, 7)] = ('BLACK', 'Knight')
        board[(7, 7)] = ('BLACK', 'Rook')
        for x in range(8):
            board[(x, 6)] = ('BLACK', 'Pawn')

        return board
    

    # Function to print the board design in console
    def print_board(self):
        """Print the current state of the chessboard with grid lines and aligned headers."""
        print("   " + " ".join(f" {chr(c)} " for c in range(ord('a'), ord('h') + 1)))
        print("  +" + "---+" * 8)  # Top border

        for y in range(7, -1, -1):
            # Print the row number on the left side of board
            print(f"{y + 1} |", end="")
            for x in range(8):
                 # Retrieve the piece at the current position (x, y) 
                piece = self.board.get((x, y), None)
                if piece:
                    color, piece_type = piece
                    piece_symbol = uniDict[color][piece_type]
                    print(f" {piece_symbol} |", end="")
                # If no piece is present, print an empty space
                else:
                    print("   |", end="")
            print(f" {y + 1}")
            print("  +" + "---+" * 8)

        # Print captured pieces
        print("\nCaptured Pieces:")
        print("White:", " ".join(uniDict['WHITE'].get(piece, '') for piece in self.captured_pieces['WHITE']))
        print("Black:", " ".join(uniDict['BLACK'].get(piece, '') for piece in self.captured_pieces['BLACK']))


    # Function to handle moving the piece from start_pos to end_pos
    def move_piece(self, start_pos, end_pos):
        if start_pos not in self.board:
            print("No piece at the start position!")
            return False
        # Get the piece information at the starting position
        piece = self.board[start_pos]
        piece_color, piece_type = piece

        # Assuming each piece type is a class with a valid_moves method
        piece_obj = globals()[piece_type](piece_color)  # Dynamically create the piece object
        valid_moves = piece_obj.valid_moves(self.board, start_pos)

        if end_pos in valid_moves:
            # Check if the end position is a valid move
            if end_pos in self.board:
                target_piece = self.board[end_pos]
                target_color, target_type = target_piece
                if target_color != piece_color:
                    print(f"{piece_type} captures {target_type}!")
                    # Add the captured piece to the captured list
                    self.captured_pieces[target_color].append(target_type)
                else:
                    print("You can't capture your own piece!")
                    return False
            # Move the piece
            self.board[end_pos] = self.board.pop(start_pos)
            return True
        else:
            print("Invalid move!")
            return False



# Class to initialize the game with its logic

class Game:

    # Function to initialize the game board and set the starting turn to WHITE
    def __init__(self):
        self.board = Board()
        self.current_turn = "WHITE"  
        self.check_printed = False  # Flag to track if check message has been printed


    """Main game loop to play the game."""
    def play(self):
        while True:
            self.board.print_board()

            # Check if the current player's king is on the board
            if not self.is_king_on_board():
                print(f"King gone! Game over. {self.current_turn} loses.")
                break

             # Check for checkmate
            if self.is_checkmate():
                self.board.print_board()
                print(f"Checkmate! {self.current_turn} loses.")
                break

             # Check for stalemate
            if self.is_stalemate():
                self.board.print_board()
                print("Stalemate! The game is a draw.")
                break

            # Get the move from the current player
            move = input(f"{self.current_turn}'s move (e.g., 'e2 e4'): ")
            start_pos, end_pos = self.parse_move(move)

            # Validate the move
            if not self.validate_move(start_pos, end_pos):
                print("Invalid move. Try again.")
                continue
            # Move the piece
            self.board.move_piece(start_pos, end_pos)

            # Check if the king is in check after the move
            king_position = next((pos for pos, (color, piece) in self.board.board.items()
                              if piece == "King" and color == self.current_turn), None)
            if king_position and self.is_in_check(king_position):
                print(f"King is in check at {king_position}")

            # Switch to the other player's turn
            self.switch_turn()


    # Function to convert move notation (e.g., 'e2 e4') to board coordinates.
    def parse_move(self, move):
        """Convert move notation (e.g., 'e2 e4') to board coordinates."""
        try:
            start, end = move.split()
            start_pos = (ord(start[0]) - ord('a'), int(start[1]) - 1)
            end_pos = (ord(end[0]) - ord('a'), int(end[1]) - 1)
            return start_pos, end_pos
        except (IndexError, ValueError):
            print("Invalid input format.")
            return None, None

    # Function to validate the move based on the current board state.
    def validate_move(self, start_pos, end_pos):
        """Validate the move based on the current board state."""
        if start_pos is None or end_pos is None:
            return False

        piece = self.board.board.get(start_pos)
        if not piece:
            print("No piece at the start position!")
            return False

        piece_color, piece_type = piece
        if piece_color != self.current_turn:
            print(f"Not your turn! {piece_color} pieces cannot move.")
            return False

        piece_obj = globals()[piece_type](piece_color)
        if end_pos not in piece_obj.valid_moves(self.board.board, start_pos):
            print("Move is not valid for this piece.")
            return False

        return True
    

    # Function to check if the current player's king is in checkmate.
    def is_checkmate(self):
        """Check if the current player's king is in checkmate."""
        king_position = next((pos for pos, (color, piece) in self.board.board.items()
                          if piece == "King" and color == self.current_turn), None)

        if king_position is None:
            print("King not found on the board!")
            return False

        if self.is_in_check(king_position):
            print(f"King is in check at {king_position}")

            # Check if there are any valid moves to escape the check
            board_items = list(self.board.board.items())  # Create a list of board items
            for start_pos, (piece_color, piece_type) in board_items:
                if piece_color == self.current_turn:
                    piece_obj = globals()[piece_type](piece_color)
                    for move in piece_obj.valid_moves(self.board.board, start_pos):
                        # Save the original piece and its position
                        original_piece = self.board.board.get(move)
                        # Make the move
                        self.board.move_piece(start_pos, move)
                        # Check if the king is still in check
                        if not self.is_in_check(king_position):
                            # Undo the move
                            self.board.board[start_pos] = (piece_color, piece_type)
                            if original_piece:
                                self.board.board[move] = original_piece
                            else:
                                del self.board.board[move]
                            return False
                        # Undo the move
                        self.board.board[start_pos] = (piece_color, piece_type)
                        if original_piece:
                            self.board.board[move] = original_piece
                        else:
                            del self.board.board[move]

            print(f"Checkmate! {self.current_turn} loses.")
            return True

        return False
    

    # Function to check if the game is in a stalemate situation.
    def is_stalemate(self):
        king_position = self.get_king_position(self.current_turn)

        # If the king is not in check
        if king_position and not self.is_in_check(king_position):
            # Loop through all pieces of the current player
            for start_pos, (color, piece_type) in list (self.board.board.items()):
                if color == self.current_turn:
                    piece_obj = globals()[piece_type](color)
                    # Check if the piece has any valid moves
                    for move in piece_obj.valid_moves(self.board.board, start_pos):
                        # Temporarily make the move and see if it leads to a legal position
                        original_piece = self.board.board.get(move)
                        self.board.move_piece(start_pos, move)

                        # If any valid move exists, it's not stalemate
                        if not self.is_in_check(self.get_king_position(self.current_turn)):
                            # Undo the move and continue the game
                            self.board.board[start_pos] = (color, piece_type)
                            if original_piece:
                                self.board.board[move] = original_piece
                            else:
                                del self.board.board[move]
                            return False

                        # Undo the move to restore the original board state
                        self.board.board[start_pos] = (color, piece_type)
                        if original_piece:
                            self.board.board[move] = original_piece
                        else:
                            del self.board.board[move]

            # If no valid moves are found and the king is not in check, it's stalemate
            print("Stalemate! The game is a draw.")
            return True
        return False


    # Function to check if the current player's king is on the board.
    def is_king_on_board(self):
        """Check if the current player's king is on the board."""
        return self.get_king_position(self.current_turn) is not None

    # Find the position of the king for the given color.
    def get_king_position(self, color):
        """Find the position of the king for the given color."""
        for pos, (piece_color, piece_type) in self.board.board.items():
            if piece_type == "King" and piece_color == color:
                return pos
        return None
    
    
    # Function to check if the king at the given position is in check
    def is_in_check(self, king_position):
        """Check if the king at the given position is in check."""
        try:
            king_color = next(color for pos, (color, piece) in self.board.board.items()
                          if piece == "King" and pos == king_position)
        except StopIteration:
            return False  # Assuming king not found means no check

        opponent_color = "BLACK" if king_color == "WHITE" else "WHITE"

        for pos, (color, piece) in self.board.board.items():
            if color == opponent_color:
                piece_obj = globals()[piece](color)
                if king_position in piece_obj.valid_moves(self.board.board, pos):
                    return True

        return False
    
    # Function to Switch turn between white and black.
    def switch_turn(self):
        """Switch turn between white and black."""
        self.current_turn = "BLACK" if self.current_turn == "WHITE" else "WHITE"

    # Function to convert board position (x, y) to chess notation.
    def convert_position(self, position):
        """Convert board position (x, y) to chess notation."""
        return f"{chr(position[0] + ord('a'))}{position[1] + 1}"

if __name__ == "__main__":
    # Create an instance of the Game class to start a new game.
    game = Game()
    game.play() 
