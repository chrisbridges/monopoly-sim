def create_complete_monopoly_board():
    # board = MonopolyBoard()
    
    for space in spaces:
        board.add_space(*space)
    
    return board

board = create_complete_monopoly_board()

# Display the first 10 spaces for demonstration
display_first_n_spaces(board, 10)
