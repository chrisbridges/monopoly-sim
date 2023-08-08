from models.board import MonopolyBoard
from models.spaces import spaces

def create_complete_monopoly_board():
    board = MonopolyBoard()
    
    for space in spaces:
        board.add_space(*space)
    
    return board

# board = create_complete_monopoly_board()

# Display the first 10 spaces for demonstration
# display_first_n_spaces(board, 10)
if __name__ == '__main__':
  create_complete_monopoly_board()