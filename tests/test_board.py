import pytest
from simulation.models.board import create_monopoly_board
from simulation.models.square import Square

def test_board_length():
    """Ensure the board has exactly 40 squares."""
    board = create_monopoly_board()
    assert len(board) == 40, "The Monopoly board should have 40 squares."

def test_unique_positions():
    """Ensure each square has a unique position from 0 to 39."""
    board = create_monopoly_board()
    positions = [square.position for square in board]
    assert len(set(positions)) == 40, "All square positions should be unique."
    assert set(positions) == set(range(40)), "Positions should cover 0 through 39."

def test_go_square():
    """Check the first square is 'Go' at position 0."""
    board = create_monopoly_board()
    go_square = board[0]
    assert go_square.name == "Go"
    assert go_square.type == "go"
    assert go_square.position == 0

def test_boardwalk_square():
    """Check that Boardwalk is at position 39 with the correct attributes."""
    board = create_monopoly_board()
    boardwalk = board[39]
    assert boardwalk.name == "Boardwalk"
    assert boardwalk.type == "property"
    assert boardwalk.position == 39
    assert boardwalk.price == 400
    assert boardwalk.rent == [50, 200, 600, 1400, 1700, 2000]
    assert boardwalk.color == "dark_blue"

def test_sample_property():
    """
    Check a mid-board property (e.g., Illinois Avenue) 
    to ensure correct position, price, and rent.
    """
    board = create_monopoly_board()
    illinois_ave = board[24]  # position 24 is Illinois Avenue
    assert illinois_ave.name == "Illinois Avenue"
    assert illinois_ave.type == "property"
    assert illinois_ave.position == 24
    assert illinois_ave.price == 240
    assert illinois_ave.rent == [20, 100, 300, 750, 925, 1100]
    assert illinois_ave.color == "red"

def test_income_tax_square():
    """Verify Income Tax square at position 4."""
    board = create_monopoly_board()
    income_tax = board[4]
    assert income_tax.name == "Income Tax"
    assert income_tax.type == "tax"
    assert income_tax.position == 4
    # We treat 'price' as the tax amount in this simplified model
    assert income_tax.price == 200

def test_jail_square():
    """Check the Jail / Just Visiting square at position 10."""
    board = create_monopoly_board()
    jail_square = board[10]
    assert jail_square.name == "Jail / Just Visiting"
    assert jail_square.type == "jail"
    assert jail_square.position == 10

def test_railroad_example():
    """Verify Reading Railroad is at position 5 with correct price."""
    board = create_monopoly_board()
    reading_rr = board[5]
    assert reading_rr.name == "Reading Railroad"
    assert reading_rr.type == "railroad"
    assert reading_rr.position == 5
    assert reading_rr.price == 200

def test_community_chest_example():
    """Check a Community Chest square (e.g., position 2)."""
    board = create_monopoly_board()
    community_chest = board[2]
    assert community_chest.name == "Community Chest"
    assert community_chest.type == "community_chest"
    assert community_chest.position == 2

def test_chance_example():
    """Check a Chance square (e.g., position 7)."""
    board = create_monopoly_board()
    chance_square = board[7]
    assert chance_square.name == "Chance"
    assert chance_square.type == "chance"
    assert chance_square.position == 7