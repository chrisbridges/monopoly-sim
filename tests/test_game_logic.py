# tests/test_monopoly_game.py
from simulation.game_engine.movement import roll_dice
from simulation.models.square import Square
from simulation.game_engine.game import MonopolyGame
import pytest
import random

@pytest.fixture
def small_game():
    """Returns a MonopolyGame with two players for testing."""
    game = MonopolyGame(["Alice", "Bob"])
    return game

def test_roll_dice(small_game):
    """Check dice roll is between 2 and 12."""
    for _ in range(100):
        roll = roll_dice()
        assert 2 <= roll <= 12

def test_move_player(small_game):
    """Verify player position and passing Go logic."""
    player = small_game.players[0]
    player.position = 38
    small_game.move_player(player, 4)  # 38 + 4 = 42 -> 42 % 40 = 2
    assert player.position == 2
    # Passed Go, so +200
    assert player.money == 1700

def test_handle_property_buy(small_game):
    """Check property purchase logic."""
    # Force the board to have a known property at position 1
    small_game.board = [
        Square(name="Go", type="go", position=0),
        Square(name="Test Property", type="property", position=1, price=100, rent=[10]),
    ] + [Square(name=f"Dummy {i}", type="go", position=i) for i in range(2, 40)]

    player = small_game.players[0]
    player.position = 1
    small_game.handle_square(player)
    assert small_game.board[1].owner == player.name
    assert player.money == 1400  # 1500 - 100

def test_handle_property_rent(small_game):
    """Check paying rent to another player."""
    small_game.board = [
        Square(name="Go", type="go", position=0),
        Square(name="Test Property", type="property", position=1, price=100, rent=[10], owner="Bob"),
    ] + [Square(name=f"Dummy {i}", type="go", position=i) for i in range(2, 40)]

    alice = small_game.players[0]
    bob = small_game.players[1]

    alice.position = 1
    small_game.handle_square(alice)
    # Alice pays 10 rent to Bob
    assert alice.money == 1490
    assert bob.money == 1510

def test_handle_tax(small_game):
    """Check paying tax."""
    small_game.board = [
        Square(name="Income Tax", type="tax", position=0, price=200),
    ] + [Square(name=f"Dummy {i}", type="go", position=i) for i in range(1, 40)]

    player = small_game.players[0]
    player.position = 0
    small_game.handle_square(player)
    assert player.money == 1300  # 1500 - 200

def test_send_to_jail(small_game):
    """Check jail logic."""
    alice = small_game.players[0]
    small_game.send_to_jail(alice)
    assert alice.position == 10
    assert alice.in_jail is True
    assert alice.jail_turns == 0

def test_integration_run_game():
    """Run a small game with random outcomes to ensure it completes."""
    game = MonopolyGame(["Alice", "Bob"])
    # We don't need to assert the final state in detail—just that it terminates.
    game.run_game()
    # Check that the game ended
    assert game.game_over is True
    # At least one player has money >= 0
    survivors = [p for p in game.players if p.money >= 0]
    assert len(survivors) >= 1