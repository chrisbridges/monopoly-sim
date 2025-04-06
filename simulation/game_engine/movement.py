import random
from dataclasses import replace
from typing import Tuple
from models.player import Player
from models.constants import CONSTANTS
from game_engine import actions
from models.square import Railroad, Utility

def roll_dice() -> Tuple[int, int]:
    """Roll two dice and return their values."""
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2

def move(player: Player) -> Player:
    """
    Pure function that simulates rolling dice and moving the player.
    Returns a new Player state and the dice total.
    
    - Updates doubles_count: if the player rolled doubles, increments the count; otherwise resets it.
    - Updates position based on dice roll.
    - If the player passes GO (i.e. new position is numerically lower than old position), adds $200.
    """
    dice1, dice2 = roll_dice()
    total = dice1 + dice2
    rolled_doubles = (dice1 == dice2)
    
    # Update doubles_count: increment if doubles, otherwise reset to 0.
    new_doubles_count = player.doubles_count + 1 if rolled_doubles else 0

    if new_doubles_count == 3:
        return send_to_jail(player)

    old_position = player.position
    new_position = (old_position + total) % CONSTANTS.BOARD_LENGTH
    player_passed_go = new_position < old_position
    
    new_money = player.money
    if player_passed_go:
        player_with_go_money = actions.give_player_go_money(player)
        new_money = player_with_go_money.money

    # Create a new Player with updated state.
    return replace(player,
                    money=new_money,
                    position=new_position,
                    doubles_count=new_doubles_count)

def advance_to_go(player: Player) -> Player:
    """
    Move the player directly to GO and collect $200.
    This is a special case for certain cards or squares.
    """
    return replace(player, position=CONSTANTS.GO_POSITION, money=player.money + CONSTANTS.GO_MONEY)

def send_to_jail(player: Player) -> Player:
    print(f"{player.name} goes to Jail!")
    return replace(player, 
                   in_jail=True, 
                   position=CONSTANTS.JAIL_POSITION, 
                   jail_turns=0, 
                   doubles_count=0)

# TODO: leverage all these direct movement funcs with "handle_square" in actions?
def move_player_directly_to_square(player: Player, square_position: int) -> Player:
    """
    Move the player directly to a specified square position.
    This is used for certain cards or game mechanics.
    """
    return replace(player, position=square_position)

def move_player_back_3_spaces(player: Player) -> Player:
    """
    Move the player back 3 spaces.
    This is used for certain cards or game mechanics.
    """
    new_position = (player.position - 3) % CONSTANTS.BOARD_LENGTH
    return replace(player, position=new_position)

def move_nearest_utility(player: Player, board) -> Player:
    """
    Move the player to the nearest utility.
    If the utility is unowned, the player can buy it.
    If owned, pay 10x the dice roll to the owner.
    """
    # Find the nearest utility
    utilities = [square for square in board if isinstance(square, Utility)]
    current_position = player.position
    nearest_utility = min(utilities, key=lambda x: (x.position - current_position) % CONSTANTS.BOARD_LENGTH)
    
    return move_player_directly_to_square(player, nearest_utility.position)

def move_nearest_railroad(player: Player, board) -> Player:
    """
    Move the player to the nearest railroad.
    If the railroad is unowned, the player can buy it.
    If owned, pay twice the rental to the owner.
    """
    # Find the nearest railroad
    railroads = [square for square in board if isinstance(square, Railroad)]
    current_position = player.position
    nearest_railroad = min(railroads, key=lambda x: (x.position - current_position) % CONSTANTS.BOARD_LENGTH)
    
    return move_player_directly_to_square(player, nearest_railroad.position)